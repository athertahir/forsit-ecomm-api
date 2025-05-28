from sqlalchemy.orm import Session
from typing import Optional
from datetime import date
from app.repositories.sales_repo import SalesRepository

class SalesService:
    @staticmethod
    def get_sales(db: Session):
        return SalesRepository.get_all(db)

    @staticmethod
    def get_daily_revenue(db: Session):
        rows = SalesRepository.get_revenue_by_day(db)
        return [{"day": row.day, "revenue": float(row.revenue or 0)} for row in rows]

    @staticmethod
    def get_weekly_revenue(db: Session):
        rows = SalesRepository.get_revenue_by_week(db)
        return [{"year": row.year, "week": row.week, "revenue": float(row.revenue or 0)} for row in rows]

    @staticmethod
    def get_monthly_revenue(db: Session):
        rows = SalesRepository.get_revenue_by_month(db)
        return [{"month": row.month, "revenue": float(row.revenue or 0)} for row in rows]

    @staticmethod
    def get_annual_revenue(db: Session):
        rows = SalesRepository.get_revenue_by_year(db)
        return [{"year": row.year, "revenue": float(row.revenue or 0)} for row in rows]

    @staticmethod
    def get_revenue_by_category(db: Session, start_date: Optional[date] = None, end_date: Optional[date] = None):
        rows = SalesRepository.get_revenue_by_category(db, start_date, end_date)
        return [{"category": row.category, "revenue": float(row.revenue or 0)} for row in rows]

    @staticmethod
    def get_revenue_comparison(
        db: Session,
        period1_start: date,
        period1_end: date,
        period2_start: date,
        period2_end: date,
        category: Optional[str] = None,
    ):
        return SalesRepository.get_revenue_comparison(
            db, period1_start, period1_end, period2_start, period2_end, category
        )
