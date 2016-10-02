from application import board
from application import animation
from time import sleep
from sys import stdout
from itertools import product

class Game(object):

    '''
    This is where the simulation will occur, although the game loop is housed in the animation
    class.
    '''

    def __init__(self, data_from_file):
        self.board = board.Board(data_from_file)
        self.simulation_going = False
        self.cycles = 0
        self.max_cycles = 300

    def count_my_neighbours(self, square, board_data):
        '''
        Considering each square, check to see how many living neighbours it has.
        '''
        
        neighbour_count = 0

        for i, j in product(range(-1, 2), range(-1, 2)): 
            if i == 0 and j == 0:
                # This square, relative to itself, not for comparing
                continue
            x_check = j + square.x
            y_check = i + square.y
            if x_check < 0 or y_check < 0:
                continue
            try:
                neighbour = board_data[x_check][y_check]
                if neighbour.is_alive == True:
                    neighbour_count += 1
            except IndexError:
                continue

        return neighbour_count

    def squares_evaluate(self, board_data):
        '''
        Cycle through all squares, call function to count each square's neighbours, then apply
        rules for game.

        Those rules are:
        - Living square with fewer than two neighbours dies.
        - Living square with more than three neighbours dies.
        - Not living square with three neigbours born.
        '''

        for _i, row in enumerate(board_data):
            for _j, square in enumerate(row):
                square.neighbour_count = self.count_my_neighbours(square, board_data)
                if square.is_alive == True and square.neighbour_count == 2:
                    square.will_be_alive = True
                elif square.neighbour_count == 3:
                    square.will_be_alive = True
                else:
                    square.will_be_alive = False

    def squares_change_states(self, board_data):
        '''
        When all squares have had neighbour counts, then we can change each square.
        The neighbour count of all squares are reset, ready for next game loop.
        The continue_simulation is used in run_simulation, but in the animate_simulation
        it's ineffective.
        '''

        for _i, row in enumerate(board_data):
            for _j, square in enumerate(row):

                if square.is_alive != square.will_be_alive:
                    self.continue_simulation = True

                square.is_alive = square.will_be_alive
                square.neighbour_count = 0

    def update_board(self):
        '''
        This will be called from the self.animation object, since Tkinter will handle the game loop.
        '''

        board_data = self.board.data
        self.squares_evaluate(board_data)
        self.squares_change_states(board_data)

    def animate_simulation(self):
        '''
        Unit testing demands this is a seperate function, since the animation occurs when it
        is initialised, so let's call this from the run_app file.
        '''

        self.game_animation = animation.Animation(self, self.board)

    def run_simulation(self):
        '''
        Rather than animate the results, run the simulation until there are no more
        cells evolving. After the update_board() function is complete, all squares have been
        evaluated and if any single square has changed its is_alive property, then the loop
        continues. Otherwise the loop stops, and we've found the end state of this sequence.
        '''

        while True:
            self.continue_simulation = False
            self.cycles += 1
            self.update_board()
            if self.continue_simulation == False:
                break
            elif self.cycles >= self.max_cycles:
                break

        return self.cycles
