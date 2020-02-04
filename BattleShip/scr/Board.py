from typing import *


class Board(object):
    def __init__(self, num_rows: int, num_cols: int, blank_char: str = "*") -> None:
        self.grid = [[blank_char for col in range(num_cols+1)] for row in range(num_rows+1)]
        self.blank_char = blank_char

    @property
    def num_rows(self) -> int:
        return len(self.grid)

    @property
    def num_cols(self) -> int:
        # different
        return len(self.grid[0])

    def __str__(self) -> str:
        """
          0 1 2
        0 X 0 *
        1 * * 0
        2 O O X
        :return:
        """
        sep = ' ' * max([len(str(self.num_rows)), len(str(self.num_cols))])
        rep = sep * 2 + sep.join((str(i) for i in range(self.num_cols))) + '\n'
        for row_index, row in enumerate(self):
            rep += str(row_index) + sep + sep.join(row) + '\n'
        return rep

    def __iter__(self) -> Iterator[List[str]]:
        return iter(self.grid)

    def __getitem__(self, index: int) -> List[str]:
        return self.grid[index]

    def is_in_bounds(self, row: int, col: int) -> bool:
        return (0 <= row < self.num_rows and
                0 <= col < self.num_cols)


