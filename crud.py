from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
import schemas
from db import models


async def get_all_products(db: AsyncSession):
    db_products = await db.execute(models.Product.select())
    return db_products.scalars().all()


async def get_product(id: int, db: AsyncSession):
    db_product = await db.execute(models.Product.select().where(models.Product.id == id))
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product.scalar_one()


async def create_product(product: schemas.ProductBase, db: AsyncSession):
    db_product = models.Product(
        name=product.name,
        description=product.description,
        price=product.price,
        created_at=datetime.now(),
        quantity=product.quantity,
        category=product.category
    )
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product


async def update_product(id: int, product: schemas.ProductUpdate, db: AsyncSession):
    db_product = await db.execute(models.Product.select().where(models.Product.id == id))
    if db_product.scalar() is None:
        raise HTTPException(status_code=404, detail="Product not found")

    product_data = product.dict(exclude_unset=True)
    for field, value in product_data.items():
        setattr(db_product.scalar(), field, value)

    await db.commit()
    await db.refresh(db_product.scalar())
    return db_product.scalar()


async def delete_product(id: int, db: AsyncSession):
    db_product = await db.execute(models.Product.select().where(models.Product.id == id))
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    await db.delete(db_product)
    await db.commit()
    return {"message": "Product deleted successfully"}
