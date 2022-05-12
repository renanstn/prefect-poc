from prefect import Flow

import tasks


with Flow("hello-flow") as flow:
    random_name = tasks.GetRandomName(name="GetRandomName")()
    number_a = tasks.GetRandomNumber(name="GetRandomNumberA")()
    number_b = tasks.GetRandomNumber(name="GetRandomNumberB")()

    result = tasks.SumValues(name="SumValues")(number_a, number_b)

    tasks.ShowLog(name="ShowLog")(random_name, result)
