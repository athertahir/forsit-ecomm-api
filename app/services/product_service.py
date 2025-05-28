from sqlalchemy.orm import Session
from app.schemas.schemas import ProductCreate
from app.repositories.product_repo import ProductRepository

class ProductService:
    @staticmethod
    def create_product(db: Session, product: ProductCreate):
        return ProductRepository.create(db, product.dict())

    @staticmethod
    def list_products(db: Session):
        return ProductRepository.list_all(db)
