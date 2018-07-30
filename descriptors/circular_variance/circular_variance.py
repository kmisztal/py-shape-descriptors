import cv2
import numpy as np
from warnings import warn

from descriptors.utils.moments import moments


def circular_variance(image, method=None):
    _, contours, _ = cv2.findContours(image, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)
    if len(contours) != 1:
        warn("More than one blob?")
    cnt = contours[0]

    n = len(cnt)
    centroid = moments(image, kind='central')
    centroid_x = centroid['mean_x']
    centroid_y = centroid['mean_y']

    norm = np.linalg.norm(cnt - [centroid_x, centroid_y], axis=2)
    mean_radius = sum(norm)[0] / n

    b = sum((norm - mean_radius) ** 2)[0]

    return b / n / mean_radius ** 2
