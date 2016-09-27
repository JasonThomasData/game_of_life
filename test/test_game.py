#! usr/bin/env python3

import os
import sys
import unittest
from time import sleep
from sys import stdout
from itertools import product

# Here we're moving the context into the parent folder
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)

from application import board
from application import animation
from application import game
from application import squares

class TestCountNeighbours(unittest.TestCase):
    '''
    Test this function counts the neighbours for each cell.
    '''

    def test(self):
        '''
        Test data looks like

            .O
            OO
        
        '''

        mock_data_from_file = ['..']

        simulation = game.Game(mock_data_from_file)

        s_0_0 = squares.Square(0, 0, False)
        s_0_1 = squares.Square(0, 1, True)
        s_1_0 = squares.Square(1, 0, True)
        s_1_1 = squares.Square(1, 1, True)
        
        board_data = [
            [s_0_0, s_0_1],
            [s_1_0, s_1_1]
        ]

        for row in board_data:
            for square in row:
                square.neighbour_count = simulation.count_my_neighbours(square, board_data)
           
        assert board_data[0][0].neighbour_count == 3
        assert board_data[0][1].neighbour_count == 2
        assert board_data[1][0].neighbour_count == 2
        assert board_data[1][1].neighbour_count == 2


if __name__ == '__main__':
    unittest.main()
