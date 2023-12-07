# This program extracts the fluorescent beads coordinates detected in our 3D 
# Line Confocal Microscope scans. The point locations in x, y, z are outputted 
# as arrays to be displayed in our Javascript visualizer program.

# The below code is modified from the starter code Javier/ChatGPT wrote.

import tifffile as tiff
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os

# 1. Load in all the tiffs in a given folder
# corresponding to a z-stack. Combine into a single tif.
# Append to a numpy array

def combine_frames(path):
    # Combine all the tif files in a folder into one multi-layered/"page" tif

    tif_files = []

    for filename in os.listdir(path):
        if filename.endswith(".tif"):
            tif_files.append(os.path.join(path, filename))

    # sanity check.
    # num_files = len(tif_filenames)
    # print(f"found {num_files} images under stack: {path}")

    # sort alphabetically to ensure proper ordering
    tif_files.sort()

    # store the data here as a list
    data_list = []

    # combine! read data from each tif file and append to list
    for tif_file in tif_files:
        with tiff.TiffFile(tif_file) as tif:
            data_list.append(tif.asarray())

    # save
    combined_tif_output_path = f"{path}/combined.tif"
    tiff.imwrite(combined_tif_output_path, data_list)

    # ignore below.
    # another sanity check.
    # print(f"the corresponding numpy array has length {len(tif_array)}.")
    # that LONG ASS array has length num_frames * (image_width * image height)

def stack_loader(path):
    # Load in and return the combined tif file as a numpy array.

    # If it doesn't exist yet, call the combine function & save the multi-
    # layered tif file.
    if not os.path.isfile(f"{path}/combined.tif"):
        combine_frames(path)
    
    # read the newly-created multipage TIFF file
    with tiff.TiffFile(combined_tif_output_path) as tif:
        # Load all pages into a NumPy array
        tif_array = tif.asarray()

    # return the array -- ready to be processed w/ Javier's code.
    return tif_array

stack1_array = stack_loader("D:/hella_data/beads120523/stack1")
# stack_loader("D:/hella_data/beads120523/stack2")
# stack_loader("D:/hella_data/beads120523/stack3")
# stack_loader("D:/hella_data/beads120523/stack4")
# stack_loader("D:/hella_data/beads120523/stack5")

# data
#   stack1 (folder)
#       image1
#       image2
#       ...
#   stack2
#       (etc.)

# 2. Scan thru the numpy array. (the part Javier wrote.)

# 3. Export to a array in a .js file