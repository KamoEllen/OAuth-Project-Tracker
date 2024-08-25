from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "contact@me.my",
                "password": "weakpassword"
            }
        }

class ProjectSchema(BaseModel):
    task: str = Field(...)
    createdBy: str = Field(...)
    startDate: datetime = Field(...)
    endDate: datetime = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "task": "Example Task",
                "createdBy": "Ellie",
                "startDate": "2021-01-01T00:00:00",
                "endDate": "2021-12-31T23:59:59",
            }
        }

class UpdateProjectModel(BaseModel):
    task: Optional[str]
    createdBy: Optional[str]
    startDate: Optional[datetime]
    endDate: Optional[datetime]

    class Config:
        schema_extra = {
            "example": {
                "task": "Updated Task",
                "createdBy": "Ellie",
                "startDate": "2021-01-01T00:00:00",
                "endDate": "2021-12-31T23:59:59",
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
