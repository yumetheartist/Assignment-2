import pygame
import sys
import random
import heapq

from ui import *

ROWS = 9
COLS = 13

CELL_SIZE = 58

GRID_X = 250
GRID_Y = 120

grid = []

visited_nodes = []
path_nodes = []

message = "Generate a grid and run pathfinding"

path_cost = 0

start = (0, 0)
end = (ROWS - 1, COLS - 1)

def generate_grid():

    global grid
    global visited_nodes
    global path_nodes
    global message
    global path_cost

    visited_nodes = []
    path_nodes = []

    path_cost = 0

    grid = []

    for row in range(ROWS):

        current_row = []

        for col in range(COLS):

            value = random.randint(1, 9)

            blocked = random.random() < 0.18

            if (row, col) == start:
                blocked = False

            if (row, col) == end:
                blocked = False

            current_row.append({
                "value": value,
                "blocked": blocked
            })

        grid.append(current_row)

    message = "Generated new weighted grid"

def draw_grid(screen):

    for row in range(ROWS):

        for col in range(COLS):

            x = GRID_X + col * CELL_SIZE
            y = GRID_Y + row * CELL_SIZE

            cell = grid[row][col]

            rect = pygame.Rect(
                x,
                y,
                CELL_SIZE - 3,
                CELL_SIZE - 3
            )

            color = (245, 245, 245)

            if cell["blocked"]:
                color = (45, 45, 45)

            if (row, col) in visited_nodes:
                color = (120, 180, 255)

            if (row, col) in path_nodes:
                color = (120, 220, 120)

            if (row, col) == start:
                color = (70, 140, 255)

            if (row, col) == end:
                color = (255, 110, 110)

            pygame.draw.rect(
                screen,
                color,
                rect,
                border_radius=8
            )

            pygame.draw.rect(
                screen,
                BLACK,
                rect,
                1,
                border_radius=8
            )

            if not cell["blocked"]:

                draw_text(
                    screen,
                    str(cell["value"]),
                    20,
                    BLACK,
                    rect.centerx,
                    rect.centery
                )

def get_neighbors(row, col):

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    neighbors = []

    for dr, dc in directions:

        nr = row + dr
        nc = col + dc

        if 0 <= nr < ROWS and 0 <= nc < COLS:

            if not grid[nr][nc]["blocked"]:
                neighbors.append((nr, nc))

    return neighbors

def dijkstra():

    pq = []

    heapq.heappush(pq, (0, start))

    distances = {
        start: 0
    }

    previous = {}

    visited_order = []

    while pq:

        current_distance, current = heapq.heappop(pq)

        if current in visited_order:
            continue

        visited_order.append(current)

        if current == end:
            break

        for neighbor in get_neighbors(current[0], current[1]):

            weight = grid[neighbor[0]][neighbor[1]]["value"]

            distance = current_distance + weight

            if neighbor not in distances or distance < distances[neighbor]:

                distances[neighbor] = distance

                previous[neighbor] = current

                heapq.heappush(
                    pq,
                    (distance, neighbor)
                )

    path = []

    current = end

    if current in previous or current == start:

        while current != start:

            path.append(current)

            current = previous[current]

        path.append(start)

        path.reverse()

    return visited_order, path, distances.get(end, 0)

def run(screen, clock):

    global visited_nodes
    global path_nodes
    global message
    global path_cost

    generate_grid()

    running = True

    back_button = pygame.Rect(30, 25, 130, 50)

    run_button = pygame.Rect(300, 730, 240, 55)

    generate_button = pygame.Rect(700, 730, 300, 55)

    while running:

        screen.fill((235, 240, 248))

        draw_text(
            screen,
            "Pathfinding Challenge",
            48,
            BLACK,
            640,
            40
        )

        draw_text(
            screen,
            "Weighted Grid using Dijkstra's Algorithm",
            24,
            BLACK,
            640,
            82
        )

        pygame.draw.rect(
            screen,
            (225, 230, 240),
            (220, 105, 840, 540),
            border_radius=20
        )

        draw_grid(screen)

        pygame.draw.rect(
            screen,
            (220, 220, 220),
            (250, 655, 780, 45),
            border_radius=12
        )

        draw_text(
            screen,
            message,
            24,
            BLACK,
            640,
            678
        )

        pygame.draw.rect(
            screen,
            (235, 235, 235),
            (450, 705, 380, 35),
            border_radius=10
        )

        draw_text(
            screen,
            f"Shortest Path Cost: {path_cost}",
            24,
            BLACK,
            640,
            722
        )

        draw_button(
            screen,
            back_button,
            "Back",
            BLUE,
            LIGHT_BLUE
        )

        draw_button(
            screen,
            run_button,
            "Run Dijkstra",
            (90, 170, 120),
            (120, 200, 150)
        )

        draw_button(
            screen,
            generate_button,
            "Generate New Grid",
            (170, 120, 210),
            (190, 145, 230)
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

                pos = event.pos

                if back_button.collidepoint(pos):
                    running = False

                if generate_button.collidepoint(pos):
                    generate_grid()

                if run_button.collidepoint(pos):

                    visited_nodes, path_nodes, path_cost = dijkstra()

                    if path_nodes:
                        message = "Shortest path found using Dijkstra's Algorithm"
                    else:
                        message = "No valid path found"

        clock.tick(60)