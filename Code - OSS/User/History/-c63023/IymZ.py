from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Response

#import models

router = APIRouter(
    prefix='/sms',
    tags=['sms'],
)


@router.get(
    '/',
    #не забудь пофиксить
    #response_model=list[models.TextFieldBase],
)
def get_all_text(
    text_service: services.TextService = Depends()
):
    return text_service.get_all_text()

@router.post(
    '/',
    response_model=models.TextFieldBase
)
def add_text_field(
        text_field: models.TextFieldBase,
        text_service: services.TextService = Depends()
):
    return text_service.create_text_field(text_field)


@router.get(
    '/{id}',
    response_model=models.TextFieldBase,
)
def get_text_field(
        id: int,
        text_service: services.TextService = Depends()
):
    return text_service.get_text_field(id)


@router.put('/{id}')
def update_text_field(
        id: int,
        text_field: models.TextFieldBase,
        text_service: services.TextService = Depends(),
):
    return text_service.update_text_field(id, text_field)


@router.delete(
    '/{id}',
    status_code=status.HTTP_204_NO_CONTENT,

)
def delete_text_field(
        id: int,
        text_service: services.TextService = Depends(),
):
    text_service.delete_text_field(id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
