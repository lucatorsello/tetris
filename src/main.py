import pygame
from setup_play_area.grid_functions import create_grid
from setup_play_area.window_funciton import draw_window

from setup_shapes.generate_shape import get_shape

pygame.font.init()

# GLOBALS VARS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
GAME_WIDTH = 300  # meaning 300 // 10 = 30 width per block
GAME_HEIGHT = 600  # meaning 600 // 20 = 20 height per block
BLOCK_SIZE = 30

top_left_x = (SCREEN_WIDTH - GAME_WIDTH) // 2
top_left_y = SCREEN_HEIGHT - GAME_HEIGHT


def valid_space(shape, grid):
    pass


def main(window):
    global grid

    locked_positions = {}  # (x,y):(255,0,0)
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0

    while run:
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
                    current_piece.rotation = (current_piece.rotation + 1) % len(
                        current_piece.shape
                    )
                    if not valid_space(current_piece, grid):
                        current_piece.rotation = (current_piece.rotation - 1) % len(
                            current_piece.shape
                        )

                if event.key == pygame.K_DOWN:
                    # move shape down
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1
        draw_window(
            window,
            top_left_x,
            top_left_y,
            GAME_WIDTH,
            GAME_HEIGHT,
            grid,
        )

        # Limit frame rate
        clock.tick(30)

        # Update the display
        pygame.display.flip()


window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

main(window=window)
