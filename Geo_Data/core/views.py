from typing import Any

import folium  # type: ignore
from django.http.request import HttpRequest
from django.shortcuts import render
from folium.plugins import Fullscreen  # type: ignore

from core.models import City


def home(request: HttpRequest):
    data = []
    name = ""
    count_result = 0
    if "search" in request.GET and request.GET["search"]:
        name: Any = request.GET["search"]
        data = City.objects.filter(name__icontains=name)
        count_result = data.count()
    context: dict[str, Any] = {"data": data, "name": name, "count": count_result}
    return render(request, "home.html", context)


def main_map(request: HttpRequest):
    city_name = request.GET.get("city")
    if city_name:
        try:
            city = City.objects.get(name__iexact=city_name)
            lat = city.latitude
            long = city.longitutude
        except City.DoesNotExist:
            return render(request, "index.html", {"error": "City not found."})
    else:
        return render(request, "index.html", {"error": "No city provided."})

    map_location = folium.Map(location=[lat, long], zoom_start=13)
    Fullscreen().add_to(map_location)
    folium.Marker([lat, long], tooltip=city.name).add_to(map_location)
    map_html = map_location._repr_html_()  # type: ignore

    return render(request, "index.html", {"map_html": map_html})


def list_cities(request: HttpRequest):
    cities = City.objects.all()
    context = {"cities": cities}
    return render(request, "cities.html", context)
