import pygame
import sys

from ui import *

stack = []
queue = []
linked_list = []
bst_values = []

stack_value = 1
queue_value = 1
linked_list_value = 1
bst_value = 1

message = "Welcome to the Data Structures Module"

def insert_bst(root, value):
    if root is None:
        return {
            "value": value,
            "left": None,
            "right": None
        }

    if value < root["value"]:
        root["left"] = insert_bst(root["left"], value)
    else:
        root["right"] = insert_bst(root["right"], value)

    return root

def inorder(root, result):
    if root:
        inorder(root["left"], result)
        result.append(str(root["value"]))
        inorder(root["right"], result)

def build_bst():
    root = None

    for value in bst_values:
        root = insert_bst(root, value)

    return root

def draw_stack(screen):
    pygame.draw.rect(screen, (230, 235, 245), (40, 100, 220, 500), border_radius=16)

    draw_text(screen, "STACK", 34, BLACK, 150, 130)
    draw_text(screen, "LIFO", 22, BLACK, 150, 165)

    for i, value in enumerate(reversed(stack[-5:])):
        rect = pygame.Rect(
            90,
            520 - (i * 60),
            120,
            45
        )

        pygame.draw.rect(screen, BLUE, rect, border_radius=8)

        draw_text(
            screen,
            str(value),
            26,
            WHITE,
            rect.centerx,
            rect.centery
        )

def draw_queue(screen):
    pygame.draw.rect(screen, (245, 232, 232), (290, 100, 420, 220), border_radius=16)

    draw_text(screen, "QUEUE", 34, BLACK, 500, 130)
    draw_text(screen, "FIFO", 22, BLACK, 500, 165)

    for i, value in enumerate(queue[:3]):
        rect = pygame.Rect(
            330 + (i * 120),
            220,
            100,
            50
        )

        pygame.draw.rect(screen, RED, rect, border_radius=8)

        draw_text(
            screen,
            str(value),
            26,
            WHITE,
            rect.centerx,
            rect.centery
        )

def draw_linked_list(screen):
    pygame.draw.rect(screen, (232, 245, 236), (290, 350, 670, 180), border_radius=16)

    draw_text(screen, "LINKED LIST", 34, BLACK, 620, 380)

    for i, value in enumerate(linked_list[:4]):
        x = 340 + (i * 150)

        rect = pygame.Rect(
            x,
            450,
            90,
            45
        )

        pygame.draw.rect(screen, (90, 170, 120), rect, border_radius=8)

        draw_text(
            screen,
            str(value),
            24,
            WHITE,
            rect.centerx,
            rect.centery
        )

        if i < len(linked_list[:4]) - 1:
            pygame.draw.line(
                screen,
                BLACK,
                (x + 90, 472),
                (x + 140, 472),
                4
            )

            pygame.draw.polygon(
                screen,
                BLACK,
                [
                    (x + 140, 472),
                    (x + 128, 464),
                    (x + 128, 480)
                ]
            )

def draw_bst_node(screen, value, x, y):
    pygame.draw.circle(screen, (170, 120, 210), (x, y), 24)

    draw_text(
        screen,
        str(value),
        22,
        WHITE,
        x,
        y
    )

def draw_bst_tree(screen, root, x, y, offset):
    if root is None:
        return

    draw_bst_node(screen, root["value"], x, y)

    if root["left"]:
        pygame.draw.line(
            screen,
            BLACK,
            (x, y),
            (x - offset, y + 70),
            3
        )

        draw_bst_tree(
            screen,
            root["left"],
            x - offset,
            y + 70,
            offset // 2
        )

    if root["right"]:
        pygame.draw.line(
            screen,
            BLACK,
            (x, y),
            (x + offset, y + 70),
            3
        )

        draw_bst_tree(
            screen,
            root["right"],
            x + offset,
            y + 70,
            offset // 2
        )

