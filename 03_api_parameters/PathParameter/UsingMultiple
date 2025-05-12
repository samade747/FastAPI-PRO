from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

app = FastAPI()

@app.put("/items/validated/{item_id}")
async def update_item(
    item_id: int = Path(..., title="Item ID", ge=1),
    q: str | None = Query(None, min_length=3),
    item: Item | None = Body(None, description="Optional item data (JSON body)")
):
    result = {"item_id": item_id}
    if q:
        result.update({"q": q})
    if item:
        result.update({"item": item.model_dump()})
    return result