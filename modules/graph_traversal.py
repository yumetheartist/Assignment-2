import pygame
import sys
from collections import deque

from ui import *

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5, 6],
    5: [2, 4, 7],
    6: [4],
    7: [5]
}

positions = {
    0: (250, 170),
    1: (150, 290),
    2: (380, 290),
    3: (90, 450),
    4: (240, 450),
    5: (420, 450),
    6: (620, 450),
    7: (560, 290)
}

selected_start = None

visited_nodes = []
current_node = None

algorithm = None

animation_index = 0
animation_timer = 0

message = "Select a start node"

running_algorithm = False

def bfs(start):
    visited = set()
    order = []

    queue = deque([start])

    visited.add(start)

    while queue:

        node = queue.popleft()

        order.append(node)

        for neighbor in graph[node]:

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order

def dfs(start):
    visited = set()
    order = []

    stack = [start]

    while stack:

        node = stack.pop()

        if node not in visited:

            visited.add(node)

            order.append(node)

            for neighbor in reversed(graph[node]):
                stack.append(neighbor)

    return order

def draw_graph(screen):

    for node in graph:

        for neighbor in graph[node]:

            x1, y1 = positions[node]
            x2, y2 = positions[neighbor]

            pygame.draw.line(
                screen,
                (120, 120, 120),
                (x1, y1),
                (x2, y2),
                4
            )

    for node, (x, y) in positions.items():

        color = BLUE

        if node in visited_nodes:
            color = (100, 200, 120)

        if node == current_node:
            color = RED

        if node == selected_start:
            color = (240, 180, 60)

        pygame.draw.circle(
            screen,
            color,
            (x, y),
            35
        )

        pygame.draw.circle(
            screen,
            BLACK,
            (x, y),
            35,
            3
        )

        draw_text(
            screen,
            str(node),
            28,
            WHITE,
            x,
            y
        )

def reset_graph():
    global selected_start
    global visited_nodes
    global current_node
    global algorithm
    global animation_index
    global animation_timer
    global message
    global running_algorithm

    selected_start = None

    visited_nodes = []

    current_node = None

    algorithm = None

    animation_index = 0
    animation_timer = 0

    running_algorithm = False

    message = "Graph reset"

def run(screen, clock):

    global selected_start
    global visited_nodes
    global current_node
    global algorithm
    global animation_index
    global animation_timer
    global message
    global running_algorithm

    reset_graph()

    running = True

    back_button = pygame.Rect(30, 25, 120, 45)

    bfs_button = pygame.Rect(260, 650, 180, 50)

    dfs_button = pygame.Rect(500, 650, 180, 50)

    reset_button = pygame.Rect(740, 650, 180, 50)

    while running:

        screen.fill(BACKGROUND)

        draw_text(
            screen,
            "Graph Traversal Visualiser",
            48,
            BLACK,
            600,
            45
        )

        draw_text(
            screen,
            "Click a node to choose the starting point",
            24,
            BLACK,
            600,
            95
        )

        draw_graph(screen)

        pygame.draw.rect(
            screen,
            (220, 220, 220),
            (120, 570, 960, 40),
            border_radius=10
        )

        draw_text(
            screen,
            message,
            22,
            BLACK,
            600,
            590
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
            bfs_button,
            "Run BFS",
            (90, 170, 120),
            (120, 200, 150)
        )

        draw_button(
            screen,
            dfs_button,
            "Run DFS",
            (200, 120, 70),
            (220, 150, 100)
        )

        draw_button(
            screen,
            reset_button,
            "Reset",
            RED,
            LIGHT_RED
        )

        if running_algorithm:

            animation_timer += 1

            if animation_timer >= 25:

                animation_timer = 0

                if animation_index < len(algorithm):

                    current_node = algorithm[animation_index]

                    visited_nodes.append(current_node)

                    message = f"Visiting node {current_node}"

                    animation_index += 1

                else:

                    running_algorithm = False

                    current_node = None

                    message = "Traversal completed"

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

                if reset_button.collidepoint(pos):
                    reset_graph()

                if not running_algorithm:

                    for node, (x, y) in positions.items():

                        distance = ((pos[0] - x) ** 2 + (pos[1] - y) ** 2) ** 0.5

                        if distance <= 35:

                            selected_start = node

                            message = f"Selected node {node} as start"

                if bfs_button.collidepoint(pos):

                    if selected_start is not None:

                        algorithm = bfs(selected_start)

                        visited_nodes = []

                        animation_index = 0

                        running_algorithm = True

                        message = "Running Breadth First Search"

                if dfs_button.collidepoint(pos):

                    if selected_start is not None:

                        algorithm = dfs(selected_start)

                        visited_nodes = []

                        animation_index = 0

                        running_algorithm = True

                        message = "Running Depth First Search"

        clock.tick(60)