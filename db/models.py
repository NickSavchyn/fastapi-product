from enum import StrEnum, auto

from sqlalchemy import Column, Integer, String, Numeric, DateTime, func, Enum
from db.engine import Base


class Category(StrEnum):
    computer = auto()
    smartphone = auto()
    tablet = auto()
    other = auto()


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(511))
    price = Column(Numeric(precision=10, scale=2), nullable=False)
    created_at = Column(DateTime, default=func.now())
    quantity = Column(Integer, default=0)
    category = Column(Enum(Category), nullable=False)
