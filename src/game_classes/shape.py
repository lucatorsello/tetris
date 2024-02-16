from src.graphics.shapes import shapes, shape_colors


class Piece(object):
    y_height = 20
    x_width = 10

    def __init__(self, column: int, row: int, shape: list):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0  # number from 0-3
