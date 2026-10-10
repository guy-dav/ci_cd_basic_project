from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World! This is my automated CD pipeline working!"}

@app.get("/add")
def add(a: int, b: int):
    return a + b

@app.get("/multiply")
def multiply(a: int, b: int):
    return a * b

