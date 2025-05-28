from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.inventory_service import InventoryService
from app.schemas import schemas

router = APIRouter()

@router.get("/", response_model=list[schemas.InventoryOut])
def inventory_status(db: Session = Depends(get_db)):
    return InventoryService.get_inventory(db)

@router.put("/update", response_model=schemas.InventoryOut)
def update_inventory(inv: schemas.InventoryUpdate, db: Session = Depends(get_db)):
    return InventoryService.update_inventory(db, inv)

@router.get("/low-stock", response_model=list[schemas.InventoryOut])
def low_stock_alerts(db: Session = Depends(get_db)):
    return InventoryService.low_stock_alerts(db)
