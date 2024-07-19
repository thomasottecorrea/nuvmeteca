from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Book(BaseModel):
    id: str
    title: str
    author: str
    category: str
    is_available: bool = True
    borrower: Optional[str] = None
    loan_date: Optional[datetime] = None
    return_date: Optional[datetime] = None
    wait_list: List[str] = []

class BookCreate(BaseModel):
    title: str
    author: str
    category: str
