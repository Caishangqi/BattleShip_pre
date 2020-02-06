from . import Player
from . import Board
from . import Ship

Board = Board.Board


class Attack(object):
    def __init__(self, maker: "Player.Player", row: int, col: int) -> None:
        self.maker = maker
        self.row = row
        self.col = col

    @classmethod
    def from_str(cls, maker: "Player.Player", str_move: str) -> "Move":
        """

        :param maker:
        :param str_move: should be in the form row, col
        :return:
        """

        try:
            row, col = str_move.split(',')
        except ValueError:
            raise (f'{str_move} is not in the form row, col')

        try:
            row = int(row)
        except ValueError:
            raise (f'row needs to be an integer. {row} is not an integer')

        try:
            col = int(col)
        except ValueError:
            raise (f'col needs to be an integer. {col} is not an integer')

        return cls(maker, row, col)

    def attack(self, the_board: "Board.Board") -> None:
        if not the_board.is_in_bounds(self.row, self.col):
            raise (f'{self.row}, {self.col} is not in bounds')
        elif the_board.grid[self.row][self.col] == "X" or "0":
            raise (f"You can't attack at {self.row}, {self.col} because you have already attak there")
        elif the_board.grid[self.row][self.col].isalpha() == True and the_board.grid[self.row][self.col] != "X":
            the_board.grid[self.row][self.col] = "X"
            return Ship.Ship.boat_name #查找覆盖点在对应名字返回它
        else:the_board.grid[self.row][self.col] = "O"
