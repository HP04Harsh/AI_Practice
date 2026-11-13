from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Pydantic Model for validation
class ChaiItem(BaseModel):
    name: str
    price: float
    is_hot: bool = True

# Mock database
menu = []

@app.get("/menu")
def get_menu():
    return {"menu": menu}

@app.post("/menu")
def add_chai(item: ChaiItem):
    menu.append(item)
    return {"message": "Chai added successfully!", "item": item}