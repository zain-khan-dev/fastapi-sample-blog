import string
from pydantic import BaseModel

class BlogModel(BaseModel):
    id:int
    title:str
    description:str

    class Config:
        orm_mode = True


class BlogUpdate(BaseModel):
    title:str
    description:str

    class Config:
        orm_mode=True