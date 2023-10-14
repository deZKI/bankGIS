from math import radians, sin, cos, sqrt, atan2

from django.db.models import Func, FloatField


def haversine_distance(lat1, lon1, lat2, lon2):
    """ Расстояние между точками на глобусе"""
    R = 6371  # Радиус Земли в километрах

    lat1_rad = radians(lat1)
    lon1_rad = radians(lon1)
    lat2_rad = radians(lat2)
    lon2_rad = radians(lon2)

    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad

    a = sin(dlat / 2) ** 2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


def parse_coordinate(coordinate_str: str):
    """ Замена , на . в числах"""
    coordinate_str = coordinate_str.replace(',', '.')
    try:
        coordinate = float(coordinate_str)
        return coordinate
    except ValueError:
        return None


class Atan2Func(Func):
    function = 'ATAN2'
    output_field = FloatField()
