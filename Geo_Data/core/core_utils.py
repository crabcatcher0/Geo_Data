import re
from typing import Any

# validate longitudes (-180.000000 to 180.000000)
# and latitudes (-90.000000 to 90.000000)


def extract_coordinates(to_read: Any):
    pattern = r"([-+]?((1[0-7]\d|\d{1,2})(\.\d+)?|180(\.0+)?)),\s*([-+]?([1-8]?\d(\.\d+)?|90(\.0+)?))"
    with open(to_read, "r") as file:
        text = file.read()
    coordinates = re.findall(pattern, text)

    return [(match[0], match[5]) for match in coordinates]


coordinates = extract_coordinates("cities.csv")
for coord in coordinates:
    print(f"Longitude: {coord[0]}, Latitude: {coord[1]}")
