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


class TestSquaresEvaluate_1(unittest.TestCase):
    '''
    Once neighbours are counted, loop through and evaluate whether each
    square will live or die.
    '''

    def test(self):
        '''
        Test data looks like, all will survive

            O.
            OO
        
        '''

        mock_data_from_file = ['..']

        simulation = game.Game(mock_data_from_file)

        s_0_0 = squares.Square(0, 0, True)
        s_0_1 = squares.Square(0, 1, False)
        s_1_0 = squares.Square(1, 0, True)
        s_1_1 = squares.Square(1, 1, True)

        board_data = [
            [s_0_0, s_0_1],
            [s_1_0, s_1_1]
        ]

        simulation.squares_evaluate(board_data)

        assert board_data[0][0].will_be_alive == True
        assert board_data[0][1].will_be_alive == True
        assert board_data[1][0].will_be_alive == True
        assert board_data[1][1].will_be_alive == True


class TestSquaresEvaluate_2(unittest.TestCase):
    '''
    Once neighbours are counted, loop through and evaluate whether each
    square will live or die.
    '''

    def test(self):
        '''
        Test data looks like

            .O.
            O..
            OOO
        
        '''

        mock_data_from_file = ['..']

        simulation = game.Game(mock_data_from_file)

        s_0_0 = squares.Square(0, 0, False)
        s_0_1 = squares.Square(0, 1, True)
        s_0_2 = squares.Square(0, 2, False)
        s_1_0 = squares.Square(1, 0, True)
        s_1_1 = squares.Square(1, 1, False)
        s_1_2 = squares.Square(1, 2, False)
        s_2_0 = squares.Square(2, 0, True)
        s_2_1 = squares.Square(2, 1, True)
        s_2_2 = squares.Square(2, 2, True)

        board_data = [
            [s_0_0, s_0_1, s_0_2],
            [s_1_0, s_1_1, s_1_2],
            [s_2_0, s_2_1, s_2_2]
        ]

        simulation.squares_evaluate(board_data)
       
        assert board_data[0][0].will_be_alive == False
        assert board_data[0][1].will_be_alive == False
        assert board_data[0][2].will_be_alive == False
        
        assert board_data[1][0].will_be_alive == True
        assert board_data[1][1].will_be_alive == False
        assert board_data[1][2].will_be_alive == True

        assert board_data[2][0].will_be_alive == True
        assert board_data[2][1].will_be_alive == True
        assert board_data[2][2].will_be_alive == False

class TestSquaresChangeStates(unittest.TestCase):
    '''
    Once neighbours are evaluated in terms of life or death, loop through the squares
    and change their states.
    '''

    def test(self):
        '''
        Test data looks like, all will die

            .O
            O.

        '''

        mock_data_from_file = ['..']

        simulation = game.Game(mock_data_from_file)

        s_0_0 = squares.Square(0, 0, False)
        s_0_1 = squares.Square(0, 1, True)
        s_1_0 = squares.Square(1, 0, True)
        s_1_1 = squares.Square(1, 1, False)

        board_data = [
            [s_0_0, s_0_1],
            [s_1_0, s_1_1]
        ]

        for row in board_data:
            for square in row:
                square.will_be_alive = False

        simulation.squares_change_states(board_data)
 
        assert board_data[0][0].is_alive == False
        assert board_data[0][1].is_alive == False
        assert board_data[1][0].is_alive == False
        assert board_data[1][1].is_alive == False

if __name__ == '__main__':
    unittest.main()
