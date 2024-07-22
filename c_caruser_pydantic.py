from pydantic import BaseModel, field_validator

class CarUser(BaseModel):
    age: int
    gender: int

    @field_validator("age")
    @classmethod
    def check_valid_age(cls, age: int) -> int:
        if age < 18:
            raise ValueError("Age must be at least 18 years old.")

        return age
    
    @field_validator("gender")
    @classmethod
    def check_valid_gender(cls, gender: int) -> int:
        if gender > 2 or gender <1:
            raise ValueError("Gender must be 1  or 2.")

        return gender