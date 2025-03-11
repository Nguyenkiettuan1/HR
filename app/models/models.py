from pydantic import BaseModel, Field
from typing import Optional, List, Literal
from bson import ObjectId
from datetime import datetime, date


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return str(v)


class Employee(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    full_name: str
    email: str
    password: str
    role: Literal["EMPLOYEE", "ADMIN"] = "EMPLOYEE"
    created_at: datetime = Field(default_factory=datetime.now())


class LeaveType(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    leave_type_name: str
    description: Optional[str] = None


class LeaveRequest(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    employee_id: PyObjectId
    leave_types_id: PyObjectId
    start_date: datetime
    end_date: datetime
    reason: Optional[str] = None
    status: Literal["PENDING", "PROCESSING", "REJECT", "ACCEPT"] = "PENDING"
    created_at: datetime = Field(default_factory=datetime.now())


class Approval(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    leave_request_id: PyObjectId
    employee_id: PyObjectId
    decision: Literal["REJECT", "ACCEPT"]
    created_at: datetime = Field(default_factory=datetime.now())
    comment: Optional[str] = None


