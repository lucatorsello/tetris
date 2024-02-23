import pygame
from gameplay_rules.loss import check_lost
from input_handler import handle_keypress
from main_readability import place_shape_on_grid, update_locked_positions
from setup_play_area.grid_functions import create_grid, valid_space
from setup_play_area.window_funciton import draw_next_shape, draw_window

from setup_shapes.generate_shape import convert_shape_format, get_shape
from gameplay_rules.delete_row import clear_rows

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

        shape_position = convert_shape_format(current_piece)
        run = handle_keypress(current_piece, grid, run)
        place_shape_on_grid(shape_position, grid, current_piece)
        if change_piece:
            update_locked_positions(shape_position, locked_positions, current_piece)
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            clear_rows(grid, locked_positions)
        draw_window(
            window,
            top_left_x,
            top_left_y,
            GAME_WIDTH,
            GAME_HEIGHT,
            grid,
        )
        draw_next_shape(
            next_piece,
            window,
            top_left_x,
            top_left_y,
            GAME_WIDTH,
            GAME_HEIGHT,
        )
        pygame.display.update()

        if check_lost(locked_positions):
            run = False


window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

main(window=window)
