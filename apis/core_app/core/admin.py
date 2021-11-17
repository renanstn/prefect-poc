from django.contrib import admin
from core import models


@admin.register(models.Run)
class RunAdmin(admin.ModelAdmin):
    list_display = ["id", "result"]
    ordering = ["id"]


@admin.register(models.Value)
class ValueAdmin(admin.ModelAdmin):
    list_display = ["id", "value_a", "value_b"]
    ordering = ["id"]
