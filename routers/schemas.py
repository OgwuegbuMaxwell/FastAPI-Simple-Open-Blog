from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime


class PostBase(BaseModel):
    image_url: str
    title: str
    content: str 
    creator: str
    
class PostDisplay(BaseModel):
    id: str
    image_url: str
    title: str
    content: str 
    creator: str
    timestamps: datetime
    
    class ConfigDict:
        from_attributes = True
