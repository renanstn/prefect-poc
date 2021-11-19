from rest_framework.response import Response
from rest_framework import viewsets
from prefect import Flow

from core.utils import tasks
from core.api import serializers
from core import models


class HelloViewSet(viewsets.ViewSet):
    """
    A dummy viewset just for tests
    """

    def list(self, request):
        return Response({"message": "pong"})


class StartFluxViewSet(viewsets.ViewSet):
    """
    An endpoint to receive commands to start the flux pipeline
    """

    def create(self, request):
        random_name_task = tasks.GetRandomName()
        random_number_task = tasks.GetRandomNumber()

        with Flow("Teste") as flow:
            # Get random values from APIs
            random_name = random_name_task.run()
            random_value_a = random_number_task.run()
            random_value_b = random_number_task.run()

            # Sum random numbers using API
            sum_task = tasks.SumValues(random_value_a, random_value_b)
            numbers_sum = sum_task.run()

            # Prepare data to save
            run = {
                "result": f"{random_name}-{numbers_sum}",
                "values": [
                    {
                        "value_a": random_value_a,
                        "value_b": random_value_b,
                        "name": random_name,
                    }
                ],
            }

            # Save data
            run_serializer = serializers.RunSerializer(data=run)
            run_serializer.is_valid(raise_exception=True)
            run_serializer.save()

            flow.run()

        return Response({"message": "pipeline finished"})


class RunViewSet(viewsets.ModelViewSet):
    queryset = models.Run.objects.all()
    serializer_class = serializers.RunSerializer
