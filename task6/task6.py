from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, constr, validator
from typing import List, Optional
from datetime import date
from uuid import uuid4

# In-memory "database"
users_db = {}
tasks_db = {}


# UserCreate model
class UserCreate(BaseModel):
    username: constr(min_length=3, max_length=20)  # Username constraint
    email: EmailStr  # Valid email


    # UserRead model
class UserRead(BaseModel):
    id: str
    username: str
    email: EmailStr

# Task model
class Task(BaseModel):
    id: str
    user_id: str
    title: str
    description: Optional[str] = None
    due_date: date
    status: str = "pending"

     # ✅ Validate due_date to ensure it is today or later

    @validator('due_date')
    def validate_due_date(cls, v):
        if v < date.today():
            raise ValueError("Due date must be today or in the future.")
        return v
    
    # ✅ Validate status to allow only specific values
    @validator('status')
    def validate_status(cls, v):
        allowed_statuses = ["pending", "in progress", "completed"]
        if v not in allowed_statuses:
            raise ValueError(f"Status must be one of {allowed_statuses}")
        return v
    
# ✅ TaskCreate model (used for POST requests)
class TaskCreate(BaseModel):
    user_id: str
    title: str
    description: Optional[str] = None
    due_date: date

    @validator('due_date')
    def validate_due_date(cls, v):
        if v < date.today():
            raise ValueError("Due date must be today or in the future.")
        return v