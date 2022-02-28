from app.api.routes.blogs import router as blog_routes

from fastapi import APIRouter

router = APIRouter()

router.include_router(blog_routes, prefix="/blog", tags=["cleanings"])
