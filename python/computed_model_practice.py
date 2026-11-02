from pydantic import BaseModel, field_validator, model_validator, computed_field

class NegativeValueError(ValueError):
    pass

class Area(BaseModel):
    length: int
    width: int

    @model_validator(mode='after')
    def validator(self):
        if self.length <= 0 or self.width <= 0:
            raise NegativeValueError("Length and width must be positive numbers.")
        return self

    @computed_field
    @property
    def area_calculation(self) -> float:
        return self.length * self.width

a = Area(length=1, width=10)
print(f"Length: {a.length}, Width: {a.width}, Area: {a.area_calculation}")            