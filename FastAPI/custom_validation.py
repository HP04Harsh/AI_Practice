from pydantic import BaseModel, field_validator

class UserRegistration(BaseModel):
    username: str
    age: int

    # Custom validation to check if age is 18 or above
    @field_validator('age')
    def validate_age(cls, value):
        if value < 18:
            raise ValueError('Age must be at least 18 years old.')
        return value
s
# Test karein:
# valid_user = UserRegistration(username="Rahul", age=22) -> Pass ho jayega
# invalid_user = UserRegistration(username="Aman", age=16) -> ValueError dega!