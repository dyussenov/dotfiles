from typing import Optional
from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session

import tables
from database import get_session


class TextService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_all_text(self):
        all_text = (
            self.session
            .query(tables.TextField)
            .all()
        )
        response = {
            'ru': {},
            'kz': {}
        }
        for text_field in all_text:
            response['ru'][text_field.field_name] = text_field.field_value_ru
            response['kz'][text_field.field_name] = text_field.field_value_kz
        return response

    def get_all_text_for_admin(self):
        all_text = (
            self.session
            .query(tables.TextField)
            .all()
        )
        return all_text

    def update_text_field(self, field_id: int, field_data) -> tables.TextField:
        text_field = self._get(field_id)
        for field, value in field_data:
            print(field, value)
            setattr(text_field, field, value)
        self.session.commit()
        return text_field

    def get_text_field(self, text_field_id: int) -> tables.TextField:
        text_field = self._get(text_field_id)
        return text_field

    def delete_text_field(self, text_field_id: int):
        text_field = self._get(text_field_id)
        self.session.delete(text_field)
        self.session.commit()

    def create_text_field(self, text_field_data) -> tables.TextField:
        text_field = tables.TextField(**text_field_data.dict())
        self.session.add(text_field)
        self.session.commit()
        return text_field

    def _get(self, text_field_id: int) -> Optional[tables.TextField]:
        text_field = (
            self.session
            .query(tables.TextField)
            .filter(
                tables.TextField.id == text_field_id,
            )
            .first()
        )
        if not text_field:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return text_field
