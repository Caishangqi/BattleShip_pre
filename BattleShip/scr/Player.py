from typing import Iterable
from .Attack import Attack
from .Board import Board


class Player(object):
    def __init__(self,other_players: Iterable["Player"]):
        self.name = self.get_name_from_player(other_players)
        pass

    def get_name_from_player(self, other_players: Iterable["Player"]) -> str:
        already_used_names = set([player.name for player in other_players])
        while True:
            name = input('Please enter your name: ')
            if name not in already_used_names:
                return name
            else:
                print(f'{name} has already been used. Pick another name.')

    def take_turn(self, the_board: "Board") -> None:
        while True:
            move = self.get_move()
            move.make(the_board)

    def place_ships(self):
        pass
