import uuid
from copy import deepcopy
from datetime import datetime
from datetime import timedelta

from jose import jwt, JWTError
from fastapi import status, HTTPException, Depends
from pydantic import ValidationError

from passlib.hash import bcrypt
from fastapi.security import OAuth2PasswordBearer

import models

from settings import settings
from database import users_collection
from database import courses_collection
from database import lessons_collection
from database import redis_db

oauth2_schema = OAuth2PasswordBearer(tokenUrl='/auth/sign-in')


def get_current_user(token: str):
    return AuthService.validate_token(token)


def generate_lessons_schedule(weekdays: list[int], lessons_amount: int, first_lesson_date: datetime):
    first_lesson_weekday = first_lesson_date.isoweekday()
    if first_lesson_weekday in weekdays:
        delta_index = weekdays.index(first_lesson_weekday)
    else:
        return []

    i = 0
    lessons_schedule = []
    prev_lesson = first_lesson_date
    while i < lessons_amount:
        if delta_index != len(weekdays) - 1:
            delta = weekdays[delta_index + 1] - weekdays[delta_index]
            delta_index += 1
        else:
            delta_index = 0
            delta = weekdays[0] - weekdays[-1] + 7

        next_lesson = prev_lesson + timedelta(days=delta)
        prev_lesson = next_lesson
        lessons_schedule.append(next_lesson)
        i += 1
    return lessons_schedule

class AuthService:
    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return bcrypt.verify(plain_password, hashed_password)

    @classmethod
    def hash_password(cls, password: str) -> str:
        return bcrypt.hash(password)

    @classmethod
    def validate_token(cls, token: str) -> models.User:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='could not authorize credentials',
            headers={
                'WWW-authenticate': 'Bearer'
            },
        )
        try:
            payload = jwt.decode(
                token,
                settings.jwt_secret,
                algorithms=[settings.jwt_algorithm]
            )
        except JWTError:
            raise exception from None

        user_data = payload.get('user')

        try:
            user = models.User.parse_obj(user_data)
        except ValidationError:
            raise exception from None

        return user

    @classmethod
    def create_token(cls, base_user: models.BaseUser) -> models.Token:
        now = datetime.utcnow()
        payload = {
            'iat': now,
            'nbf': now,
            'exp': now + timedelta(seconds=settings.jwt_expiration),
            'sub': str(base_user.login),
            'user': base_user.dict()
        }

        token = jwt.encode(
            payload,
            settings.jwt_secret,
            algorithm=settings.jwt_algorithm
        )

        return models.Token(access_token=token)

    async def register_new_user(self, user_data: models.RegisterUser) -> models.Token:      
        user_data.password_hash = self.hash_password(user_data.password)
        await users_collection.insert_one(user_data.dict())
        return self.create_token(user_data)

    def validate_sms(self, login: str, user_code: int, phone: str):
        cache = redis_db.hmget(login, {'phone': phone, 'code': user_code})
        if not cache[0]:
            return False
        if int(cache[1]) == user_code:
            return True
        else:
            return False

    async def update_user(self, user_data: models.User, update_data: dict):
        #print(update_data.__dict__)
        print(user_data)
        updating = {}
        for k, v in update_data.__dict__.items():
            if v:
                updating[k] = v
        await users_collection.update_one({'login': user_data.login}, {'$set': updating})
        return 200

    async def authenticate_user(self, login: str, password: str) -> models.Token:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'},
        )

        user = await users_collection.find_one({'login': login})
        print(user)
        if not user:
            raise exception

        if not self.verify_password(password, user['password_hash']):
            raise exception

        return self.create_token(models.BaseUser.parse_obj(user))

    async def add_course(self, teacher, course_data):
        weekdays = course_data.lessons_weekdays
        schedule = generate_lessons_schedule(weekdays, course_data.course_length, course_data.course_start)
        course_data.teacher_id = teacher.id
        course_data.id = str(uuid.uuid4())
        course_data.lessons_days = schedule
        await courses_collection.insert_one(course_data.dict())
        return course_data


    async def get_courses(self, user):
        courses = []
        async for course in courses_collection.find({'teacher_id': user.id}):
            courses.append(course)
        print(courses)
        return courses
