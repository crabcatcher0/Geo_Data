from django.urls import path
from .views import main_map

urlpatterns = [path("", main_map, name="map")]
