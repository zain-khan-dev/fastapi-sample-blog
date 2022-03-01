from fastapi import APIRouter, Depends
from starlette.requests import Request
from sqlalchemy.orm import Session
from app.db.schema import Author
from app.models.author import  AuthorModel
from typing import List

router = APIRouter()

def get_db(request:Request):
    db = request.app.state._SessionLocal()
    try:
        yield db
    except Exception as e:
        print(f"closed with error {e}")
        db.close()


@router.get("/author", response_model=List[AuthorModel])
def get_all_users(db:Session = Depends(get_db)):
    return db.query(Author).all()


@router.post("/author", response_model=AuthorModel)
def add_new_user(new_author:AuthorModel, db:Session = Depends(get_db)):
    db.add(Author(**new_author.dict()))
    db.commit()
    return new_author


@router.get("/{id}", response_model=AuthorModel)
def get_all_blogs(id:int, db:Session = Depends(get_db)):
    return db.query(Author).filter(Author.id == id).first()
    