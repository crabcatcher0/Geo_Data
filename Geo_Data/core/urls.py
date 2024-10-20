from django.urls import path
from .views import main_map
from .views import home
from .views import list_cities

urlpatterns = [
    path("", home, name="home"),
    path("map/", main_map, name="map"),
    path("cities/", list_cities, name="cities"),
]
