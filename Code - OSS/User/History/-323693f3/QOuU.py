from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter(
    prefix='/file',
    tags=['file'],
)

@router.get(
    '/{filename}'
)
def get_file(filename):
    file_path = f'static/{filename}.pdf'
    return FileResponse(file_path)


