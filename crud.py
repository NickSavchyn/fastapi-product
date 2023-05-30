from datetime import datetime
from sqlalchemy.orm import Session
from fastapi import HTTPException
import schemas
from db import models


def get_all_products(db: Session):
    db_products = db.query(models.Product).all()
    return db_products


def get_product(id: str, db: Session):
    db_product = db.query(models.Product).filter(models.Product.id == id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


def create_product(product: schemas.ProductCreate, db: Session):
    db_product = models.Product(
        name=product.name,
        description=product.description,
        price=product.price,
        created_at=datetime.now(),
        quantity=product.quantity,
        category=product.category
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(id: str, product: schemas.ProductUpdate, db: Session):
    db_product = db.query(models.Product).filter(models.Product.id == id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    for field, value in product.dict(exclude_unset=True).items():
        setattr(db_product, field, value)
    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(id: str, db: Session):
    db_product = db.query(models.Product).filter(models.Product.id == id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)
    db.commit()
    return {"message": "Product deleted successfully"}
