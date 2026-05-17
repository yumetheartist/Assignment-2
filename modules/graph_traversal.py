import pygame
import sys
from collections import deque

from ui import *

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F", "G"],
    "F": ["C", "E", "H"],
    "G": ["E"],
    "H": ["F"]
}

positions = {
    "A": (280, 160),
    "B": (160, 300),
    "C": (430, 300),
    "D": (110, 500),
    "E": (300, 500),
    "F": (500, 500),
    "G": (700, 500),
    "H": (640, 300)
}

selected_start = None

visited_nodes = []

current_node = None

algorithm = []

path_edges = []

message = "Select a starting node"

running_algorithm = False

animation_index = 0

animation_timer = 0

def bfs(start):

    visited = set()

    queue = deque([start])

    order = []

    edges = []

    visited.add(start)

    while queue:

        node = queue.popleft()

        order.append(node)

        for neighbor in graph[node]:

            if neighbor not in visited:

                visited.add(neighbor)

                queue.append(neighbor)

                edges.append((node, neighbor))

    return order, edges

def dfs(start):

    visited = set()

    stack = [start]

    order = []

    edges = []

    while stack:

        node = stack.pop()

        if node not in visited:

            visited.add(node)

            order.append(node)

            for neighbor in reversed(graph[node]):

                if neighbor not in visited:

                    stack.append(neighbor)

                    edges.append((node, neighbor))

    return order, edges

def draw_graph(screen):

    for node in graph:

        for neighbor in graph[node]:

            x1, y1 = positions[node]
            x2, y2 = positions[neighbor]

            color = (140, 140, 140)

            thickness = 4

            if (node, neighbor) in path_edges or (neighbor, node) in path_edges:

                color = (90, 220, 120)

                thickness = 8

            pygame.draw.line(
                screen,
                color,
                (x1, y1),
                (x2, y2),
                thickness
            )

    for node, (x, y) in positions.items():

        color = BLUE

        if node in visited_nodes:

            color = (120, 210, 130)

        if node == current_node:

            color = RED

        if node == selected_start:

            color = (255, 190, 70)

        pygame.draw.circle(
            screen,
            color,
            (x, y),
            40
        )

        pygame.draw.circle(
            screen,
            BLACK,
            (x, y),
            40,
            3
        )

        draw_text(
            screen,
            node,
            30,
            WHITE,
            x,
            y
        )

def reset_graph():

    global selected_start
    global visited_nodes
    global current_node
    global algorithm
    global path_edges
    global message
    global running_algorithm
    global animation_index
    global animation_timer

    selected_start = None

    visited_nodes = []

    current_node = None

    algorithm = []

    path_edges = []

    running_algorithm = False

    animation_index = 0

    animation_timer = 0

    message = "Graph reset"

def run(screen, clock):

    global selected_start
    global visited_nodes
    global current_node
    global algorithm
    global path_edges
    global message
    global running_algorithm
    global animation_index
    global animation_timer

    reset_graph()

    running = True

    back_button = pygame.Rect(30, 25, 140, 50)

    bfs_button = pygame.Rect(180, 700, 220, 60)

    dfs_button = pygame.Rect(500, 700, 220, 60)

    reset_button = pygame.Rect(820, 700, 220, 60)

    while running:

        screen.fill((235, 240, 248))

        pygame.draw.rect(
            screen,
            (225, 230, 240),
            (40, 110, 1120, 540),
            border_radius=22
        )

        pygame.draw.rect(
            screen,
            (220, 225, 235),
            (40, 670, 1120, 120),
            border_radius=22
        )

        draw_text(
            screen,
            "Graph Traversal Visualiser",
            48,
            BLACK,
            600,
            40
        )

        draw_text(
            screen,
            "Breadth First Search and Depth First Search",
            24,
            BLACK,
            600,
            82
        )

        draw_graph(screen)

        pygame.draw.rect(
            screen,
            (240, 240, 240),
            (180, 650, 840, 40),
            border_radius=10
        )

        draw_text(
            screen,
            message,
            22,
            BLACK,
            600,
            670
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

            if animation_timer >= 28:

                animation_timer = 0

                if animation_index < len(algorithm):

                    current_node = algorithm[animation_index]

                    visited_nodes.append(current_node)

                    message = f"Visiting Node {current_node}"

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

                        distance = (
                            (pos[0] - x) ** 2 +
                            (pos[1] - y) ** 2
                        ) ** 0.5

                        if distance <= 40:

                            selected_start = node

                            message = f"Selected Start Node: {node}"

                if bfs_button.collidepoint(pos):

                    if selected_start is not None:

                        algorithm, path_edges = bfs(selected_start)

                        visited_nodes = []

                        animation_index = 0

                        running_algorithm = True

                        message = "Running Breadth First Search"

                if dfs_button.collidepoint(pos):

                    if selected_start is not None:

                        algorithm, path_edges = dfs(selected_start)

                        visited_nodes = []

                        animation_index = 0

                        running_algorithm = True

                        message = "Running Depth First Search"

        clock.tick(60)