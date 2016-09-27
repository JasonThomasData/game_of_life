from application import squares
import numpy as np

class Board(object):
    '''
    In the simulation, this is the board that all squares sit on top of.
    This class makes the naive assumption that all imported lines are the same length.
    '''

    def __init__(self, data_from_file):
        self.side_buffer_size = 10
        self.high = len(data_from_file) + (self.side_buffer_size * 2)
        self.wide = len(data_from_file[0]) + (self.side_buffer_size * 2)
        self.data = self.make_board(data_from_file)

    def add_buffer(self, data_from_file):
        '''
        The files taken from the online site are depictions of minimal shapes, but often
        lack the required space to do their functions correctly in isolation. This function
        adds a buffer to the uploaded data before the board is created.
        '''
        
        side_buffer = '.' * self.side_buffer_size
        
        data_with_side_buffers = []

        for i, row in enumerate(data_from_file):
            
            row_with_buffers = ''.join([side_buffer, row, side_buffer])
            data_with_side_buffers.append(row_with_buffers)

            print(row)
            print(row_with_buffers)

        top_bottom_buffer = ['.' * self.wide] * self.side_buffer_size

        data_with_buffers = sum([top_bottom_buffer, data_with_side_buffers, top_bottom_buffer], [])

        print(data_with_buffers)

        return data_with_buffers

    def make_board(self, data_from_file):
        '''
        Iterates through the data from the file upload and converts each list element to an
        object, each with x, y and is_alive properties.
        '''

        data_with_buffers = self.add_buffer(data_from_file)

        squares_on_board = []

        for i, row in enumerate(data_with_buffers):
            squares_in_this_row =  []

            for j, elem in enumerate(row):
                if elem == 'O':
                    is_alive = True
                else:
                    is_alive = False
                new_square = squares.Square(i, j, is_alive)
                squares_in_this_row.append(new_square)
            
            squares_on_board.append(squares_in_this_row)

        return np.array(squares_on_board)

