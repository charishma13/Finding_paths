import numpy as np
from collections import deque

def path_exists(universe: np.ndarray, start_x: int, start_y: int, end_x: int, end_y: int) -> bool:
    if universe[start_y, start_x] != 0 or universe[end_y, end_x] != 0:
        return False  # start or end is not black

    height, width = universe.shape
    visited = np.zeros_like(universe, dtype=bool)
    queue = deque([(start_x, start_y)])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # left, right, up, down

    while queue:
        x, y = queue.popleft()
        if (x, y) == (end_x, end_y):
            return True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < width) and (0 <= ny < height):
                if universe[ny, nx] == 0 and not visited[ny, nx]:
                    visited[ny, nx] = True
                    queue.append((nx, ny))

    return False
