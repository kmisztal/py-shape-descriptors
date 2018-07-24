import cv2
from math import pi
from warnings import warn

from descriptors.utils import moments as m


def circularity(image, method='Ch'):
    if method == 'Ch':
        m00 = m.m00(image)

        mu20 = m.mu20(image)
        mu02 = m.mu02(image)

        return (m00 * m00) / (2.0 * pi * (mu20 + mu02))
    elif method == 'Cst':
        area = m.m00(image)

        _, contours, _ = cv2.findContours(image, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) != 1:
            warn("More than one blob?")
        cnt = contours[0]
        perimeter = cv2.arcLength(cnt, closed=True)

        return 4 * pi * area / perimeter ** 2
    else:
        warn("Unknown method.")
