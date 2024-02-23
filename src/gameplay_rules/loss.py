import pygame


def check_lost(positions):
    for position in positions:
        x, y = position
        if y < 1:
            return True
    return False


def draw_text_middle(
    surface, text, size, color, top_left_x, top_left_y, game_width, game_height
):
    font = pygame.font.SysFont("comicsans", size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(
        label,
        (
            top_left_x + game_width / 2 - (label.get_width() / 2),
            top_left_y + game_height / 2 - label.get_height() / 2,
        ),
    )
