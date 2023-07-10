from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
import schemas
import crud
from db.engine import get_async_session

router = APIRouter()


@router.get("/products/", response_model=list[schemas.Product])
async def read_products(
    page: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1, le=100),
    db: AsyncSession = Depends(get_async_session)
):
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    products = await crud.get_all_products(db)
    paginated_products = products[start_index:end_index]
    return paginated_products


@router.get("/products/{id}", response_model=schemas.Product)
async def get_product(id: int, db: AsyncSession = Depends(get_async_session)):
    return await crud.get_product(id, db)


@router.post("/product/", response_model=schemas.Product)
async def create_product(product: schemas.ProductBase, db: AsyncSession = Depends(get_async_session)):
    return await crud.create_product(product, db)


@router.patch("/products/{id}", response_model=schemas.Product)
async def patch_product(id: int, product: schemas.ProductUpdate, db: AsyncSession = Depends(get_async_session)):
    return await crud.update_product(id, product, db)


@router.delete("/products/{id}")
async def delete_product(id: int, db: AsyncSession = Depends(get_async_session)):
    return await crud.delete_product(id, db)
