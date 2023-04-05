from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os
router = APIRouter(
    prefix='/file',
    tags=['file'],
)

@router.get(
    '/{filename}'
)
def get_file(filename):
    file_path = f'static/{filename}.pdf'
    print(os.listdir('/static'))
    #return FileResponse(file_path)


