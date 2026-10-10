from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to my CI/CD Calculator API!"}

@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}
