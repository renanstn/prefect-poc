from django.contrib import admin
from core import models


@admin.register(models.Run)
class RunAdmin(admin.ModelAdmin):
    list_display = ["id", "result"]
    ordering = ["id"]
