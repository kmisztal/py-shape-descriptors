from math import sqrt

import numpy as np


def is_edge(img, i, j):
    # if img.getRed[i, j] != 0:
    if img[i, j] != 0:
        return False

    height, width = img.shape

    neighbors = 0
    if i > 0 and img[i - 1, j] == 0:
        neighbors += 1

    if i < width - 1 and img[i + 1, j] == 0:
        neighbors += 1

    if j > 0 and img[i, j - 1] == 0:
        neighbors += 1

    if j < height - 1 and img[i, j + 1] == 0:
        neighbors += 1

    return neighbors not in [0, 4]


def perimeter(img):
    height, width = img.shape
    num_matrix = np.zeros((height, width), dtype=np.int)  # 0-background 1-perimeter

    perimeter_ = 0
    for i in range(height):  # zamiana z: width
        for j in range(width):  # zamiana z: height
            if img[i, j] == 0:
                if is_edge(img, i, j):
                    num_matrix[i][j] = 1
                else:
                    num_matrix[i][j] = 0
            else:
                num_matrix[i][j] = 0

    # convolution with mask
    kernel = [10, 2, 10, 2, 1, 2, 10, 2, 10]
    num_output = [0] * (width * height)
    for y in range(height):
        for x in range(width):
            xMin = x - 1
            xMax = x + 1
            yMin = y - 1
            yMax = y + 1
            for r in range(yMin, yMax + 1):
                for c in range(xMin, xMax + 1):
                    if 0 <= r < width and 0 <= c < height:  # zamiana z: if 0 <= r < height and 0 <= c < width:
                        num_output[y * width + x] += num_matrix[c][r] * kernel[(r - yMin) * 3 + (c - xMin)]

    # perimeter calc
    a = 1
    b = sqrt(2)
    c = (1 + b) / 2

    for j in range(height):
        for i in range(width):
            v = num_output[j * width + i]
            if v in [5, 7, 15, 17, 25, 27]:
                perimeter_ += a
            elif v in [21, 33]:
                perimeter_ += b
            elif v in [13, 23]:
                perimeter_ += c

    return perimeter_
