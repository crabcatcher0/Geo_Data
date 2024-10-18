from django.shortcuts import render
from django.http.request import HttpRequest

import folium  # type: ignore


def main_map(request: HttpRequest):
    main_coordinates = [27.7103, 85.3222]
    map_location = folium.Map(location=main_coordinates, zoom_start=13)
    map_html = map_location._repr_html_()  # type: ignore
    return render(request, "index.html", {"map_html": map_html})
