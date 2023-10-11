from pydantic import BaseModel
from typing import Optional


class BookModel(BaseModel):
    title: str
    author: str
    publication_year: int

class BookQueryModel(BaseModel):
    id: str
    title:str
    author:str
    publication_year: int
    
class BookModelResponse(BaseModel):
    id: str
    title:str
    author:str
    publication_year: int

class ResponseBody(BaseModel):
    status:int
    message:Optional[str]
    data:Optional[list]
    error: Optional[str]

class ResponseSuccessOne(BaseModel):
    status:int
    message:str
    data:dict

class ResponseSuccessMany(BaseModel):
    status:int
    message:str
    data: list

class ResponseError(BaseModel):
    status:int
    error: Optional[str]
    