import requests
from prefect import Task


class GetRandomName(Task):
    def run(self):
        response = requests.get("http://localhost:8000/random_name")
        if response.status_code == 200:
            response_json = response.json()
            return response_json.get("random_name")
        raise Exception("Problem getting random name")


class GetRandomNumber(Task):
    def run(self):
        response = requests.get("http://localhost:8000/random_number")
        if response.status_code == 200:
            response_json = response.json()
            return response_json.get("random_number")
        raise Exception("Problem getting random value")


class SumValues(Task):
    def run(self, value_a: int, value_b: int):
        data = {"value_a": value_a, "value_b": value_b}
        response = requests.post("http://localhost:8000/calculator/sum/", json=data)
        if response.status_code == 200:
            response_json = response.json()
            return response_json.get("result")
        raise Exception("Problem getting the sum of values")


class ShowLog(Task):
    def run(self, random_name, result):
        self.logger.info(random_name)
        self.logger.info(result)
