import pygame


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
    top_left_x: int,
    top_left_y: int,
    game_width: int,
    game_height: int,
    grid: list,
):

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(
                surface,
                grid[i][j],
                (top_left_x + j * 30, top_left_y + i * 30, 30, 30),
                0,
            )

    pygame.draw.rect(
        surface, (255, 0, 0), (top_left_x, top_left_y, game_width, game_height), 5
    )
