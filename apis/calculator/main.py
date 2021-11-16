from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class SumValues(BaseModel):
    value_a: int
    value_b: int


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/sum/")
def sum(sum_values: SumValues):
    result = sum_values.value_a + sum_values.value_b
    return {"result": result}
