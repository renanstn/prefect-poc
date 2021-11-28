from typing import List

from django.contrib import admin, messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import path, reverse
from django.urls.resolvers import URLPattern
from django import forms

from core import models


@admin.register(models.Run)
class RunAdmin(admin.ModelAdmin):
    list_display = ["id", "result"]
    ordering = ["id"]


@admin.register(models.Value)
class ValueAdmin(admin.ModelAdmin):
    list_display = ["id", "value_a", "value_b"]
    ordering = ["id"]


class CsvImportform(forms.Form):
    csv_upload = forms.FileField()


@admin.register(models.Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]

    def get_urls(self) -> List[URLPattern]:
        urls = super().get_urls()
        new_urls = [path("upload-csv/", self.upload_csv)]
        return new_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
            # Read data from CSV file
            csv_file = request.FILES["csv_upload"]

            if not csv_file.name.endswith(".csv"):
                messages.warning(request, "Wrong file type. Only CSV allowed")
                return HttpResponseRedirect(request.path_info)

            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for data in csv_data:
                fields = data.split(",")
                models.Food.objects.create(name=fields[0], price=fields[1])

            url = reverse("admin:index")
            return HttpResponseRedirect(url)

        form = CsvImportform()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)
