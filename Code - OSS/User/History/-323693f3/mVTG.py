from fastapi import APIRouter, HTTPException
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
    res = FileResponse(file_path)
    print(res.__dict__)
    return 200


