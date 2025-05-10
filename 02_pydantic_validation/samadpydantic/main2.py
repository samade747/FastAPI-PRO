from pydantic import BaseModel, EmailStr

# Define a nested model
class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class UserWithAddress(BaseModel):
    id: int
    name: str
    age: int | None = None  # Optional field
    email: EmailStr # Built-in validator for email format
    address: list[Address]  # List of nested Address models

# Valid data with nested structure
user_data = {
    "id": 1,
    "name": "Samad",
    "age": 25,
    "email": "gIu3o@example.com",
    "address": [
        {"street": "123 Main St", "city": "New York", "zip_code": "10001"},
        {"street": "456 Elm St", "city": "Los Angeles", "zip_code": "90001"},
    ],
}

user = UserWithAddress.model_validate(user_data)
print(user.model_dump())