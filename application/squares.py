class Square(object):
    '''
    Each square on the board will persist even when dead. Dead squares will appear as white,
    and can come back to life. Squares are pushed to a Numpy array in the board class.
    Each square has a canvas_shape property, which is the canvas element to update the colour
    of.
    '''

    def __init__(self, x, y, is_alive):
        self.x = x
        self.y = y
        self.is_alive = is_alive
        self.will__be_alive = is_alive
        self.neighbour_count = 0
        self.canvas_shape = None

