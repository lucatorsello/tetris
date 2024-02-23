import pygame
from gameplay_rules.loss import check_lost, draw_text_middle
from input_handler import handle_keypress
from main_readability import place_shape_on_grid, update_locked_positions
from setup_play_area.grid_functions import create_grid, valid_space
from setup_play_area.window_funciton import draw_next_shape, draw_window

from setup_shapes.generate_shape import convert_shape_format, get_shape
from gameplay_rules.delete_row import clear_rows
from setup_play_area.score import max_score, update_score

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
    level_time = 0
    score = 0
    last_score = max_score()
    while run:
        level_time += clock.get_rawtime()
        if level_time / 1000 > 5:
            level_time = 0
            if level_time > 0.12:
                level_time -= 0.005
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
        if score > last_score:
            last_score = score
        shape_position = convert_shape_format(current_piece)
        run = handle_keypress(current_piece, grid, run)
        place_shape_on_grid(shape_position, grid, current_piece)
        if change_piece:
            update_locked_positions(shape_position, locked_positions, current_piece)
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            score += clear_rows(grid, locked_positions) * 10
        draw_window(
            window,
            top_left_x,
            top_left_y,
            GAME_WIDTH,
            GAME_HEIGHT,
            grid,
            score,
            last_score,
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
            draw_text_middle(
                window,
                "YOU LOST!",
                80,
                (255, 0, 0),
                screen_height=SCREEN_HEIGHT,
                screen_width=SCREEN_WIDTH,
            )
            pygame.display.update()
            pygame.time.delay(1500)
            run = False
            update_score(score)
            run = False


def main_menu(window):
    run = True
    while run:
        window.fill((0, 0, 0))
        draw_text_middle(
            window,
            "Press Any Key To Play",
            40,
            (255, 255, 255),
            screen_height=SCREEN_HEIGHT,
            screen_width=SCREEN_WIDTH,
        )
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main(window=window)

    pygame.display.quit()


window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")
main_menu(window=window)
