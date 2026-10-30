from fastapi import APIRouter

from app.auth.router import router as auth_router
from app.burgers.router import router as burgers_router
from app.core.config import settings
from app.items.router import router as items_router
from app.private.router import router as private_router
from app.system.router import router as system_router
from app.users.router import router as users_router

api_router = APIRouter()
api_router.include_router(auth_router)
api_router.include_router(users_router)
api_router.include_router(items_router)
api_router.include_router(burgers_router)
api_router.include_router(system_router)

if settings.FASTAPI_ENV == "development":
    api_router.include_router(private_router)
