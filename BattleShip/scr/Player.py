from typing import *
from .Attack import Attack
from .Board import Board


def place_ships():

    print("you have total")


class Player(object):
    def __init__(self, other_players: Iterable["Player"]):
        self.name = self.get_name_from_player(other_players)
        pass

    def get_name_from_player(self, other_players: Iterable["Player"]) -> str:
        already_used_names = set([i for i in other_players])
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

    def place_ships1(self, ships: List[Tuple[str, int]], boards: List[List[List[str]]])->None:
        for j in range(len(ships)):
            direction=input("Do you want to place your ship vertically or horizontally? Please type h or v:")
            print("What coordinates do you want to place your ship? Please enter the first row and col numners.")
            x=input("Please enter the first row number:")
            y=input("Please enter the first col number:")
            if direction=="h":
                for k in range(int(x), int(x)+ships[j][1]):
                    boards[0][int(y)][k]=ships[j][0]
            elif direction=="v":
                for k in range(int(y), int(y)+ships[j][1]):
                    boards[0][k][int(x)]=ships[j][0]

    def place_ships2(self, ships: List[Tuple[str, int]], boards: List[List[List[str]]])->None:
        for j in range(len(ships)):
            direction=input("Do you want to place your ship vertically or horizontally? Please type h or v:")
            print("What coordinates do you want to place your ship? Please enter the first row and col numners.")
            x=input("Please enter the first row number:")
            y=input("Please enter the first col number:")
            if direction=="h":
                for k in range(int(x), int(x)+ships[j][1]):
                    boards[1][int(y)][k]=ships[j][0]
            elif direction=="v":
                for k in range(int(y), int(y)+ships[j][1]):
                    boards[1][k][int(x)]=ships[j][0]
