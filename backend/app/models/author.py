from pydantic import BaseModel
from ..models.blog import BlogModel
from typing import List

class AuthorModel(BaseModel):
    id:int
    name:str
    email:str
    blogs:List[BlogModel] = []

    class Config:
        orm_mode = True


class AuthorUpdate(BaseModel):
    title:str
    description:str

    class Config:
        orm_mode=True


# class AuthorInDBModel(BaseModel):
#     id:int
#     name:str
#     email:str
#     blogs:List[BlogModel] = []

#     class Conig:
#         orm_mode = True