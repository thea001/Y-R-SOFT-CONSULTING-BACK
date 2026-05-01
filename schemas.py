from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class LeadBase(BaseModel):
    leadType: str = Field(..., alias="lead_type")
    name: str
    email: str
    countryCode: str = Field(..., alias="country_code")
    phone: str
    company: Optional[str] = None
    service: str
    message: Optional[str] = None
    contactMethod: str = Field(..., alias="contact_method")
    discoveryCall: bool = Field(..., alias="discovery_call")

    class Config:
        populate_by_name = True
        from_attributes = True


class LeadCreate(BaseModel):
    leadType: str
    name: str
    email: str
    countryCode: str
    phone: str
    company: Optional[str] = None
    service: str
    message: Optional[str] = None
    contactMethod: str
    discoveryCall: bool


class LeadResponse(LeadBase):
    id: int


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"