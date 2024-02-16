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

    surface.blit(label, (top_left_x + game_height / 2 - (label.get_width() / 2), 30))
    draw_grid(surface, top_left_x, top_left_y, game_width, game_height, grid)
    pygame.display.update()
