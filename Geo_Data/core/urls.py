from django.urls import path

from .views import home, list_cities, main_map

urlpatterns = [
    path("", home, name="home"),
    path("map/", main_map, name="map"),
    path("cities/", list_cities, name="cities"),
]
