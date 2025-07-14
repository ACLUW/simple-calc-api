# main.py

from fastapi import FastAPI

app = FastAPI()

# Simple route to test
@app.get("/")
def read_root():
    return {"message": "Hello, ACL from FastAPI!"}  # ACL signature

