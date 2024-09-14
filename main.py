from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from typing import List

app = FastAPI()

templates = Jinja2Templates(directory="templates")

cars = [
    {"id": 1, "make": "Toyota", "model": "Camry", "year": 2020},
    {"id": 2, "make": "Honda", "model": "Civic", "year": 2019},
    {"id": 3, "make": "Ford", "model": "Mustang", "year": 2018},
    {"id": 4, "make": "Chevrolet", "model": "Impala", "year": 2020},
    {"id": 5, "make": "BMW", "model": "3 Series", "year": 2021},
    {"id": 6, "make": "Audi", "model": "A4", "year": 2017},
    {"id": 7, "make": "Tesla", "model": "Model 3", "year": 2022},
    {"id": 8, "make": "Mercedes", "model": "C-Class", "year": 2020},
    {"id": 9, "make": "Nissan", "model": "Altima", "year": 2021},
    {"id": 10, "make": "Hyundai", "model": "Sonata", "year": 2019},
    {"id": 11, "make": "Kia", "model": "Optima", "year": 2020},
    {"id": 12, "make": "Mazda", "model": "Mazda6", "year": 2021},
]


users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
    {"id": 4, "name": "David", "email": "david@example.com"}
]


@app.get("/cars/", response_model=List[dict])
def get_cars(page: int = Query(1, ge=1), limit: int = Query(10, ge=1)):
    start = (page - 1) * limit
    end = start + limit
    return cars[start:end]


@app.get("/cars/{id}")
def get_car(id: int):
    car = next((car for car in cars if car["id"] == id), None)

    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")

    return car




@app.get("/users", response_class=HTMLResponse)
def get_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})