from pydantic import BaseModel, Field
from pydantic.networks import EmailStr, PhoneNumber

class UserDetail(BaseModel):
    username: str
    email: EmailStr
    phone: PhoneNumber

user = UserDetail(username="john_doe", email="harsh@email.com", phone="39393")
print(user)
