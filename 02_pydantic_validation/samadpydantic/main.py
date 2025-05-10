from pydantic import BaseModel, ValidationError

# Define a simple model
class User(BaseModel):
    id: int
    name: str
    age: int
    email: str
    age: int | None = None  # Optional field



# Valid data we giving user data or data in database
user_data = {
    "id": 1,
    "name": "Samad",
    "age": 25,
    "email": "gIu3o@example.com",
}


user = User(**user_data)

print(user)  # 

print(user.model_dump())  

# Invalid data (will raise an error)
try:
    invalid_user = User(id="not_an_int", name="Bob", email="bob@example.com")
except ValidationError as e:
    print(e)