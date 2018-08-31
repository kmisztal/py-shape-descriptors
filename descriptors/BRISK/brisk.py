import cv2
import numpy as np
import matplotlib.pyplot as plt


def brisk(image, mask, sort_by_response=False, *args, **kwargs):


    # matching
    brisk = cv2.BRISK_create(*args, **kwargs)

    kp, des = brisk.detectAndCompute(image, mask)
    # kp2, des2 = brisk.compute(img2, kp2)  # bo keypoints mogą być zmienione przec compute (usunięte, przeorganizowane itp)

    if sort_by_response:
        if len(kp) > 0:
            responses = [x.response for x in kp]
            des = [x[1] for x in sorted(zip(responses, des), reverse=True)]
            des = np.array(des)
        else:
            des = np.array([], dtype=np.uint8)

    # a = False
    # if a:
    # # create BFMatcher object
    #     bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    #     # Match descriptors.
    #     matches = bf.match(des, des2)
    #
    #     # Sort them in the order of their distance.
    #     matches = sorted(matches, key = lambda x:x.distance)
    #     # Draw first 10 matches.
    #     img3 = cv2.drawMatches(img, kp, img2, kp2, matches[:10], outImg=None, flags=2)
    #     plt.imshow(img3),plt.show()
    # else:
    #     # BFMatcher with default params
    #     bf = cv2.BFMatcher()
    #     matches = bf.knnMatch(des, des2, k=2)
    #     # Apply ratio test
    #     good = []
    #     for m, n in matches:
    #         if m.distance < 0.75 * n.distance:
    #             good.append([m])
    #     # cv2.drawMatchesKnn expects list of lists as matches.
    #     img3 = cv2.drawMatchesKnn(img, kp, img2, kp2, good, None, flags=2)
    #     plt.imshow(img3), plt.show()
    return kp, des


def show_keypoints(image, keypoints, *args, **kwargs):
    image2 = cv2.drawKeypoints(image, keypoints, outImage=None, *args, **kwargs)
    plt.figure()
    plt.imshow(image2)

