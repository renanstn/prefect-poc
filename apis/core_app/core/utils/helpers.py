import requests


def get_random_name():
    response = requests.get("http://random_name/random_name")
    if response.status_code == 200:
        response_json = response.json()
        return response_json.get("random_name")
    raise Exception("Problem getting random name")


def get_random_number():
    response = requests.get("http://random_number/random_number")
    if response.status_code == 200:
        response_json = response.json()
        return response_json.get("random_number")
    raise Exception("Problem getting random value")


def sum_values(value_a, value_b):
    data = {"value_a": value_a, "value_b": value_b}
    response = requests.post("http://calculator/sum/", json=data)
    if response.status_code == 200:
        response_json = response.json()
        return response_json.get("result")
    raise Exception("Problem getting the sum of values")
