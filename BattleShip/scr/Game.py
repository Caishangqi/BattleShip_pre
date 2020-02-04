from typing import *
from .Board import Board
from .Player import Player
from .Ship import Ship


class Game(object):
    def __init__(self, dimension: List[int],ships: List, blank_char: str = "*") -> None:
        self.blank_char = blank_char
        # this dimension[0] is row number dimension[1] is col number.
        self.board = [].append(Board(dimension[0], dimension[1], blank_char) for i in range(2))
        self.ships = [].append(ships)
        # Board[0] is player 1's Board[1] is player 2's
        self.players = []
        self._cur_player_turn = 0

    def play(self) -> None:
        while not self.is_game_over():
            self.display_game_state()
            self.cur_player.take_turn(self.board)
            self.change_turn()
        self.change_turn()
        self.display_game_state()
        self.display_the_winner()

    def display_game_state(self) -> None:
        print(self.board)

    def is_game_over(self):
        return self.someone_won()

    def someone_won(self) -> bool:
        pass

    def change_turn(self) -> None:
        if self._cur_player_turn == 0:
            self._cur_player_turn = 1
        else:
            self._cur_player_turn = 0

    @property
    def cur_player(self) -> "Player":
        return self.players[self._cur_player_turn]

    def display_the_winner(self):
        if self.someone_won():
            print(f'{self.cur_player} won the game!')
