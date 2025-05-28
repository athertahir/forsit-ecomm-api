from sqlalchemy.orm import Session
from app.models.models import Sale, Product
from sqlalchemy import func, and_
from typing import Optional
from datetime import date

class SalesRepository:
    @staticmethod
    def get_all(db: Session):
        return db.query(Sale).all()

    @staticmethod
    def get_revenue_by_day(db: Session):
        # Format: "2024-05-30" format
        return (
            db.query(
                func.strftime("%Y-%m-%d", Sale.sale_date).label("day"),
                func.sum(Sale.total_price).label("revenue")
            )
            .group_by(func.strftime("%Y-%m-%d", Sale.sale_date))
            .order_by(func.strftime("%Y-%m-%d", Sale.sale_date))
            .all()
        )

    @staticmethod
    def get_revenue_by_week(db: Session):
        return (
            db.query(
                func.strftime("%Y", Sale.sale_date).label("year"),
                func.strftime("%W", Sale.sale_date).label("week"),
                func.sum(Sale.total_price).label("revenue")
            )
            .group_by(func.strftime("%Y", Sale.sale_date), func.strftime("%W", Sale.sale_date))
            .order_by(func.strftime("%Y", Sale.sale_date), func.strftime("%W", Sale.sale_date))
            .all()
        )

    @staticmethod
    def get_revenue_by_month(db: Session):
        # Format: "2024-05"
        return (
            db.query(
                func.strftime("%Y-%m", Sale.sale_date).label("month"),
                func.sum(Sale.total_price).label("revenue")
            )
            .group_by(func.strftime("%Y-%m", Sale.sale_date))
            .order_by(func.strftime("%Y-%m", Sale.sale_date))
            .all()
        )

    @staticmethod
    def get_revenue_by_year(db: Session):
        return (
            db.query(
                func.strftime("%Y", Sale.sale_date).label("year"),
                func.sum(Sale.total_price).label("revenue")
            )
            .group_by(func.strftime("%Y", Sale.sale_date))
            .order_by(func.strftime("%Y", Sale.sale_date))
            .all()
        )

    @staticmethod
    def get_revenue_by_category(
        db: Session,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
    ):
        query = (
            db.query(
                Product.category.label("category"),
                func.sum(Sale.total_price).label("revenue")
            )
            .join(Product, Sale.product_id == Product.id)
        )
        if start_date:
            query = query.filter(Sale.sale_date >= start_date)
        if end_date:
            query = query.filter(Sale.sale_date <= end_date)
        return (
            query.group_by(Product.category)
            .order_by(Product.category)
            .all()
        )

    @staticmethod
    def get_revenue_by_period(
        db: Session,
        start_date: date,
        end_date: date,
        category: Optional[str] = None,
    ):
        query = db.query(func.sum(Sale.total_price).label("revenue"))
        if category:
            query = query.join(Product, Sale.product_id == Product.id).filter(Product.category == category)
        query = query.filter(
            and_(
                Sale.sale_date >= start_date,
                Sale.sale_date <= end_date
            )
        )
        return query.scalar() or 0

    @staticmethod
    def get_revenue_comparison(
        db: Session,
        period1_start: date,
        period1_end: date,
        period2_start: date,
        period2_end: date,
        category: Optional[str] = None,
    ):
        rev1 = SalesRepository.get_revenue_by_period(db, period1_start, period1_end, category)
        rev2 = SalesRepository.get_revenue_by_period(db, period2_start, period2_end, category)
        return {
            "period1": {"start": period1_start, "end": period1_end, "revenue": rev1},
            "period2": {"start": period2_start, "end": period2_end, "revenue": rev2},
            "difference": rev2 - rev1
        }
