from sqlalchemy import Column, Integer, String, Text, Boolean, TIMESTAMP
from database import Base
from sqlalchemy.sql import func

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    lead_type = Column(String(50))
    name = Column(String(255))
    email = Column(String(255))
    country_code = Column(String(10))
    phone = Column(String(50))
    company = Column(String(255))
    service = Column(String(255))
    message = Column(Text)
    contact_method = Column(String(50))
    discovery_call = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    is_admin = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, server_default=func.now())