from rest_framework.response import Response
from rest_framework import viewsets

from core.utils import helpers
from core.api import serializers


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
        random_name = helpers.get_random_name()
        random_value_a = helpers.get_random_number()
        random_value_b = helpers.get_random_number()
        numbers_sum = helpers.sum_values(random_value_a, random_value_b)
        run = {"result": f"{random_name}-{numbers_sum}"}
        run_serializer = serializers.RunSerializer(data=run)
        run_serializer.is_valid(raise_exception=True)
        run_serializer.save()
        return Response({"message": "pipeline finished"})
