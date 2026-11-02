from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class User(BaseModel):
    name: str
    email: str
    address: Address

user_data = User(
    name="John Doe",
    email="john.doe@example.com",
    address=Address(
        street="123 Main St",
        city="Anytown",
        state="CA",
        zip_code="12345"
    )
)

print(user_data.address.state)  # Output: CA