import pygame
from setup_play_area.grid_functions import draw_grid


def draw_window(
    surface,
    top_left_x: int,
    top_left_y: int,
    game_width: int,
    game_height: int,
    grid: list,
):
    surface.fill((0, 0, 0))
    # Tetris Title
    font = pygame.font.SysFont("comicsans", 60)
    label = font.render("TETRIS", 1, (255, 255, 255))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(
                surface,
                grid[i][j],
                (top_left_x + j * 30, top_left_y + i * 30, 30, 30),
                0,
            )

    pygame.draw.rect(
        surface,
        (255, 0, 0),
        (top_left_x, top_left_y, game_width, game_height),
        5,
    )
    surface.blit(label, (top_left_x + game_width / 2 - (label.get_width() / 2), 30))
    draw_grid(
        surface,
        20,
        10,
        top_left_x,
        top_left_y,
        game_width,
        game_height,
        grid,
    )
    pygame.display.update()
