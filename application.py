from fastapi import FastAPI

application  = FastAPI()

@application.get("/")
def read_root():
    return {"message": "Hello World! This is my automated CD pipeline working!"}

@application.get("/add")
def add(a: int, b: int):
    return a + b

@application.get("/multiply")
def multiply(a: int, b: int):
    return a * b

@application.get("/subtract")
def subtract(a: int, b: int):
    return a - b

