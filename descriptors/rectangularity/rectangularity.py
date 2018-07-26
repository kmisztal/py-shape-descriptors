import cv2
import numpy as np
# https://docs.opencv.org/3.4/dd/d49/tutorial_py_contour_features.html
from diCELLa_INDeep.utils.utils import show_image
# need compute minimum bounding rectangle
# Algorytm:
# weź maskę
# znajdź punkty na konturze
# znajdź otoczkę wypukłą
# dopasuj prostokąt (algorytm wymaga punktów z otoczki)
# zwraca współrzędne
#
# jest też boundingRect ale on dopasowuje prostokąto o osiach równoległych do osi
#
# spoko artykuł o Contour Features: https://docs.opencv.org/3.4/dd/d49/tutorial_py_contour_features.html
#
#
# img = load()
# im2,contours,hierarchy = cv.findContours(thresh, 1, 2)  # https://docs.opencv.org/3.4.0/d3/dc0/group__imgproc__shape.html#ga17ed9f5d79ae97bd4c7cf18403e1689a
# cnt = contours[0]
#
#
# # Rotated Rectangle
# rect = cv2.minAreaRect(cnt)
# box = cv2.boxPoints(rect)
# box = np.int0(box)
# cv2.drawContours(img,[box],0,(0,0,255),2)  # działa?
#
#
# # Drawing polygon - for testing
# https://docs.opencv.org/3.1.0/dc/da5/tutorial_py_drawing_functions.html
# show_image(cv2.polylines(img, [box.reshape(-1,1,2).astype(np.int32)], True, 3))


def rectangularity(image, method='mbr'):
    """
    There are 3 methods to define rectangularity:
    Minimum bounding rectangle: MBR
    Rectangular discrepancy: R'_D
    Robust MBR: R_R
    http://dicella.chrispi.webfactional.com/wp-content/uploads/2018/07/download.pdf

    This function implements the moment invariants so far.
    :param image: np.ndarray: Source, an 8-bit single-channel image. Non-zero pixels are treated as 1's. Zero pixels remain 0's, so the image is treated as binary.
    :return: float \in [0, 1]
    """
    if method == 'mbr':
        # mode: https://docs.opencv.org/3.4.0/d3/dc0/group__imgproc__shape.html#ga819779b9857cc2f8601e6526a3a5bc71
        # method: https://docs.opencv.org/3.4.0/d3/dc0/group__imgproc__shape.html#ga4303f45752694956374734a03c54d5ff
        im2, contours, hierarchy = cv2.findContours(image, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) != 1:
            print("More than one blob?")
        cnt = contours[0]  # mdoe=cv2.RETR_EXTERNAL powinno wystarczyć, żeby złapało największy:
        # por. example_ellipse3 dla mode = cv2.RETR_LIST
        # https://docs.opencv.org/3.4.1/d3/dc0/group__imgproc__shape.html#ga3d476a3417130ae5154aea421ca7ead9
        rect = cv2.minAreaRect(cnt)  # output ( center (x,y), (width, height), angle of rotation )
        # https://docs.opencv.org/3.4/d3/dc0/group__imgproc__shape.html#gaf78d467e024b4d7936cf9397185d2f5c
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        mbr_area = cv2.contourArea(box)

        show_image(cv2.polylines(image, [box.reshape(-1, 1, 2)], True, 3))

        image[image > 0] = 1
        region_area = np.sum(image)
        print(region_area)
        print(mbr_area)
        return region_area / mbr_area
    else:
        print("Wrong method.")
