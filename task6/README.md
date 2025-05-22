⿦ Task 06

📝 Project: Task Tracker API
📦 Overview
Implement an API that manages Users and their Tasks, with:

🚀 Requirements
Pydantic Models & Validation

Define UserCreate and UserRead models inheriting BaseModel. 

Use EmailStr for email validation. 

Constrain username to 3–20 characters using constr.

Ensure due_date ≥ today via a @validator. 

FastAPI Endpoints

Users
POST /users/ – create a user (return UserRead).

GET /users/{user_id} – retrieve user.

Tasks
POST /tasks/ – create a task (return full Task model).

GET /tasks/{task_id} – get task.

PUT /tasks/{task_id} – update status only, validating allowed values. 

GET /users/{user_id}/tasks – list all tasks for a user.

with complete comments each task seperately 




| Feature                          | Description                                              |
| -------------------------------- | -------------------------------------------------------- |
| **UserCreate & UserRead Models** | Validated using `constr` and `EmailStr`                  |
| **Task Date Validation**         | Ensures `due_date >= today`                              |
| **Status Validation**            | Only accepts `"pending"`, `"in progress"`, `"completed"` |
| **POST /users/**                 | Adds new user                                            |
| **GET /users/{user\_id}**        | Retrieves user                                           |
| **POST /tasks/**                 | Adds task for a user                                     |
| **GET /tasks/{task\_id}**        | Retrieves task                                           |
| **PUT /tasks/{task\_id}**        | Updates task status                                      |
| **GET /users/{user\_id}/tasks**  | Lists tasks by user                                      |
