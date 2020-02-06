from typing import *
from .Board import Board
from .Player import Player


class Game(object):
    def __init__(self, dimension: List[int], ships: List[Tuple[str, int]], blank_char: str = "*") -> None:
        self.blank_char = blank_char
        # this dimension[0] is row number dimension[1] is col number.
        self.board = Board(dimension[0], dimension[1], blank_char)
        self.boards = [self.board.grid for i in range(2)]
        self.ships = ships
        # Board[0] is player 1's Board[1] is player 2's
        self._cur_player_turn = 0

    def play(self) -> None:
        self.players = []
        for player_num in range(2):
            self.player = Player(self.players)
            self.players.append(self.player.name)
            if player_num==0:
                self.player.place_ships1(self.ships, self.boards)
            elif player_num==1:
                self.player.place_ships2(self.ships, self.boards)
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

    def check_ship_valid(self)->bool:
        if orientation_overlapped() == False:
            if ship_direction == "h":
                if ship_horizontal_valid() == True:
                    return True
                else: return False
            if ship_direction == "v":
                if ship_vertical_valid() == True:
                    return True
                else:return False
        else: return False

    def orientation_overlapped(self)->bool:
        if col_give_by_player < Board.num_cols and reo_give_by_player < Board.num_rows:
            if self.players[self._cur_player_turn].


