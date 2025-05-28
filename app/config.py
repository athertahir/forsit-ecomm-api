import os

class Config():
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "sqlite:///./forsit_ecom.db"
        # "mysql+pymysql://root:forsitpwd@db/forsit_forsit_ecom_db"
    )

config = Config()