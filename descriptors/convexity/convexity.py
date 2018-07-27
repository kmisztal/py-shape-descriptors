import cv2
import numpy as np
from warnings import warn

from diCELLa_INDeep.utils.utils import show_image

# based on https://pdfs.semanticscholar.org/cd7d/a1577c985e6d1ed6c19a276e24246e81c20d.pdf
# Perimeter of convex hull / Perimeter of mask


def convexity(image, method='perimeters_ratio', approx_contour=True):
    # more information in rectangularity
    if method == 'perimeters_ratio':
        im2, contours, hierarchy = cv2.findContours(image, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) != 1:
            warn("More than one blob?")
        cnt = contours[0]
        hull = cv2.convexHull(cnt)

        # box = cv2.boxPoints(hull)
        # box = np.int0(box)
        # mbr_area = cv2.contourArea(box)
        # show_image(cv2.polylines(image.copy(), [hull.reshape(-1, 1, 2)], True, 2))

        # pic = np.zeros_like(im2)
        # for point in cnt:
        #     p = point[0][::-1]
        #     pic[p[0], p[1]] = 1
        #
        # for point in hull:
        #     p = point[0][::-1]
        #     pic[p[0], p[1]] = 2

        if approx_contour:
            cnt = cv2.approxPolyDP(cnt, epsilon=1, closed=True)
            # for point in cnt:
            #     p = point[0][::-1]
            #     pic[p[0], p[1]] = 3
        perimeter = cv2.arcLength(cnt, closed=True)

        # pic2 = pic.copy()
        # show_image(cv2.polylines(pic2, cnt, True, 2))
        # show_image(cv2.polylines(pic2, cnt_approx, True, 3))

        # show_image(pic)

        perimeter_convex_hull = cv2.arcLength(hull, True)

        print("Len cnt:", len(cnt))
        print("Len hull:", len(hull))
        print("Obwód cv2:", perimeter)
        print("Obwód otoczki cv2:", perimeter_convex_hull)

        return perimeter_convex_hull / perimeter
    else:
        print("Unknown method.")
