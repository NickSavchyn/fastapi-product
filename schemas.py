from datetime import datetime

from pydantic import BaseModel, Field

from db.models import Category


class ProductBase(BaseModel):
    name: str
    description: str = None
    price: float
    created_at: datetime
    quantity: int = Field(..., gt=0)
    category: Category


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: str = None
    description: str = None
    price: float = None
    quantity: int
    category: Category


class ProductDelete(BaseModel):
    id: int


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
