from app.api.routes.blogs import router as blog_routes

from app.api.routes.author import router as author_routes

from fastapi import APIRouter

router = APIRouter()



router.include_router(blog_routes, prefix="/blog", tags=["blogs"])

router.include_router(author_routes, prefix="/author", tags=["author"])