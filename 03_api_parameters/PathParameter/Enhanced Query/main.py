from fastapi import FastAPI, Query


app = FastAPI()

@app.get("/items/")
async def read_items(
    q: str | None = Query(
        None,  # Default value is None (optional parameter)
        title="Query string",
        description="Query string for searching items",
        min_length=3,
        max_length=50
    ),
    skip: int = Query(0, ge=0),  # Greater than or equal to 0
    limit: int = Query(10, le=100)  # Less than or equal to 100
):
    return {"q": q, "skip": skip, "limit": limit}