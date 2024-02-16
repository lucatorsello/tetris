import pygame
from gameplay_rules.loss import check_lost
from setup_play_area.grid_functions import create_grid, valid_space
from setup_play_area.window_funciton import draw_window

from setup_shapes.generate_shape import convert_shape_format, get_shape

pygame.font.init()

# GLOBALS VARS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
GAME_WIDTH = 300  # meaning 300 // 10 = 30 width per block
GAME_HEIGHT = 600  # meaning 600 // 20 = 20 height per block
BLOCK_SIZE = 30

top_left_x = (SCREEN_WIDTH - GAME_WIDTH) // 2
top_left_y = SCREEN_HEIGHT - GAME_HEIGHT


def main(window):
    locked_positions = {}  # (x,y):(255,0,0)
    grid = create_grid(locked_positions)
    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0

    while run:
        fall_speed = 0.27
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()
        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not (valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1

                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                elif event.key == pygame.K_UP:
                    # rotate shape
                    current_piece.rotation = current_piece.rotation + 1 % len(
                        current_piece.shape
                    )
                    if not valid_space(current_piece, grid):
                        current_piece.rotation = current_piece.rotation - 1 % len(
                            current_piece.shape
                        )

                if event.key == pygame.K_DOWN:
                    # move shape down
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1

        shape_pos = convert_shape_format(current_piece)

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False

        draw_window(
            window,
            top_left_x,
            top_left_y,
            GAME_WIDTH,
            GAME_HEIGHT,
            grid,
        )

        if check_lost(locked_positions):
            run = False


window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

main(window=window)
