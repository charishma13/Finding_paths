# Python Take-Home Interview - TetraMem

## Overview

This repository contains the solution to the TetraMem Python take-home interview assignment. The task involves analyzing a 2D "universe" (a black-and-white image) to:

- Determine if a path exists between two points crossing only black pixels.

- Visualize the valid path if it exists.

- Find two non-intersecting paths for two pairs of points, ensuring paths are on black pixels and do not overlap.

## Problem Description

Given a black-and-white image representing a 2D universe and pairs of start and end coordinates, the program determines if paths exist on black pixels between the points. It also visualizes these paths by saving images with the paths overlaid.

Additional goals include finding two paths for two pairs of points that do not intersect with each other.

## Project Structure

Q1_main.py - Script to check for a single path existence and visualize it.

Q2_main.py - Script to find two non-intersecting paths and save visualizations.

check_paths.py - Contains path_exists() function to verify path existence.

find_path_save_image.py - Functions to find paths and visualize them on images.

nonintersecting_paths.py - Logic to find two non-intersecting paths.

Inputs/ - Folder containing input images (black-and-white universe images).

Outputs/ - Folder where path visualization images are saved.

Outputs_nonintersection/ - Folder where outputs of two non-intersecting paths are saved.

Take_Home_Assessment.ipynb - Jupyter notebook with exploratory work or demonstrations.

## How to Run

1. Single path check and visualization:

<pre><code>Q1_main.py start_x start_y end_x end_y</code></pre>

Example:

<pre><code>Q1_main.py 10 10 99 99</code></pre>

Output images are saved in the Outputs/ folder.

2. Two non-intersecting paths:

<pre><code>Q2_main.py start1_x start1_y end1_x end1_y start2_x start2_y end2_x end2_y</code></pre>

Example:

<pre><code>Q2_main.py 10 10 99 99 20 20 80 80</code></pre>

Output images are saved in uniquely named subfolders under Outputs_nonintersection/ folder.

## Notes:

If no command line arguments are provided, default coordinates are used.

The scripts create output folders automatically if they don’t exist.

Input file names are used in output folder or file naming for clarity.

The paths found are guaranteed to lie only on black pixels.

***

Feel free to explore the Jupyter notebook Take_Home_Assessment.ipynb for additional context and examples.