def draw_bst(screen):
    pygame.draw.rect(screen, (240, 232, 250), (740, 100, 220, 220), border_radius=16)

    draw_text(screen, "BST", 34, BLACK, 850, 130)

    root = build_bst()

    draw_bst_tree(screen, root, 850, 200, 50)

def run(screen, clock):
    global stack_value
    global queue_value
    global linked_list_value
    global bst_value
    global message

    running = True

    back_button = pygame.Rect(30, 25, 120, 45)

    push_button = pygame.Rect(60, 620, 80, 40)
    pop_button = pygame.Rect(160, 620, 80, 40)

    enqueue_button = pygame.Rect(330, 620, 110, 40)
    dequeue_button = pygame.Rect(460, 620, 110, 40)

    insert_button = pygame.Rect(650, 620, 90, 40)
    delete_button = pygame.Rect(760, 620, 90, 40)
    reverse_button = pygame.Rect(870, 620, 90, 40)

    bst_insert_button = pygame.Rect(780, 340, 150, 40)
    inorder_button = pygame.Rect(780, 390, 150, 40)

    while running:
        screen.fill(BACKGROUND)

        draw_text(
            screen,
            "Data Structures Visualiser",
            46,
            BLACK,
            500,
            45
        )

        draw_stack(screen)
        draw_queue(screen)
        draw_linked_list(screen)
        draw_bst(screen)

        draw_button(screen, back_button, "Back", BLUE, LIGHT_BLUE)

        draw_button(screen, push_button, "Push", BLUE, LIGHT_BLUE)
        draw_button(screen, pop_button, "Pop", BLUE, LIGHT_BLUE)

        draw_button(screen, enqueue_button, "Enqueue", RED, LIGHT_RED)
        draw_button(screen, dequeue_button, "Dequeue", RED, LIGHT_RED)

        draw_button(screen, insert_button, "Insert", (90, 170, 120), (120, 200, 150))
        draw_button(screen, delete_button, "Delete", (90, 170, 120), (120, 200, 150))
        draw_button(screen, reverse_button, "Reverse", (90, 170, 120), (120, 200, 150))

        draw_button(screen, bst_insert_button, "BST Insert", (170, 120, 210), (190, 145, 230))
        draw_button(screen, inorder_button, "Inorder", (170, 120, 210), (190, 145, 230))

        pygame.draw.rect(screen, (220, 220, 220), (40, 560, 920, 40), border_radius=10)

        draw_text(
            screen,
            message,
            22,
            BLACK,
            500,
            580
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

                if push_button.collidepoint(event.pos):
                    stack.append(stack_value)
                    message = f"Pushed {stack_value} onto Stack"
                    stack_value += 1

                if pop_button.collidepoint(event.pos):
                    if stack:
                        removed = stack.pop()
                        message = f"Popped {removed} from Stack"

                if enqueue_button.collidepoint(event.pos):
                    queue.append(queue_value)
                    message = f"Enqueued {queue_value} into Queue"
                    queue_value += 1

                if dequeue_button.collidepoint(event.pos):
                    if queue:
                        removed = queue.pop(0)
                        message = f"Dequeued {removed} from Queue"

                if insert_button.collidepoint(event.pos):
                    linked_list.append(linked_list_value)
                    message = f"Inserted {linked_list_value} into Linked List"
                    linked_list_value += 1

                if delete_button.collidepoint(event.pos):
                    if linked_list:
                        removed = linked_list.pop()
                        message = f"Deleted {removed} from Linked List"

                if reverse_button.collidepoint(event.pos):
                    linked_list.reverse()
                    message = "Reversed Linked List"

                if bst_insert_button.collidepoint(event.pos):
                    bst_values.append(bst_value)
                    message = f"Inserted {bst_value} into BST"
                    bst_value += 1

                if inorder_button.collidepoint(event.pos):
                    result = []

                    root = build_bst()

                    inorder(root, result)

                    message = "BST Inorder: " + " ".join(result)

        clock.tick(60)