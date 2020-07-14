#!/usr/bin/python3

import argparse
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import math
import sys
import os

# Convert rgb to grayscale
# from https://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])


# Process micrometer image
def process(jpg):

    if not os.path.exists(jpg):
        print("Please provide an image that exists",file=sys.stderr)
        return

    # Load image and threshold
    micrometer = Image.open(jpg)
    micrometer = rgb2gray(np.array(micrometer))
    micrometer = micrometer > np.mean(micrometer)*0.83

    width = micrometer.shape[1]
    height = micrometer.shape[0]
    pixels = np.zeros((width))

    for y in range(0, height):
        for x in range(0, width):
            if not micrometer[y][x]:
                pixels[x] = pixels[x] + 1

    # Record the x position of each line
    lines = []
    for i in range(len(pixels)):
        if pixels[i] > height * 0.25:
            lines.append(i)

    pos = []   # position of lines
    yaxis = [] # y axis value for 'dot' for visualisation

    lastcolumn = lines[0]
    newcolumn = lines[0]
    i = 0

    # Find groups of pixels that make up micrometer lines
    for curline in lines:
        if curline >= lastcolumn + 2 or i == len(lines)-1:
            pos.append((newcolumn + lastcolumn) / 2)
            yaxis.append(height/2)
            newcolumn = curline
        lastcolumn = curline
        i+=1

    print("Number of micrometer lines",len(pos))

    if len(pos) == 101:
        print("Found all micrometer lines, length is: ",pos[-1] - pos[0]," pixels")

    plt.scatter(pos, yaxis)
    plt.imshow(micrometer)
    plt.show() # show visualisation

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image", help="Filename of micrometer image")
    args = parser.parse_args()
    process(args.image)

