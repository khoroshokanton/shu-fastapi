import shutil

from fastapi import APIRouter
from fastapi import UploadFile

router = APIRouter(prefix="/images", tags=["Загрузка картинок"])


@router.post("/hotels")
async def add_hotel_image(name: int, file: UploadFile):
    with open(f"app/static/images/{name}.webp", "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
