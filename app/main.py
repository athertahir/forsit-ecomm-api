from fastapi import FastAPI
from app.api import products, inventory, sales
from app.db.base import Base
from app.db.session import engine
API_PREFIX = "/api/v1"

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Forsit - E-commerce Admin API")

app.include_router(products.router, prefix=f"{API_PREFIX}/products", tags=["Products"])
app.include_router(inventory.router, prefix=f"{API_PREFIX}/inventory", tags=["Inventory"])
app.include_router(sales.router, prefix=f"{API_PREFIX}/sales", tags=["Sales"])
