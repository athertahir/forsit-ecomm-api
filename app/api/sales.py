from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.sales_service import SalesService
from app.schemas import schemas
from typing import Optional
from datetime import date

router = APIRouter()

@router.get("/", response_model=list[schemas.SaleOut])
def list_sales(db: Session = Depends(get_db)):
    return SalesService.get_sales(db)

@router.get("/revenue/daily")
def daily_revenue(db: Session = Depends(get_db)):
    return SalesService.get_daily_revenue(db)

@router.get("/revenue/weekly")
def weekly_revenue(db: Session = Depends(get_db)):
    return SalesService.get_weekly_revenue(db)

@router.get("/revenue/monthly")
def monthly_revenue(db: Session = Depends(get_db)):
    return SalesService.get_monthly_revenue(db)

@router.get("/revenue/annual")
def annual_revenue(db: Session = Depends(get_db)):
    return SalesService.get_annual_revenue(db)

@router.get("/revenue/by-category")
def revenue_by_category(
    db: Session = Depends(get_db),
    start_date: Optional[date] = Query(None),
    end_date: Optional[date] = Query(None),
):
    return SalesService.get_revenue_by_category(db, start_date, end_date)

@router.get("/revenue/compare")
def revenue_compare(
    db: Session = Depends(get_db),
    period1_start: date = Query(..., description="Start date for first period"),
    period1_end: date = Query(..., description="End date for first period"),
    period2_start: date = Query(..., description="Start date for second period"),
    period2_end: date = Query(..., description="End date for second period"),
    category: Optional[str] = Query(None, description="Product category to filter")
):
    return SalesService.get_revenue_comparison(
        db, period1_start, period1_end, period2_start, period2_end, category
    )
