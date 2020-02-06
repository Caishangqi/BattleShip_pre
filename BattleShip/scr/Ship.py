from typing import List, Dict, Iterable
from .Board import Board


class Ship(object):

    """
    use boat_cover_point to determine which boat is hit. traversing all cover point
    to find the ship name of the hit boat.

    If one player hit others boat, program should traverse  all ships_with_entities = [] with
    ship_with_entities.is_hitted(player's target enter) to return the Boat name.

    This method could be stupid:)
    """

    def __init__(self, boat_name: str):
        self.boat_cover_point = []
        self.boat_name = boat_name


    def print_boat_name(self) -> str:
        return self.boat_name

    def is_hitted(self,target:[int]):
        for points in self.boat_cover_point:
            if target == points:
                return self.print_boat_name()






