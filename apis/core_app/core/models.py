from django.db import models


class Run(models.Model):
    """
    Stores the results of each pipeline run
    """

    id = models.AutoField(primary_key=True)
    result = models.CharField(max_length=255)

    def __str__(self) -> str:
        return str(self.id)


class Value(models.Model):
    """
    Stores the values used to compose the result
    """

    id = models.AutoField(primary_key=True)
    run = models.ForeignKey(
        Run, on_delete=models.CASCADE, related_name="values"
    )
    value_a = models.IntegerField()
    value_b = models.IntegerField()
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.run.id}: {self.value_a} / {self.value_b}"


class Food(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, help_text="The food's name")
    price = models.DecimalField(
        max_digits=5, decimal_places=2, help_text="The food's price"
    )

    def __str__(self) -> str:
        return self.name
