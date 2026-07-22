from fastapi import APIRouter

from app.api.v1.endpoints.hello_axione import router as hello_router


api_router = APIRouter()
api_router.include_router(hello_router, tags=["hello"])
