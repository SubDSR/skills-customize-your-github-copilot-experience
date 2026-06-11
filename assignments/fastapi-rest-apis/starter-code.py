from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="FastAPI REST API Assignment")


class Item(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    completed: bool = False


items = [
    {"id": 1, "name": "Read the assignment", "completed": False},
]


@app.get("/")
def read_root():
    return {"message": "FastAPI is running"}


@app.get("/items")
def list_items():
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")


@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    new_item = item.model_dump()
    new_item["id"] = max((existing["id"] for existing in items), default=0) + 1
    items.append(new_item)
    return new_item


@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items):
        if item["id"] == item_id:
            replacement = updated_item.model_dump()
            replacement["id"] = item_id
            items[index] = replacement
            return replacement
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item["id"] == item_id:
            items.pop(index)
            return None
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
