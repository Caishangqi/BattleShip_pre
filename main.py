import sys
from BattleShip.scr.Game import Game

if __name__ == '__main__':
    file = open(sys.argv[1], "r")
    configuration_file = []
    ships_in_list = []
    for line in file.readlines():
        line = line.strip('\n')
        configuration_file.append(line)
    dimension = configuration_file[0].split(" ")
    for element in dimension:
        element = int(element)
    for ships in range(1, len(configuration_file)):
        ships_in_list.append(ships)
    # Game need input dimension and list of ships
    game1 = Game(dimension, ships_in_list)
    game1.play()
