from pydantic import BaseModel
from datetime import datetime

class ProductBase(BaseModel):
    name: str
    category: str
    price: float
    sku: str
    description: str

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int
    class Config:
        orm_mode = True

class SaleOut(BaseModel):
    id: int
    product_id: int
    quantity: int
    total_price: float
    sale_date: datetime
    class Config:
        orm_mode = True

class InventoryOut(BaseModel):
    product_id: int
    stock_level: int
    last_updated: datetime
    class Config:
        orm_mode = True

class InventoryUpdate(BaseModel):
    product_id: int
    change: int
    updated_by: str
