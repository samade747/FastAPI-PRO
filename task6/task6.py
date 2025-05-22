from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, constr, validator
from typing import List, Optional
from datetime import date
from uuid import uuid4

app = FastAPI()

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
    
# TaskCreate model (used for POST requests)
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

# TaskStatusUpdate model for PUT requests
class TaskStatusUpdate(BaseModel):
    status: str

    @validator('status')
    def validate_status(cls, v):
        allowed_statuses = ["pending", "in progress", "completed"]
        if v not in allowed_statuses:
            raise ValueError(f"Status must be one of {allowed_statuses}")
        return v
    


#  POST /users/ - Create a new user
@app.post("/users/", response_model=UserRead)
def create_user(user: UserCreate):
    user_id = str(uuid4())  # Generate a unique user ID
    user_data = {
        "id": user_id,
        "username": user.username,
        "email": user.email
    }
    users_db[user_id] = user_data
    return user_data


#  GET /users/{user_id} - Retrieve a user by ID
@app.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: str):
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


#  POST /tasks/ - Create a new task
@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate):
    if task.user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")

    task_id = str(uuid4())
    task_data = Task(
        id=task_id,
        user_id=task.user_id,
        title=task.title,
        description=task.description,
        due_date=task.due_date,
        status="pending"
    )
    tasks_db[task_id] = task_data
    return task_data


# GET /tasks/{task_id} - Retrieve a task by ID
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: str):
    task = tasks_db.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


#  PUT /tasks/{task_id} - Update task status
@app.put("/tasks/{task_id}", response_model=Task)
def update_task_status(task_id: str, status_update: TaskStatusUpdate):
    task = tasks_db.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.status = status_update.status
    return task


# GET /users/{user_id}/tasks - List all tasks for a user
@app.get("/users/{user_id}/tasks", response_model=List[Task])
def get_user_tasks(user_id: str):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")

    user_tasks = [task for task in tasks_db.values() if task.user_id == user_id]
    return user_tasks