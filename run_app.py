#! usr/bin/env python3

import sys
from application import file_reader
from application import squares
from application import board
from application import game

try:
    file_name = sys.argv[1]
except IndexError:
    print('You must enter a file name, like maps/map.txt')
    sys.exit()

try:
    data_from_file = file_reader.get_board_data(file_name)
except FileNotFoundError:
    print('File not found')
    sys.exit()

game_of_life = game.Game(data_from_file)
game_of_life.run_simulation()

