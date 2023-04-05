from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Response

import models
import services

router = APIRouter(
    prefix='/text',
    tags=['text'],
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
    '/{field_id}',
    response_model=models.TextFieldBase,
)
def get_text_field(
        text_field_id: int,
        text_service: services.TextService = Depends()
):
    return text_service.get_text_field(text_field_id)


@router.put('/{field_id}')
def update_text_field(
        field_id: int,
        text_field: models.TextFieldBase,
        text_service: services.TextService = Depends(),
):
    return text_service.update_text_field(field_id, text_field)


@router.delete(
    '/{field_id}',
    status_code=status.HTTP_204_NO_CONTENT,

)
def delete_text_field(
        field_id: int,
        text_service: services.TextService = Depends(),
):
    text_service.delete_text_field(field_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
