from typing import List, Dict, Iterable
from .Board import Board


class Ship(object):
    def __init__(self, orientaion_point: list[int], boat_name: str):
        self.orientation_point = orientaion_point
        self.boat_cover_point = []
        self.boat_name = boat_name

    def print_boat_name(self) -> str:
        return self.boat_name
