from app.db.session import SessionLocal
from app.models import models
from faker import Faker
import random

fake = Faker()
db = SessionLocal()

categories = ["Electronics", "Home", "Books"]

for _ in range(10):
    product = models.Product(
        name=fake.word(),
        category=random.choice(categories),
        price=round(random.uniform(10.0, 500.0), 2),
        sku=fake.uuid4(),
        description=fake.sentence()
    )
    db.add(product)
    db.commit()
    db.refresh(product)

    db_inventory = models.Inventory(product_id=product.id, stock_level=random.randint(5, 100))
    db.add(db_inventory)
    db.commit()

    for _ in range(20):
        db_sale = models.Sale(
            product_id=product.id,
            quantity=random.randint(1, 5),
            total_price=round(product.price * random.randint(1, 5), 2),
            sale_date=fake.date_time_this_year()
        )
        db.add(db_sale)
        db.commit()

db.close()