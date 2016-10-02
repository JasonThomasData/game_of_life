from tkinter import Tk, Canvas

class Animation(object):
    '''
    This class handles the visual representation of the game. This creates canvas shapes that are
    attached to the squares on the board, which allows us to loop through all squares on the board
    and update a property of each square - the canvas shape - to change how that square appears.
    '''

    def __init__(self, game, board):
        self.milliseconds_between_frames = 200
        self.square_width = 10
        self.canvas_width = board.wide * self.square_width
        self.canvas_height = board.high * self.square_width
        self.anim_tk = Tk()
        self.canvas = Canvas(self.anim_tk, width=self.canvas_width, height=self.canvas_height)
        self.draw_squares(board.data)
        self.canvas.pack()
        self.game_loop(game)
        self.anim_tk.mainloop()

    def draw_squares(self, board_data):
        '''
        Creates the canvas_shape property of each square. Each square's canvas_shape is a space on
        the canvas. This allows us to keep the knowledge of a square on the board, and a square
        on the canvas, in the one place. That way we can loop through each square on the board and
        not have to then find the corresponding shapes.
        '''

        for i, row in enumerate(board_data):
            for j, square in enumerate(row):
                y_start = i * self.square_width
                y_finish = (i + 1) * self.square_width
                x_start = j * self.square_width
                x_finish = (j + 1) * self.square_width
                square.canvas_shape = self.canvas.create_rectangle(x_start, y_start, x_finish, y_finish, fill='white', width=0)

    def update_canvas(self, board_data):
        '''
        For each square.canvas_shape, update its colour according to whether it is alive or not.
        '''

        for i, row in enumerate(board_data):
            for j, square in enumerate(row):
                if square.is_alive == True:
                    colour = 'black'
                else:
                    colour = 'white'
                self.canvas.itemconfig(square.canvas_shape, fill=colour)

    def game_loop(self, game):
        '''
        Updating the game loop should be the main game class' responsibility, but Tkinter has a 
        method `.after()`, which does something that looks like recursion (it's not recursion).
        So this is where the game loop occurs. This is more neat than creating a sleep counter
        in the main class and then updating the canvas that way.
        '''

        game.update_board()
        board_data = game.board.data
        self.update_canvas(board_data)
        self.anim_tk.after(self.milliseconds_between_frames, self.game_loop, game)

