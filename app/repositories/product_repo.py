from sqlalchemy.orm import Session
from app.models.models import Product, Inventory

class ProductRepository:
    @staticmethod
    def create(db: Session, data: dict):
        product = Product(**data)
        db.add(product)
        db.commit()
        db.refresh(product)
        # Initialize inventory for product
        db_inventory = Inventory(product_id=product.id, stock_level=0)
        db.add(db_inventory)
        db.commit()
        return product

    @staticmethod
    def list_all(db: Session):
        return db.query(Product).all()
