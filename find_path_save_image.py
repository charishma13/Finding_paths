from PIL import Image
import numpy as np

def find_path(universe: np.ndarray, start, end):
    from collections import deque
    height, width = universe.shape
    visited = np.zeros_like(universe, dtype=bool)
    parent = dict()

    queue = deque([start])
    visited[start[1], start[0]] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            # Reconstruct path
            path = [(x, y)]
            while (x, y) != start:
                x, y = parent[(x, y)]
                path.append((x, y))
            return path[::-1]  # reverse path
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < width) and (0 <= ny < height) and universe[ny, nx] == 0 and not visited[ny, nx]:
                visited[ny, nx] = True
                parent[(nx, ny)] = (x, y)
                queue.append((nx, ny))
    return None


def visualize_path(universe: np.ndarray, path, output_path='Outputs/path_visualization.png'):
    img = np.stack([universe]*3, axis=-1)  # convert to RGB
    for x, y in path:
        img[y, x] = [255, 0, 0]  # red path
    Image.fromarray(img.astype(np.uint8)).save(output_path)
