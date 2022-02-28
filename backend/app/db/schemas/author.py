from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True)
    name=Column(String)
    email = Column(String)





class Blog(Base):
    __tablename__ = "blog"

    id = Column(Integer, primary_key=True)
    title=Column(String)
    description = Column(String)
    author_id = Column('author', Integer, ForeignKey("author.id")) 
    author = relationship("Author", back_populates="blog")
