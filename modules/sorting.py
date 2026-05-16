import pygame
import sys
import random

from ui import *

array = [random.randint(40, 400) for _ in range(30)]

sorting = False
paused = False

algorithm_name = "None"
message = "Choose a sorting algorithm"

i = 0
j = 0
min_index = 0
merge_size = 1

highlight_a = -1
highlight_b = -1
sorted_index = -1

def generate_array():
    global array
    global sorting
    global paused
    global message
    global algorithm_name
    global i
    global j
    global min_index
    global merge_size
    global highlight_a
    global highlight_b
    global sorted_index

    array = [random.randint(40, 400) for _ in range(30)]

    sorting = False
    paused = False

    algorithm_name = "None"
    message = "Generated new random values"

    i = 0
    j = 0
    min_index = 0
    merge_size = 1

    highlight_a = -1
    highlight_b = -1
    sorted_index = -1

def draw_array(screen):
    start_x = 80
    bar_width = 30
    spacing = 5

    for index, value in enumerate(array):

        x = start_x + index * (bar_width + spacing)
        y = 560 - value

        color = BLUE

        if index == highlight_a:
            color = RED

        if index == highlight_b:
            color = (240, 180, 60)

        if index <= sorted_index and algorithm_name != "Merge Sort":
            color = (100, 200, 120)

        pygame.draw.rect(
            screen,
            color,
            (x, y, bar_width, value),
            border_radius=6
        )

        draw_text(
            screen,
            str(value),
            16,
            BLACK,
            x + bar_width // 2,
            y - 12
        )

def bubble_sort_step():
    global i
    global j
    global sorting
    global highlight_a
    global highlight_b
    global sorted_index
    global message

    if i < len(array):

        if j < len(array) - i - 1:

            highlight_a = j
            highlight_b = j + 1

            message = f"Comparing {array[j]} and {array[j + 1]}"

            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

            j += 1

        else:
            sorted_index += 1
            j = 0
            i += 1

    else:
        sorting = False
        message = "Bubble Sort completed"

def selection_sort_step():
    global i
    global j
    global min_index
    global sorting
    global highlight_a
    global highlight_b
    global sorted_index
    global message

    if i < len(array):

        if j == 0:
            min_index = i
            j = i + 1

        if j < len(array):

            highlight_a = min_index
            highlight_b = j

            message = f"Searching for minimum value"

            if array[j] < array[min_index]:
                min_index = j

            j += 1

        else:
            array[i], array[min_index] = array[min_index], array[i]

            sorted_index = i

            i += 1
            j = 0

    else:
        sorting = False
        message = "Selection Sort completed"

def merge(left, mid, right):
    left_part = array[left:mid]
    right_part = array[mid:right]

    i = 0
    j = 0
    k = left

    while i < len(left_part) and j < len(right_part):

        if left_part[i] <= right_part[j]:
            array[k] = left_part[i]
            i += 1
        else:
            array[k] = right_part[j]
            j += 1

        k += 1

    while i < len(left_part):
        array[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        array[k] = right_part[j]
        j += 1
        k += 1

def merge_sort_step():
    global merge_size
    global sorting
    global message

    n = len(array)

    if merge_size < n:

        left = 0

        while left < n:

            mid = min(left + merge_size, n)
            right = min(left + 2 * merge_size, n)

            merge(left, mid, right)

            left += 2 * merge_size

        merge_size *= 2

        message = f"Merging sections of size {merge_size // 2}"

    else:
        sorting = False
        message = "Merge Sort completed"

def run(screen, clock):
    global sorting
    global paused
    global algorithm_name
    global i
    global j
    global sorted_index
    global message

    generate_array()

    running = True

    back_button = pygame.Rect(30, 25, 120, 45)

    bubble_button = pygame.Rect(120, 620, 180, 50)
    selection_button = pygame.Rect(340, 620, 180, 50)
    merge_button = pygame.Rect(560, 620, 180, 50)

    pause_button = pygame.Rect(780, 620, 120, 50)
    generate_button = pygame.Rect(930, 620, 180, 50)

    while running:

        screen.fill(BACKGROUND)

        draw_text(
            screen,
            "Sorting Visualiser",
            48,
            BLACK,
            600,
            45
        )

        draw_text(
            screen,
            f"Current Algorithm: {algorithm_name}",
            26,
            BLACK,
            600,
            90
        )

        draw_array(screen)

        pygame.draw.rect(
            screen,
            (220, 220, 220),
            (80, 560, 1040, 40),
            border_radius=10
        )

        draw_text(
            screen,
            message,
            22,
            BLACK,
            600,
            580
        )

        draw_button(screen, back_button, "Back", BLUE, LIGHT_BLUE)

        draw_button(
            screen,
            bubble_button,
            "Bubble Sort",
            BLUE,
            LIGHT_BLUE
        )

        draw_button(
            screen,
            selection_button,
            "Selection Sort",
            (200, 120, 70),
            (220, 150, 100)
        )

        draw_button(
            screen,
            merge_button,
            "Merge Sort",
            (120, 160, 90),
            (145, 190, 110)
        )

        draw_button(
            screen,
            pause_button,
            "Pause",
            RED,
            LIGHT_RED
        )

        draw_button(
            screen,
            generate_button,
            "New Values",
            (170, 120, 210),
            (190, 145, 230)
        )

        if sorting and not paused:

            if algorithm_name == "Bubble Sort":
                bubble_sort_step()

            elif algorithm_name == "Selection Sort":
                selection_sort_step()

            elif algorithm_name == "Merge Sort":
                merge_sort_step()

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

                if bubble_button.collidepoint(pos):
                    generate_array()

                    sorting = True
                    algorithm_name = "Bubble Sort"

                    message = "Bubble Sort started"

                if selection_button.collidepoint(pos):
                    generate_array()

                    sorting = True
                    algorithm_name = "Selection Sort"

                    message = "Selection Sort started"

                if merge_button.collidepoint(pos):
                    generate_array()

                    sorting = True
                    algorithm_name = "Merge Sort"

                    message = "Merge Sort started"

                if pause_button.collidepoint(pos):
                    paused = not paused

                    if paused:
                        message = "Animation paused"
                    else:
                        message = "Animation resumed"

                if generate_button.collidepoint(pos):
                    generate_array()

        clock.tick(12)