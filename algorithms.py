from collections import deque
import heapq

def bubble_sort(arr):

    arr = arr.copy()

    n = len(arr)

    for i in range(n):

        for j in range(n - i - 1):

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

def selection_sort(arr):

    arr = arr.copy()

    n = len(arr)

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:

                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2

    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)

def merge(left, right):

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:

            result.append(left[i])
            i += 1

        else:

            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def bfs(graph, start):

    visited = set()

    queue = deque([start])

    order = []

    visited.add(start)

    while queue:

        node = queue.popleft()

        order.append(node)

        for neighbor in graph[node]:

            if neighbor not in visited:

                visited.add(neighbor)

                queue.append(neighbor)

    return order

def dfs(graph, start):

    visited = set()

    stack = [start]

    order = []

    while stack:

        node = stack.pop()

        if node not in visited:

            visited.add(node)

            order.append(node)

            for neighbor in reversed(graph[node]):

                stack.append(neighbor)

    return order

def dijkstra(grid, start, end):

    rows = len(grid)
    cols = len(grid[0])

    pq = []

    heapq.heappush(pq, (0, start))

    distances = {
        start: 0
    }

    previous = {}

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    while pq:

        current_distance, current = heapq.heappop(pq)

        if current == end:
            break

        row, col = current

        for dr, dc in directions:

            nr = row + dr
            nc = col + dc

            if 0 <= nr < rows and 0 <= nc < cols:

                if grid[nr][nc] == -1:
                    continue

                weight = grid[nr][nc]

                distance = current_distance + weight

                neighbor = (nr, nc)

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

    return path, distances.get(end, 0)