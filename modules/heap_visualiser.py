import pygame
import sys

from ui import *

def run(screen, clock):
    running = True

    back_button = pygame.Rect(30, 30, 140, 50)

    while running:
        screen.fill(BACKGROUND)

        draw_text(
            screen,
            "Heap Visualiser Module",
            48,
            BLACK,
            500,
            120
        )

        draw_button(
            screen,
            back_button,
            "Back",
            BLUE,
            LIGHT_BLUE
        )

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    running = False

        clock.tick(60)