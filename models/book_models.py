from pydantic import BaseModel
from typing import Optional

class BookCreate(BaseModel):
    title: str
    author: str
    year: int
    pages: Optional[int]
#iporta todos los datos del BookCreate
class Book(BookCreate):
    id: str

