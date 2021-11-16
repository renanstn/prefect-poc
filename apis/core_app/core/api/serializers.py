from rest_framework import serializers
from core import models


class RunSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Run
        fields = ["result"]
