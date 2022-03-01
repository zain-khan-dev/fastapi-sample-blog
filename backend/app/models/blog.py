from pydantic import BaseModel


class BlogBaseModel(BaseModel):
    title:str
    description:str

    class Config:
        orm_mode=True


class BlogModel(BlogBaseModel):
    id:str
    author_id:int

    class Config:
        orm_mode = True


class BlogUpdateModel(BlogBaseModel):
    pass

class BlogInsertModel(BlogBaseModel):
    pass