from fastapi import FastAPI, Depends, Query
from typing import Annotated

app : FastAPI = FastAPI()


def depfunc1(num:int):
    num = int(num)
    num += 1
    return num

def depfunc2(num:int):
    num = int(num)
    num += 2
    return num


@app.get("/main/{num}")
def get_main(num: int, num1: Annotated[int, Depends(depfunc1)], num2: Annotated[int, Depends(depfunc2)]):
    total = num + num1 + num2
    return f"Pakistan {total}"
#     return f"Pakistan {num1} {num2}"