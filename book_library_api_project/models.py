from pydantic import BaseModel
from typing import Optional
from enums import Genre, Status

class Book(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
    genre: Genre
    status: Status = Status.AVAILABLE
    rating: Optional[int] = None

    

