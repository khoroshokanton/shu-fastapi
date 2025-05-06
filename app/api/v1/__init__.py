from fastapi import APIRouter

from .booking import router as booking_router
from .auth import router as auth_router
from .users import router as user_router

router = APIRouter(prefix="/v1")
router.include_router(booking_router)
router.include_router(auth_router)
router.include_router(user_router)
