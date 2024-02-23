import pygame

from setup_play_area.grid_functions import valid_space


def handle_keypress(current_piece, grid, run_game: bool):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
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

            elif event.key == pygame.K_DOWN:
                # move shape down
                current_piece.y += 1
                if not valid_space(current_piece, grid):
                    current_piece.y -= 1

    return True
