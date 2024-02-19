import random
from setup_shapes.shape import Piece
from setup_shapes.graphics import shapes


def get_shape():
    return Piece(5, 0, random.choice(shapes))


def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == "0":
                positions.append((shape.x + j, shape.y + i))

    for i, position in enumerate(positions):
        positions[i] = (position[0] - 2, position[1] - 4)

    return positions
