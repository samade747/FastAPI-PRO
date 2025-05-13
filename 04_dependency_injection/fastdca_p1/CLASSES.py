# Import FastAPI components
from fastapi import FastAPI, Depends, HTTPException, status
from typing import Annotated

# Initialize the FastAPI application
app = FastAPI()

# --------------------------------------------------
# Mock data sources (acting like databases)
# --------------------------------------------------

# Dictionary simulating a database of blogs
blogs = {
    "1": "Generative AI Blog",
    "2": "Machine Learning Blog",
    "3": "Deep Learning Blog"
}

# Dictionary simulating a database of users
users = {
    "8": "Ahmed",
    "9": "Mohammed"
}

# --------------------------------------------------
# Dependency class to fetch objects or raise 404
# --------------------------------------------------

class GetObjectOr404():
    def __init__(self, model) -> None:
        """
        Initialize with a model (in this case, a dictionary like `blogs` or `users`).
        """
        self.model = model  # Save the model (dictionary) to use for lookup

    def __call__(self, id: str):
        """
        Make the class instance callable. Accepts an ID and attempts to retrieve the corresponding object.
        """
        obj = self.model.get(id)  # Try to get the object using the ID
        if not obj:
            # If object is not found, raise a 404 Not Found error
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Object ID {id} not found"
            )
        return obj  # Return the found object (e.g., blog title or user name)

# --------------------------------------------------
# Dependency instance for blog access
# --------------------------------------------------

# Create a reusable dependency that uses the blogs dictionary
blog_dependency = GetObjectOr404(blogs)

# Define a GET endpoint for fetching a blog by ID
@app.get("/blog/{id}")
def get_blog(blog_name: Annotated[str, Depends(blog_dependency)]):
    """
    Endpoint to return a blog name using the blog ID.
    Uses `blog_dependency` to retrieve the value.
    """
    return blog_name  # Return the title of the blog (e.g., "Generative AI Blog")

# --------------------------------------------------
# Dependency instance for user access
# --------------------------------------------------

# Create a reusable dependency that uses the users dictionary
user_dependency = GetObjectOr404(users)

# Define a GET endpoint for fetching a user by ID
@app.get("/user/{id}")
def get_user(user_name: Annotated[str, Depends(user_dependency)]):
    """
    Endpoint to return a user name using the user ID.
    Uses `user_dependency` to retrieve the value.
    """
    return user_name  # Return the name of the user (e.g., "Ahmed")
