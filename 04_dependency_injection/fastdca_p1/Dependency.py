# Import required tools from FastAPI
from fastapi import FastAPI, Depends
from typing import Annotated

# Create the FastAPI application
app = FastAPI()

# ✅ Dependency function that accepts a "username" as input
def get_goal(username: str):
    # Returns a dictionary with a goal message and the provided username
    return {
        "goal": "We are building AI Agents Workforce",
        "username": username  # This value comes from the user (query parameter)
    }

# ✅ Route handler for GET request to /get-goal
@app.get("/get-goal")
def get_my_goal(response: Annotated[dict, Depends(get_goal)]):
    # 'response' will automatically get the output of get_goal()
    return response  # Send that as the response to the browser
