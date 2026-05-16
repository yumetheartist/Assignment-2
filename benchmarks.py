import random
import time

from algorithms import *

numbers = [
    random.randint(1, 10000)
    for _ in range(1000)
]

print()
print("===== Sorting Algorithm Benchmarks =====")
print()

start = time.perf_counter()

bubble_sort(numbers)

end = time.perf_counter()

print(
    f"Bubble Sort Time: {(end - start):.6f} seconds"
)

start = time.perf_counter()

selection_sort(numbers)

end = time.perf_counter()

print(
    f"Selection Sort Time: {(end - start):.6f} seconds"
)

start = time.perf_counter()

merge_sort(numbers)

end = time.perf_counter()

print(
    f"Merge Sort Time: {(end - start):.6f} seconds"
)

print()
print("===== Graph Algorithm Benchmarks =====")
print()

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4]
}

start = time.perf_counter()

bfs(graph, 0)

end = time.perf_counter()

print(
    f"BFS Time: {(end - start):.6f} seconds"
)

start = time.perf_counter()

dfs(graph, 0)

end = time.perf_counter()

print(
    f"DFS Time: {(end - start):.6f} seconds"
)

print()
print("===== Pathfinding Benchmark =====")
print()

grid = [
    [1, 1, 2, 4],
    [2, -1, 3, 1],
    [1, 5, 2, 1],
    [3, 2, 1, 1]
]

start = time.perf_counter()

path, cost = dijkstra(
    grid,
    (0, 0),
    (3, 3)
)

end = time.perf_counter()

print(
    f"Dijkstra Time: {(end - start):.6f} seconds"
)

print()
print("Shortest Path:")
print(path)

print()
print("Path Cost:")
print(cost)