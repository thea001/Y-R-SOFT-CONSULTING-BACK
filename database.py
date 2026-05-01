from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    db_user = os.getenv("DB_USER", "postgres")
    db_password = os.getenv("DB_PASSWORD", "#q+%wY&_2@LWWpF")
    db_host = os.getenv("DB_HOST", "db.vsetfohjtcpsdibiiauj.supabase.co")
    db_port = os.getenv("DB_PORT", "5432")
    db_name = os.getenv("DB_NAME", "postgres")
    encoded_password = quote_plus(db_password)
    DATABASE_URL = f"postgresql://{db_user}:{encoded_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(DATABASE_URL, echo=True, connect_args={"sslmode": "require"})

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()