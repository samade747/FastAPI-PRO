
# # Simulate a Database: Use a class as a dependency to act like a database.

# Import necessary classes and functions from FastAPI
from fastapi import FastAPI, Depends, Query


# Import Annotated from typing to use for dependency injection with type hints
from typing import Annotated

# Create a FastAPI application instance
app: FastAPI = FastAPI()

# This function acts as a "dependency"
# It will automatically run when any route depends on it
def dep_login(username: str = Query(None), password: str = Query(None)):
    # Check if username and password are both 'admin'
    if username == "admin" and password == "admin":
        # If correct, return a success message
        return {"message": "Login Successful"}
    else:
        # If not correct, return a failure message
        return {"message": "Login Failed"}

# Define a GET route at the URL path "/signin"
@app.get("/signin")
# This function depends on `dep_login`, which is used to simulate login validation
# The return value from `dep_login` is passed into the parameter `user`
def login_api(user: Annotated[dict, Depends(dep_login)]):
    # Return the message returned from dep_login
    return user









# from fastapi import FastAPI, Depends, Query
# from typing import Annotated


# app : FastAPI = FastAPI()

# # depency function

# def dep_login(username : str = Query(None), password : str = Query(None)):
#     if username == "admin" and password == "admin":
#         return {"message" : "Login Sucessful"}
#     else:
#         return {"message" : "Login Failed"}
    
# @app.get("/signin")
# def login_api(user : Annotated[dict, Depends(dep_login)]):
#     return user
