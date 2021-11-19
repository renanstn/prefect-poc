import requests
from prefect import Task


class GetRandomName(Task):
    def run(self):
        response = requests.get("http://random_name/random_name")
        if response.status_code == 200:
            response_json = response.json()
            return response_json.get("random_name")
        raise Exception("Problem getting random name")


class GetRandomNumber(Task):
    def run(self):
        response = requests.get("http://random_number/random_number")
        if response.status_code == 200:
            response_json = response.json()
            return response_json.get("random_number")
        raise Exception("Problem getting random value")


class SumValues(Task):
    def __init__(self, value_a, value_b):
        self.value_a = value_a
        self.value_b = value_b

    def run(self):
        data = {"value_a": self.value_a, "value_b": self.value_b}
        response = requests.post("http://calculator/sum/", json=data)
        if response.status_code == 200:
            response_json = response.json()
            return response_json.get("result")
        raise Exception("Problem getting the sum of values")
