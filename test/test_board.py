#! usr/bin/env python3

import os
import sys
import unittest

# Here we're moving the context into the parent folder
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)

from application import board
from application import squares

class TestBufferAdded(unittest.TestCase):
    '''
    Test the board is initialised with a buffer.
    '''

    def test(self):

        data_from_file = [
            '.O.',
            'O..',
            'OOO'
        ]

        game_board = board.Board(data_from_file)

        # These are set upon __init__, so we're mocking these
        game_board.side_buffer_size = 5
        game_board.high = len(data_from_file) + (game_board.side_buffer_size * 2)
        game_board.wide = len(data_from_file[0]) + (game_board.side_buffer_size * 2)

        data_with_buffers = game_board.add_buffer(data_from_file)

        assert data_with_buffers[0] == '.............'
        assert len(data_with_buffers) == 13


class TestDataToBoard(unittest.TestCase):
    '''
    Test the board is initiatialised, converting raw data to a MD array of squares.
    '''

    def test(self):

        data_from_file = [
            '.O.',
            'O..',
            'OOO'
        ]
        
        game_board = board.Board(data_from_file)

        # These are set upon __init__, so we're mocking these
        game_board.side_buffer_size = 5
        game_board.high = len(data_from_file) + (game_board.side_buffer_size * 2)
        game_board.wide = len(data_from_file[0]) + (game_board.side_buffer_size * 2)

        board_data = game_board.make_board(data_from_file)

        assert board_data[0][0].is_alive == False
        assert board_data[6][5].is_alive == True
        assert board_data[6][6].is_alive == False
        assert board_data[7][6].is_alive == True

if __name__ == '__main__':
    unittest.main()

