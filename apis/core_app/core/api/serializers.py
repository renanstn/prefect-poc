from rest_framework import serializers
from core import models


class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Value
        fields = ("value_a", "value_b", "name")


class RunSerializer(serializers.ModelSerializer):
    values = ValueSerializer(many=True)

    class Meta:
        model = models.Run
        fields = ("id", "result", "values")

    def create(self, validated_data):
        """
        Save the run and their values linked
        """
        values_data = validated_data.pop("values")
        run = models.Run.objects.create(**validated_data)
        for value in values_data:
            models.Value.objects.create(run=run, **value)
        return run
