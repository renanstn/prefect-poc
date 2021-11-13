import names
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/random_name")
def read_item():
    name = names.get_first_name()
    return {"random_name": name}
