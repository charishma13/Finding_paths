import sys
import os
import imageio.v3 as imageio
from find_path_save_image import visualize_path, find_path
from check_paths import path_exists
from nonintersecting_paths import find_two_nonintersecting_paths

# Add parent directory to path (if modules are in parent folder)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

input_path = 'Inputs/polygons.png'
input_name = os.path.splitext(os.path.basename(input_path))[0]

# Load the image and convert to grayscale if needed
universe = imageio.imread(input_path)
universe = universe[:, :, 0] if len(universe.shape) == 3 else universe  # grayscale

# Default coordinates in case none provided
start_basic = (10, 10)
end_basic = (99, 99)

# Parse coordinates from command line arguments if provided
# Expected usage: python your_script.py start_x start_y end_x end_y
if len(sys.argv) == 5:
    try:
        start_basic = (int(sys.argv[1]), int(sys.argv[2]))
        end_basic = (int(sys.argv[3]), int(sys.argv[4]))
    except ValueError:
        print("Invalid coordinates provided. Using default coordinates.")
else:
    print("No coordinates provided via command line. Using default coordinates.")

# Basic path existence check
print(path_exists(universe, *start_basic, *end_basic))

# Path and Visualization
path = find_path(universe, start_basic, end_basic)
if path:
    output_path = f'Outputs/path_{input_name}_{start_basic[0]}_{start_basic[1]}_to_{end_basic[0]}_{end_basic[1]}.png'
    visualize_path(universe, path, output_path)
