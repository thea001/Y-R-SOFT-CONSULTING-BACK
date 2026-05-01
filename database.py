import os
from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

# These should come from the "Connection Pooler" section in Supabase
USER = os.getenv("user", "postgres.vsetfohjtcpsdibiiauj") # Pooler often requires the project ref
PASSWORD = os.getenv("password", "#q+%wY&_2@LWWpF")
HOST = os.getenv("host", "aws-0-eu-central-1.pooler.supabase.com") # Example pooler host
PORT = os.getenv("port", "6543") # Port 6543 for Pooler
DBNAME = os.getenv("dbname", "postgres")

# 1. URL Encode the password to handle special characters (@, #, %)
encoded_password = quote_plus(PASSWORD)

# 2. Construct the URL using the postgresql+psycopg2 dialect
DATABASE_URL = f"postgresql+psycopg2://{USER}:{encoded_password}@{HOST}:{PORT}/{DBNAME}"

# 3. Create the engine with SSL and Pooler-specific arguments
engine = create_engine(
    DATABASE_URL, 
    echo=True, 
    connect_args={
        "sslmode": "require",
    }
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()