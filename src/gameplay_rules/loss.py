import pygame

font_file = "../tetris/src/Minecraft.ttf"


def check_lost(positions):
    for position in positions:
        x, y = position
        if y < 1:
            return True
    return False


def draw_text_middle(surface, text, size, color, screen_width, screen_height):
    font = pygame.font.Font(font_file, size)
    label = font.render(text, 1, color)
    label_rect = label.get_rect(center=(screen_width / 2, screen_height / 2))

    surface.blit(label, label_rect)
