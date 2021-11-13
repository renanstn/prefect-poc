import random
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/random_number")
def read_item():
    number = random.randint(1, 100)
    return {"random_number": number}
