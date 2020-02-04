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
    for i in range(len(dimension)):
        dimension[i]=int(dimension[i])
    game1 = Game(dimension)
    game1.play()