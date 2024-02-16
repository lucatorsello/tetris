import random
from game_classes.shape import Piece
from setup_shapes.graphics import shapes


def get_shape():
    return Piece(5, 0, random.choice(shapes))
