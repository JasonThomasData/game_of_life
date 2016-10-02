#! usr/bin/env python3

import sys
from application import file_reader
from application import squares
from application import board
from application import game

try:
    available_modes = ['animate', 'get_cycles']
    selected_mode = sys.argv[1]
    if selected_mode not in available_modes:
        raise ValueError
except (IndexError, ValueError) as err:
    message = 'You must enter a mode, either "animate" or "get_cycles"'
    print(message)
    sys.exit()

try:
    file_name = sys.argv[2]
except IndexError:
    message = 'You must enter a file name, like "maps/glider.cells"'
    print(message)
    sys.exit()

try:
    data_from_file = file_reader.get_board_data(file_name)
except FileNotFoundError:
    message = 'File not found. Enter a file path like "maps/glider.cells"'
    print(message)
    sys.exit()

game_of_life = game.Game(data_from_file)

if selected_mode == 'animate':
    game_of_life.animate_simulation()
else:
    cycles_to_complete = game_of_life.run_simulation()
    print(cycles_to_complete)
