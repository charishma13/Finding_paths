import sys
import os
import imageio.v3 as imageio
from find_path_save_image import visualize_path, find_path
from check_paths import path_exists
from nonintersecting_paths import find_two_nonintersecting_paths

# Add parent directory to path (if modules are in parent folder)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Input image path
input_image_path = 'Inputs/polygons.png'

# Load the image and convert to grayscale if needed
universe = imageio.imread(input_image_path)
universe = universe[:, :, 0] if len(universe.shape) == 3 else universe  # grayscale

# Extract base input name without extension
input_name = os.path.splitext(os.path.basename(input_image_path))[0]

# Parent folder for all runs
parent_folder = 'Outputs_nonintersection'
os.makedirs(parent_folder, exist_ok=True)

# Function to get next numbered run folder inside parent folder, prefixed with input_name
def get_next_run_folder(parent, prefix):
    i = 1
    while True:
        folder_name = os.path.join(parent, f"{prefix}_{i}")
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            return folder_name
        i += 1

# Create main run folder inside Outputs_nonintersection named after input file
run_folder = get_next_run_folder(parent_folder, input_name)

# Default pairs of coordinates
pair1 = ((10, 10), (99, 99))
pair2 = ((20, 20), (80, 80))

# Parse coordinates from command line arguments if provided
# Usage: python script.py start1_x start1_y end1_x end1_y start2_x start2_y end2_x end2_y
if len(sys.argv) == 9:
    try:
        pair1 = ((int(sys.argv[1]), int(sys.argv[2])), (int(sys.argv[3]), int(sys.argv[4])))
        pair2 = ((int(sys.argv[5]), int(sys.argv[6])), (int(sys.argv[7]), int(sys.argv[8])))
    except ValueError:
        print("Invalid coordinates provided. Using default coordinates.")
else:
    print("No valid coordinate arguments provided. Using default coordinates.")

# Find two non-intersecting paths
p1, p2 = find_two_nonintersecting_paths(universe, pair1, pair2)

if p1 and p2:
    print(f"Saving results in folder: {run_folder}")
    output_path1 = os.path.join(run_folder, f'nonintersect_path1_{pair1[0][0]}_{pair1[0][1]}_to_{pair1[1][0]}_{pair1[1][1]}.png')
    output_path2 = os.path.join(run_folder, f'nonintersect_path2_{pair2[0][0]}_{pair2[0][1]}_to_{pair2[1][0]}_{pair2[1][1]}.png')
    visualize_path(universe, p1, output_path1)
    visualize_path(universe, p2, output_path2)
else:
    print("No two non-intersecting paths found.")
