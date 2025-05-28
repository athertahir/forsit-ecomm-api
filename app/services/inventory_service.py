from sqlalchemy.orm import Session
from app.repositories.inventory_repo import InventoryRepository
from app.schemas.schemas import InventoryUpdate

class InventoryService:
    @staticmethod
    def get_inventory(db: Session):
        return InventoryRepository.get_all(db)

    @staticmethod
    def update_inventory(db: Session, update: InventoryUpdate):
        return InventoryRepository.update_inventory(db, update.product_id, update.change, update.updated_by)

    @staticmethod
    def low_stock_alerts(db: Session):
        return InventoryRepository.get_low_stock(db)
