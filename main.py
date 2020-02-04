import sys
from BattleShip.scr.Game import Game

if __name__ == '__main__':
    file = open(sys.argv[1], "r")
    configuration_file = []
    ships = []
    for line in file.readlines():
        line = line.strip('\n')
        configuration_file.append(line)
    dimension = configuration_file[0].split()
    for i in range(len(dimension)):
        dimension[i] = int(dimension[i])
    for i in range(1, len(configuration_file)):
        index, element = configuration_file[i].split()
        ships.append((index[0], int(element)))
    # Game need input dimension and list of ships
    game1 = Game(dimension, ships)
    game1.play()   #Test