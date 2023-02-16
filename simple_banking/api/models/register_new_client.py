"""Model definitions."""
import datetime

from pydantic import BaseModel, EmailStr


class RegisterNewClientRequest(BaseModel):
    """Request for the register new client usecase."""

    email: EmailStr
    name: str
    last_name: str
    password: str
    birthday_date: datetime.date
