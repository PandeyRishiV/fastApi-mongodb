from enum import Enum
from typing import List, Optional
from pydantic import BaseModel


class Gender(Enum):
    male = "Male"
    female = "Female"

class Role(Enum):
    admin = "Admin"
    user = "User"
    student = "Student"
    teacher = "Teacher"

class User(BaseModel):
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    gender: Gender
    email_address: str
    phone_number: str
    roles: List[str]