from find_path_save_image import find_path

def find_two_nonintersecting_paths(universe, pair1, pair2):
    path1 = find_path(universe, pair1[0], pair1[1])
    if not path1:
        return None, None

    universe_copy = universe.copy()
    for x, y in path1:
        universe_copy[y, x] = 255  # block these pixels

    path2 = find_path(universe_copy, pair2[0], pair2[1])
    if not path2:
        return None, None

    return path1, path2
    
