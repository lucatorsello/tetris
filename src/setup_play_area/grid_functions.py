import pygame

from setup_shapes.generate_shape import convert_shape_format
from setup_shapes.shape import Piece


def create_grid(locked_positions={}) -> list:
    grid = [[(0, 0, 0) for x in range(10)] for x in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_positions:
                c = locked_positions[(j, i)]
                grid[i][j] = c
    return grid


def draw_grid(
    surface,
    row: int,
    column: int,
    top_left_x: int,
    top_left_y: int,
    game_width: int,
    game_height: int,
    grid: list,
):

    sx = top_left_x
    sy = top_left_y
    for i in range(row):
        pygame.draw.line(
            surface, (128, 128, 128), (sx, sy + i * 30), (sx + game_width, sy + i * 30)
        )  # horizontal lines
        for j in range(column):
            pygame.draw.line(
                surface,
                (128, 128, 128),
                (sx + j * 30, sy),
                (sx + j * 30, sy + game_height),
            )  #


def valid_space(shape: Piece, grid: list) -> bool:
    """Checks thats shape is in a valid position in the grid ,
    by comparing current shape grid xy and the grids xy.
    accepted_positions = values are only added if the tuple has value 000(empty)

    Args:
        shape (_type_): _description_
        grid (_type_): _description_

    Returns:
        boolean return -> returns true if its a vlid position for the shape to be in, returns false if its not
    """
    accepted_positions = [
        [(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)
    ]
    accepted_positions = [j for sub in accepted_positions for j in sub]
    formatted = convert_shape_format(shape)

    for position in formatted:
        if position not in accepted_positions:
            if position[1] > -1:
                return False

    return True
