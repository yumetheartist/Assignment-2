import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from algorithms import *

graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1]
}

grid = [
    [1, 1, 1],
    [1, -1, 1],
    [1, 1, 1]
]

numbers = [5, 3, 8, 1, 2]

print("Bubble Sort:")
print(bubble_sort(numbers))

print()

print("Selection Sort:")
print(selection_sort(numbers))

print()

print("Merge Sort:")
print(merge_sort(numbers))

print()

print("BFS:")
print(bfs(graph, 0))

print()

print("DFS:")
print(dfs(graph, 0))

print()

print("Dijkstra:")
path, cost = dijkstra(grid, (0, 0), (2, 2))

print("Path:", path)
print("Cost:", cost)