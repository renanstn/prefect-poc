from django.db import models


class Run(models.Model):
    id = models.AutoField(primary_key=True)
    result = models.CharField(max_length=255)

    def __str__(self) -> str:
        return str(self.id)
