# Dependency function 1
def depfunc1(num: int): 
    num = int(num)    # Convert input to integer (optional since type is already int)
    num += 1          # Add 1 to the number
    return num        # Return the result

# Dependency function 2
def depfunc2(num): 
    num = int(num)    # Convert input to integer (no type hint, so this ensures safety)
    num += 2          # Add 2 to the number
    return num        # Return the result

# Route handler for GET request at /main/{num}
@app.get("/main/{num}")
def get_main(
    num: int,                                           # Path parameter from the URL (e.g., /main/3)
    num1: Annotated[int, Depends(depfunc1)],           # Injected dependency: result from depfunc1
    num2: Annotated[int, Depends(depfunc2)]            # Injected dependency: result from depfunc2
):
    # Add all three values together: 
    # num from path, num1 = num + 1, num2 = num + 2
    total = num + num1 + num2
    
    # Return the result in a string response
    return f"Pakistan {total}"
