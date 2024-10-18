from django.urls import path
from .views import main_map
from .views import home

urlpatterns = [path("", home, name="home"), path("map/", main_map, name="map")]
