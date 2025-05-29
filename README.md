# Forsit - E-commerce Admin API Backend

Backend REST APIs are designed using **FastAPI** and **MySQL** for e-commerce admin functionalities.

---

## Directory Structure

```bash
forsit-ecomm-api/
├── app/
│   ├── api/
│   ├── core/
│   ├── repositories/    
│   ├── services/    
│   ├── db/               # Database session and base
│   ├── models/           # SQLAlchemy models
│   ├── schemas/          # Pydantic models
│   └── main.py
├── scripts/
├── requirements.txt
└── README.md
```

## Features

* Built for **Forsit's ecommerce dashboard**.
* Supports **sales analytics**, **inventory control**, and **product registration**.
* Uses **SQLAlchemy ORM** and **MySQL**.


## Core Features

### 1. Product Registration

* `POST /products/`: Add new product
* `GET /products/`: List all products

### 2. Inventory Management

* `GET /inventory/`: View current inventory
* `PUT /inventory/update`: Update inventory stock
* `GET /inventory/low-stock`: Alerts for low stock

### 3. Sales Analytics

* `GET /sales/`:	View all sales
* `GET /sales/revenue/daily`:	Revenue per day
* `GET /sales/revenue/weekly`:	Revenue per week (and year)
* `GET /sales/revenue/monthly`:	Revenue per month
* `GET /sales/revenue/annual`:	Revenue per year
* `GET /sales/revenue/by-category`:	Revenue by category (optionally by date range)
* `GET /sales/revenue/compare`:	Revenue comparison between two periods (and category)


## Requirements

```
fastapi
uvicorn
sqlalchemy
pymysql
python-dotenv
faker
```

## Setup Instructions (Windows)

1. Start Database (Docker or local MySQL). You can also use sqlite if mysql is not installed by setting DATABASE_URL like this `"sqlite:///./forsit_ecom.db"`

2. Install requirements:

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

3. Run FastAPI: `uvicorn app.main:app --reload`

4. Seed Data:

```
set PYTHONPATH=.

python app/scripts/forsit_data.py
```

API: [http://localhost:8000/docs](http://localhost:8000/docs)





