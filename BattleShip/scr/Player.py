from typing import Iterable
from .Attack import Attack
from .Board import Board

class Player(object):
    def __init__(self):
        pass

    def take_turn(self, the_board: "Board") -> None:
        while True:
            move = self.get_move()
            move.make(the_board)
