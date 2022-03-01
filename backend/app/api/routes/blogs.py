from fastapi import APIRouter, Depends, Body, HTTPException
from sqlalchemy.orm import Session
from app.db.schema import Blog, Author
from app.models.blog import BlogModel, BlogUpdateModel
from starlette.requests import Request
from typing import List
router = APIRouter()

def get_db(request:Request):
    db = request.app.state._SessionLocal()
    try:
        yield db
    except Exception as e:
        print(f"closed with error {e}")
        db.close()




@router.get("/all", response_model=List[BlogModel])
def get_all_blogs(db:Session = Depends(get_db)):
    return db.query(Blog).all()


@router.get("/{id}", response_model=BlogModel)
def get_blogs_by_id(id:int, db:Session = Depends(get_db)):
    required_blog = db.query(Blog).filter(Blog.id == id).first()
    if required_blog is None:
        raise HTTPException(status_code=404, detail=f"Blog with id ${id} is not found")

    return required_blog


@router.post("/new", response_model=BlogModel)
def add_new_blog_by_id(new_blog:BlogModel, db:Session = Depends(get_db)):
    refered_author = db.query(Author).filter(Author.id == new_blog.author_id).first()
    if(refered_author == None):
        return HTTPException(status_code=404, detail=f"Author with author id {new_blog.id} not found")
    db.add(Blog(**new_blog.dict(), author=refered_author))
    db.commit()
    return new_blog
    

@router.delete("/{id}")
def delete_blog_by_id(id:int, db:Session = Depends(get_db)):    
    blog_deleted = db.query(Blog).filter(Blog.id == id)
    deleted_blog = blog_deleted.first()
    if(blog_deleted.first() is None):
        raise HTTPException(status_code = 404, detail = f"The blog with id {id} not found")
    blog_deleted.delete()
    db.commit()
    return deleted_blog


@router.put("/{id}", response_model=BlogModel)
def update_blog_by_id(id:int, blog:BlogUpdateModel, db:Session = Depends(get_db)):
    updated_blog = db.query(Blog).filter(Blog.id == id)
    if(updated_blog.first() is None):
        raise HTTPException(status_code=404, detail=f"The blog with id {id} not found")
    updated_blog.update({Blog.title:blog.title, Blog.description:blog.description})
    return updated_blog.first()

