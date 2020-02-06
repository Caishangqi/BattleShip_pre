from typing import *
from .Attack import Attack
from .Board import Board


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

    def place_ships(self, ships: List[Tuple[str, int]], boards: List[List[str]]) -> None:
        self.ships=[]
        for ship in ships:
            ship_coordinates = [ship[0]]
            while True:
                while True:
                    self.direction = input("Do you want to place your ship vertically or horizontally? Please type h or v:")
                    if self.direction != "h" and self.direction != "v":
                        continue
                    else:
                        print("What coordinates do you want to place your ship? Please enter the first row and col numners. Please enter integers.")
                        break
                while True:
                    self.y = input("Please enter the first row number:")
                    self.x = input("Please enter the first col number:")
                    try:
                        int(self.y)
                        int(self.x)
                        break
                    except:
                        continue
                if self.check_ship_valid(ship, boards) == True:
                    if self.direction == "h":
                        for k in range(int(self.x), int(self.x) + ship[1]):
                            boards[int(self.y)][k] = ship[0][0]
                        for l in range(ship[1]):
                            ship_coordinates.append(self.y + str(int(self.x) + l))
                    elif self.direction == "v":
                        for k in range(int(self.y), int(self.y) + ship[1]):
                            boards[k][int(self.x)] = ship[0][0]
                        for l in range(ship[1]):
                            ship_coordinates.append(str(int(self.y) + l) + self.x)
                    break
                else:
                    print("Your coordinates choice is invalid.")
                    continue
            self.ships.append(ship_coordinates)

    def orientation_overlapped(self, boards: List[List[str]]) -> bool:
        if int(self.x) < (len(boards[0]) - 1) and int(self.y) < (len(boards) - 1):
            if boards[int(self.y)][int(self.x)] == "*":
                return False
            else:
                return True
        else:
            return True

    def ship_horizontal_valid(self, ship: Tuple[str, int], boards: List[List[str]]) -> bool:
        for hrz in range(ship[1]):
            if (int(self.x) + hrz) > (len(boards[0]) - 1) or boards[int(self.y)][int(self.x) + hrz].isalpha() == True:
                return False
        return True

    def ship_vertical_valid(self, ship: Tuple[str, int], boards: List[List[str]]) -> bool:
        for vet in range(ship[1]):
            if (int(self.y) + vet) > (len(boards) - 1) or boards[int(self.y) + vet][int(self.x)].isalpha() == True:
                return False
        return True

    def check_ship_valid(self, ship: Tuple[str, int], boards: List[List[str]]) -> bool:
        if self.orientation_overlapped(boards) == False:
            if self.direction == "h":
                if self.ship_horizontal_valid(ship, boards) == True:
                    return True
                else:
                    return False
            if self.direction == "v":
                if self.ship_vertical_valid(ship, boards) == True:
                    return True
                else:
                    return False
        else:
            return False
