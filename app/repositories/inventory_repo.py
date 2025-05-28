from sqlalchemy.orm import Session
from app.models.models import Inventory, InventoryHistory
from datetime import datetime

class InventoryRepository:
    @staticmethod
    def get_all(db: Session):
        return db.query(Inventory).all()

    @staticmethod
    def update_inventory(db: Session, product_id: int, change: int, updated_by: str):
        inv_entry = db.query(Inventory).filter(Inventory.product_id == product_id).first()
        if not inv_entry:
            return None
        inv_entry.stock_level += change
        inv_entry.last_updated = datetime.utcnow()
        history = InventoryHistory(
            product_id=product_id, change=change, updated_by=updated_by
        )
        db.add(history)
        db.commit()
        return inv_entry

    @staticmethod
    def get_low_stock(db: Session, threshold: int = 10):
        return db.query(Inventory).filter(Inventory.stock_level < threshold).all()
