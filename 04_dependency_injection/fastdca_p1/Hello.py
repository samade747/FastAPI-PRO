# Importing FastAPI and Depends from the fastapi library
from fastapi import FastAPI, Depends

# Importing Annotated from the typing module (used to provide extra info about variables)
from typing import Annotated

# Create an instance of FastAPI
# This is like starting your web application
app = FastAPI()

# This function returns a simple goal as a dictionary (key-value pair)
# It can be used as a dependency in other functions
def get_simple_goal():
    # Returning a simple goal message
    return {"goal": "We are building AI Agents Workforce"}

# This is an API route (a URL endpoint)
# When you visit http://127.0.0.1:8000/get-simple-goal in the browser,
# this function will be called
@app.get("/get-simple-goal")
def simple_goal(response: Annotated[dict, Depends(get_simple_goal)]):
    # The 'response' variable will automatically receive the result from get_simple_goal()
    # Thanks to FastAPI's 'Depends' system
    return response  # Send the goal as a response to the user
