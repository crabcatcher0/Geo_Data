from typing import Any, Dict

import requests
from django.shortcuts import get_object_or_404

from core.models import City

# validate longitudes (-180.000000 to 180.000000)
# and latitudes (-90.000000 to 90.000000)


# def extract_coordinates(to_read: Any):
#     pattern = r"([-+]?((1[0-7]\d|\d{1,2})(\.\d+)?|180(\.0+)?)),\s*([-+]?([1-8]?\d(\.\d+)?|90(\.0+)?))"
#     with open(to_read, "r") as file:
#         text = file.read()
#     coordinates = re.findall(pattern, text)

#     return [(match[0], match[5]) for match in coordinates]


# coordinates = extract_coordinates("cities.csv")
# for coord in coordinates:
#     print(f"Longitude: {coord[0]}, Latitude: {coord[1]}")


def json_data(name: str) -> str:
    return f"/static/geojson/{name.lower()}_boundaries.geojson"


def get_boundaries(name: str) -> dict[str, Any]:
    url = json_data(name=name)
    print(f"Fetching GeoJSON from: {url}")
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error fetching data: {response.status_code} - {response.text}")
        return {}

    geojson_data = response.json()

    city = get_object_or_404(City, name__iexact=name)
    city_geojson: Dict[str, Any] = {"type": "FeatureCollection", "features": []}

    for feature in geojson_data.get("features", []):
        if feature["properties"]["name"] == city.name:
            city_geojson["features"].append(feature)

    return city_geojson
