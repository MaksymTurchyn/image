from PIL import Image
import numpy as np
import sys
import matplotlib.pyplot as plt
from skimage import io
import skimage.segmentation as seg
import skimage.filters as filters
import skimage.draw as draw
import skimage.color as color

# Options
np.set_printoptions(threshold=sys.maxsize)

# Image
img = io.imread('600 dpi.png', as_gray=True)  # 300 dpi shape(3507, 2550)


def image_show(image):
    fig, ax = plt.subplots(1, 1, figsize=(14, 14))
    ax.imshow(image, cmap='gray')
    ax.axis('off')
    return fig, ax


def pixel_hist(image):
    fig, ax = plt.subplots(1, 1, figsize=(14, 14))
    ax.hist(img, bins=32, range=[0, 256])
    ax.set_xlim(0, 256)


def char_split(row):
    transposed_row = np.transpose(row)
    char_index = - 1
    char_space = []
    for t in transposed_row:
        char_index += 1
        if np.isin(t, [255]).all() == True:
            char_space.append(char_index)

    list_of_chars = []
    for s in range(1, len(char_space) - 1):
        if char_space[s - 1] + 5 < char_space[s]:
            char = transposed_row[char_space[s - 1]:char_space[s] + 1, :]
            transposed_back = np.transpose(char)
            list_of_chars.append(transposed_back)
    return list_of_chars

def row_split(image):
    lis_of_rows = []

    row_index = - 1
    row_space = []
    for i in image:
        row_index += 1
        if np.isin(i, [255]).all() == True:
            row_space.append(row_index)

    for s in range(1, len(row_space) - 1):
        if row_space[s - 1] + 20 < row_space[s]:
            row = image[row_space[s - 1]:row_space[s] + 1, :]
            list_of_char = char_split(row)
            lis_of_rows.append(list_of_char)
    return lis_of_rows

def main():
    characters = row_split(img)
    for i in characters:
        for j in i:
            image_show(j)
            plt.show()

if __name__ == '__main__':
    main()