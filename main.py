import pygame
import sys

from ui import *

from modules import data_structures
from modules import sorting
from modules import graph_traversal
from modules import pathfinding

pygame.init()

WIDTH = 1280
HEIGHT = 820

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("DSA Explorer and Visualiser")

clock = pygame.time.Clock()

cards = {
    "Data Structures": pygame.Rect(120, 180, 420, 180),
    "Sorting Visualiser": pygame.Rect(660, 180, 420, 180),
    "Graph Visualiser": pygame.Rect(120, 420, 420, 180),
    "Puzzle Challenges": pygame.Rect(660, 420, 420, 180)
}

exit_button = pygame.Rect(1000, 30, 150, 50)

descriptions = {
    "Data Structures":
        "Stack, Queue, Linked List and BST visualisation",

    "Sorting Visualiser":
        "Bubble Sort, Selection Sort and Merge Sort",

    "Graph Visualiser":
        "BFS, DFS and graph traversal animations",

    "Puzzle Challenges":
        "Pathfinding and algorithm-based puzzles"
}

card_colors = {
    "Data Structures": ((70, 130, 180), (100, 170, 220)),
    "Sorting Visualiser": ((200, 120, 70), (220, 150, 100)),
    "Graph Visualiser": ((120, 160, 90), (145, 190, 110)),
    "Puzzle Challenges": ((170, 120, 210), (190, 145, 230))
}

def draw_card(title, rect):
    mouse_pos = pygame.mouse.get_pos()

    base_color, hover_color = card_colors[title]

    color = hover_color if rect.collidepoint(mouse_pos) else base_color

    pygame.draw.rect(
        screen,
        color,
        rect,
        border_radius=22
    )

    draw_text(
        screen,
        title,
        40,
        WHITE,
        rect.centerx,
        rect.y + 55
    )

    draw_text(
        screen,
        descriptions[title],
        22,
        WHITE,
        rect.centerx,
        rect.y + 120
    )

def draw_menu():
    screen.fill((240, 244, 250))

    draw_text(
        screen,
        "DSA Explorer and Visualiser",
        54,
        BLACK,
        WIDTH // 2,
        70
    )

    draw_text(
        screen,
        "Interactive Learning of Data Structures and Algorithms",
        24,
        BLACK,
        WIDTH // 2,
        115
    )

    for title, rect in cards.items():
        draw_card(title, rect)

    draw_button(
        screen,
        exit_button,
        "Exit",
        RED,
        LIGHT_RED
    )

    pygame.display.update()

def main():
    running = True

    while running:
        draw_menu()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                pos = event.pos

                if exit_button.collidepoint(pos):
                    running = False

                if cards["Data Structures"].collidepoint(pos):
                    data_structures.run(screen, clock)

                if cards["Sorting Visualiser"].collidepoint(pos):
                    sorting.run(screen, clock)

                if cards["Graph Visualiser"].collidepoint(pos):
                    graph_traversal.run(screen, clock)

                if cards["Puzzle Challenges"].collidepoint(pos):
                    pathfinding.run(screen, clock)

        clock.tick(60)

    pygame.quit()
    sys.exit()

main()