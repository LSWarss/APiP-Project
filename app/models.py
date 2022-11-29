from sqlalchemy import Column, Integer, String
from app.database import base
from pydantic import BaseModel


class Images(base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)


class Image(BaseModel):
    url: str
