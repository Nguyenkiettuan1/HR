from motor.motor_asyncio import AsyncIOMotorClient
from app.models import Employee, LeaveType, LeaveRequest, Approval
from datetime import datetime
import asyncio
import uuid

MONGODB_URL = "mongodb://localhost:27017"
DATABASE_NAME = "your_database_name"

client = AsyncIOMotorClient(MONGODB_URL)
db = client[DATABASE_NAME]

# Dummy data for migration
employees = [
    Employee(full_name="John Doe", email="john@example.com", password="123456"),
    Employee(full_name="Jane Doe", email="jane@example.com", password="abcdef"),
]

leave_types = [
    LeaveType(leave_type_name="Annual Leave", description="Yearly paid leave"),
    LeaveType(leave_type_name="Sick Leave", description="Leave for illness"),
]

leave_requests = [
    LeaveRequest(
        employee_id=employees[0].id,
        leave_types_id=leave_types[0].id,
        start_date=datetime(2024, 5, 1),
        end_date=datetime(2024, 5, 5),
        reason="Family vacation",
    )
]

approvals = [
    Approval(
        leave_request_id=leave_requests[0].id,
        employee_id=employees[1].id,
        decision="ACCEPT",
        comment="Approved for leave"
    )
]

async def migrate():
    # Insert Employees
    await db["employees"].insert_many([employee.dict(by_alias=True) for employee in employees])
    print("✅ Employees migrated successfully.")

    # Insert Leave Types
    await db["leave_types"].insert_many([leave_type.dict(by_alias=True) for leave_type in leave_types])
    print("✅ Leave types migrated successfully.")

    # Insert Leave Requests
    await db["leave_requests"].insert_many([request.dict(by_alias=True) for request in leave_requests])
    print("✅ Leave requests migrated successfully.")

    # Insert Approvals
    await db["approvals"].insert_many([approval.dict(by_alias=True) for approval in approvals])
    print("✅ Approvals migrated successfully.")

if __name__ == "__main__":
    asyncio.run(migrate())
