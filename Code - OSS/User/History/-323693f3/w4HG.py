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
    try:
        return FileResponse(file_path)
    except:
        raise HTTPException(404, 'file not found')

