import pygame

WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
BLUE = (70, 130, 180)
LIGHT_BLUE = (100, 170, 220)
RED = (200, 70, 70)
LIGHT_RED = (230, 90, 90)
BACKGROUND = (240, 244, 250)

def get_font(size):
    return pygame.font.SysFont("arial", size)

def draw_text(screen, text, size, color, x, y):
    font = get_font(size)

    surface = font.render(text, True, color)

    rect = surface.get_rect(center=(x, y))

    screen.blit(surface, rect)

def draw_button(screen, rect, text, base_color, hover_color):
    mouse_pos = pygame.mouse.get_pos()

    color = hover_color if rect.collidepoint(mouse_pos) else base_color

    pygame.draw.rect(screen, color, rect, border_radius=12)

    draw_text(
        screen,
        text,
        32,
        WHITE,
        rect.centerx,
        rect.centery
    )