from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.product_service import ProductService
from app.schemas import schemas

router = APIRouter()

@router.post("/", response_model=schemas.ProductOut)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return ProductService.create_product(db, product)

@router.get("/", response_model=list[schemas.ProductOut])
def list_all_products(db: Session = Depends(get_db)):
    return ProductService.list_products(db)
