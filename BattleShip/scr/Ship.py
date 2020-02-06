from typing import List, Dict, Iterable
from .Board import Board


class Ship(object):
    def __init__(self, boat_name: str):
        self.boat_cover_point = {}
        self.boat_name = boat_name


    def print_boat_name(self) -> str:
        return self.boat_name
