import pygame
from setup_play_area.grid_functions import draw_grid


def draw_window(
    surface,
    top_left_x: int,
    top_left_y: int,
    game_width: int,
    game_height: int,
    grid: list,
    score=0,
    last_score=0,
):
    surface.fill((0, 100, 150))
    # Tetris Title
    font = pygame.font.SysFont("comicsans", 60)
    label = font.render("TETRIS", 1, (255, 255, 255))
    surface.blit(label, (top_left_x + game_width / 2 - (label.get_width() / 2), 20))
    # score
    font = pygame.font.SysFont("comicsans", 30)
    score = font.render("Score: " + str(score), 1, (255, 255, 255))
    surface.blit(
        score,
        (top_left_x - 200, top_left_y + 150),
    )
    max_score = font.render("High Score: " + f"{last_score}", 1, (255, 255, 255))
    surface.blit(max_score, (top_left_x - 200, top_left_y + 200))

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
        (0, 200, 0),
        (top_left_x, top_left_y, game_width, game_height),
        5,
    )
    draw_grid(
        surface,
        20,
        10,
        top_left_x,
        top_left_y,
        game_width,
        game_height,
    )


def draw_next_shape(shape, surface, top_left_x, top_left_y, game_width, game_height):
    font = pygame.font.SysFont("comicsans", 30)
    label = font.render("Next Shape", 1, (255, 255, 255))

    sx = top_left_x + game_width + 50
    sy = top_left_y + game_height / 2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == "0":
                pygame.draw.rect(
                    surface, shape.color, (sx + j * 30, sy + i * 30, 30, 30), 0
                )
    pygame.draw.rect(
        surface,
        (0, 200, 0),
        (sx, sy, 30 * 4, 30 * 4),
        5,
    )
    draw_grid(
        surface=surface,
        row=4,
        column=4,
        top_left_x=sx,
        top_left_y=sy,
        game_width=30 * 4,
        game_height=30 * 4,
    )
    surface.blit(label, (sx, sy - 40))
