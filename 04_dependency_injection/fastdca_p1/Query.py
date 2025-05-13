# Import necessary modules from FastAPI
from fastapi import FastAPI, Depends, Query

# Import Annotated for type hinting with dependencies
from typing import Annotated

# Create an instance of the FastAPI class to define your web application
app: FastAPI = FastAPI()

# ------------------------------------------------------------
# Dependency function to handle login validation
# ------------------------------------------------------------

# This function takes two query parameters: username and password
# Both parameters are optional (default is None)
def dep_login(username: str = Query(None), password: str = Query(None)):
    # Check if the username and password are both 'admin'
    if username == "admin" and password == "admin":
        # Return a success message if credentials match
        return {"message": "Login Successful"}
    else:
        # Return a failure message otherwise
        return {"message": "Login Failed"}

# ------------------------------------------------------------
# Define an API route that uses the dependency function
# ------------------------------------------------------------

# This endpoint is accessible via HTTP GET at "/signin"
# The `user` parameter depends on the output of the `dep_login` function
# The Annotated type tells FastAPI to use `Depends(dep_login)` for resolving the parameter
@app.get("/signin")
def login_api(user: Annotated[dict, Depends(dep_login)]):
    # Return the result from the dependency (either success or failure message)
    return user
