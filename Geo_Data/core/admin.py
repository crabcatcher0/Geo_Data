import csv
from typing import Any

from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.http.request import HttpRequest
from django.shortcuts import render
from django.urls import path, reverse

from core.models import City


class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "longitutude", "latitude")

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path(
                "bulk-add-cities/",
                self.admin_site.admin_view(self.bulk_add_cities),
                name="bulk-add-cities",
            ),
        ]
        return new_urls + urls

    def changelist_view(self, request: HttpRequest, extra_context: Any = None):
        extra_context = extra_context or {}
        extra_context["bulk_add_button"] = reverse("admin:bulk-add-cities")
        return super().changelist_view(request, extra_context=extra_context)

    def bulk_add_cities(self, request: HttpRequest):
        if request.method == "POST":
            file = request.FILES["file"]  # type: ignore

            if not file.name.endswith(".csv"):  # type: ignore
                self.message_user(
                    request, "Only CSV files are accepted.", messages.ERROR
                )
                return HttpResponseRedirect(request.path_info)

            decoded_file: Any = file.read().decode("utf-8").splitlines()  # type: ignore
            reader = csv.reader(decoded_file)

            for row in reader:
                try:
                    name, longitude, latitude = row
                    City.objects.create(
                        name=name,
                        longitutude=float(longitude),
                        latitude=float(latitude),
                    )
                except Exception as e:
                    self.message_user(
                        request,
                        f"Error processing row: {row} - {str(e)}",
                        messages.ERROR,
                    )

            self.message_user(
                request, "Cities have been added successfully.", messages.SUCCESS
            )
            return HttpResponseRedirect(request.path_info)

        context: dict[str, Any] = {
            "opts": self.model._meta,
            "app_label": self.model._meta.app_label,
        }
        return render(request, "admin/bulk_add_cities.html", context)


admin.site.register(City, CityAdmin)
