from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from app.db.schemas.blog import Blog
from starlette.requests import Request
from app.models.blog import BlogModel, BlogUpdate
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
    return db.query(Blog).filter(Blog.id == id).first()

@router.post("/new", response_model=BlogModel)
def add_new_blog_by_id(new_blog:BlogModel, db:Session = Depends(get_db)):
    db.add(Blog(**new_blog.dict()))
    db.commit()
    return new_blog
    

@router.delete("/{id}")
def delete_blog_by_id(id:int, db:Session = Depends(get_db)):    
    db.query(Blog).filter(Blog.id == id).delete()
    db.commit()
    return {"status":"success"}


@router.put("/{id}", response_model=BlogUpdate)
def update_blog_by_id(id:int, blog:BlogUpdate, db:Session = Depends(get_db)):
    db.query(Blog).filter(Blog.id == id).update({**blog.dict()})
    db.commit()
    return blog

