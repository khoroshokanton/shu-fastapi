from datetime import date

import uvicorn
from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field


app = FastAPI()


@app.get("/")
async def get_home_page():
    return {"message": "hello"}


class GetHotelsQueryParams(BaseModel):
    locations: str | None = None
    date_from: date | None = date.today()
    date_to: date | None = None
    has_spa: bool | None = None
    stars: int | None = Field(None, ge=1, le=5)


class HotelReadSchema(BaseModel):
    address: str
    name: str
    stars: int


@app.get("/hotels")
async def get_hotels(
    query_params: GetHotelsQueryParams = Depends(),
) -> list[HotelReadSchema]:
    print(query_params)


@app.get("/hotels/{hotel_id}")
async def get_hotel(hotel_id: int):
    return None


class BookingSchema(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/booking")
async def add_booking(booking: BookingSchema):
    pass


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
