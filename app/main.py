from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from random import randint

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from redis import asyncio as aioredis

from app.api import router as api_router
from app.pages.router import router as pages_router
from app.images.router import router as images_router


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    redis = aioredis.from_url("redis://localhost:6379")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield


app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="app/static"), "static")

app.include_router(router=api_router)
app.include_router(router=pages_router)
app.include_router(router=images_router)


@app.get("/")
@cache(expire=60)
async def get_home_page():
    return {"message": f"hello, {randint(1, 100)}"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
