from numpy import mgrid, float32
from numpy import sum as sum_np


def _sum(array):
    return sum_np(array, dtype=float32)


def moments(image, kind='all'):
    """
    This function calculates the raw, centered and normalized moments
    for any image passed as a numpy array.
    Further reading:
    https://en.wikipedia.org/wiki/Image_moment
    https://en.wikipedia.org/wiki/Central_moment
    https://en.wikipedia.org/wiki/Moment_(mathematics)
    https://en.wikipedia.org/wiki/Standardized_moment
    http://opencv.willowgarage.com/documentation/cpp/structural_analysis_and_shape_descriptors.html#cv-moments

    compare with:
    import cv2
    cv2.moments(image)
    """
    assert len(image.shape) == 2  # only for grayscale images
    y, x = mgrid[:image.shape[0], :image.shape[1]]
    moments = dict()
    moments['mean_x'] = _sum(x * image) / _sum(image)
    moments['mean_y'] = _sum(y * image) / _sum(image)

    if kind in ['all', 'spatial', 'raw']:
        # raw or spatial moments
        moments['m00'] = _sum(image)
        moments['m10'] = _sum(x * image)
        moments['m01'] = _sum(y * image)
        moments['m11'] = _sum(x * y * image)
        moments['m20'] = _sum(x ** 2 * image)
        moments['m02'] = _sum(y ** 2 * image)
        moments['m12'] = _sum(x * y ** 2 * image)
        moments['m21'] = _sum(x ** 2 * y * image)
        moments['m30'] = _sum(x ** 3 * image)
        moments['m03'] = _sum(y ** 3 * image)

    if kind in ['all', 'central', 'standardized']:
        # central moments
        moments['mu00'] = _sum(image)  # = moments['m00']
        moments['mu10'] = _sum((x - moments['mean_x']) * image)  # should be 0
        moments['mu01'] = _sum((y - moments['mean_y']) * image)  # should be 0
        moments['mu11'] = _sum((x - moments['mean_x']) * (y - moments['mean_y']) * image)
        moments['mu20'] = _sum((x - moments['mean_x']) ** 2 * image)  # variance
        moments['mu02'] = _sum((y - moments['mean_y']) ** 2 * image)  # variance
        moments['mu12'] = _sum((x - moments['mean_x']) * (y - moments['mean_y']) ** 2 * image)
        moments['mu21'] = _sum((x - moments['mean_x']) ** 2 * (y - moments['mean_y']) * image)
        moments['mu30'] = _sum((x - moments['mean_x']) ** 3 * image)
        moments['mu03'] = _sum((y - moments['mean_y']) ** 3 * image)

    # opencv versions
    # moments['mu02'] = _sum(image*(x-m01/m00)**2)
    # moments['mu02'] = _sum(image*(x-y)**2)

    # wiki variations
    # moments['mu02'] = m20 - mean_y*m10
    # moments['mu20'] = m02 - mean_x*m01

    if kind in ['all', 'standardized']:
        # central standardized or normalized or scale invariant moments
        sum_image = _sum(image)
        moments['nu00'] = moments['mu00'] / moments['mu00'] ** (0 / 2 + 1)  # = 1
        moments['nu10'] = moments['mu10'] / moments['mu00'] ** (1 / 2 + 1)  # = 0
        moments['nu01'] = moments['mu01'] / moments['mu00'] ** (1 / 2 + 1)  # = 0

        moments['nu11'] = moments['mu11'] / sum_image ** (2 / 2 + 1)
        moments['nu12'] = moments['mu12'] / sum_image ** (3 / 2 + 1)
        moments['nu21'] = moments['mu21'] / sum_image ** (3 / 2 + 1)
        moments['nu20'] = moments['mu20'] / sum_image ** (2 / 2 + 1)
        moments['nu02'] = moments['mu02'] / sum_image ** (2 / 2 + 1)
        moments['nu03'] = moments['mu03'] / sum_image ** (3 / 2 + 1)  # skewness
        moments['nu30'] = moments['mu30'] / sum_image ** (3 / 2 + 1)  # skewness
    return moments


def m00(image):
    assert len(image.shape) == 2  # only for grayscale images

    return _sum(image)


def mu20(image):
    assert len(image.shape) == 2  # only for grayscale images

    x, y = mgrid[:image.shape[0], :image.shape[1]]
    mean_x = _sum(x * image) / _sum(image)
    return _sum((x - mean_x) ** 2 * image)


def mu02(image):
    assert len(image.shape) == 2  # only for grayscale images

    x, y = mgrid[:image.shape[0], :image.shape[1]]
    mean_y = _sum(y * image) / _sum(image)
    return _sum((y - mean_y) ** 2 * image)


def hu_moments(image):
    """
    https://en.wikipedia.org/wiki/Image_moment

    :param image: input image as array with signal set to 1 and background set to 0
    :return: list of Hu moments [I_1, ..., I_7]
    """
    # TODO: perform same test
    m = moments(image, kind='standardized')
    return [
        m['nu20'] + m['nu02'],  # I1

        (m['nu20'] - m['nu02']) ** 2 + 4. * m['nu11'] ** 2,  # I2

        (m['nu30'] - 3 * m['nu12']) ** 2 + (3 * m['nu21'] - m['nu03']) ** 2,  # I3

        (m['nu30'] + m['nu12']) ** 2 + (m['nu21'] + m['nu03']) ** 2,  # I4

        (m['nu30'] - 3 * m['nu12']) * (m['nu30'] + m['nu12']) * (
            (m['nu30'] + m['nu12']) ** 2 - 3 * (m['nu21'] + m['nu03']) ** 2)
        + (3 * m['nu21'] - m['nu03']) * (m['nu21'] + m['nu03']) * (
            3 * (m['nu30'] + m['nu12']) ** 2 - (m['nu21'] + m['nu03']) ** 2),  # I5

        (m['nu20'] - m['nu02']) * ((m['nu30'] + m['nu12']) ** 2 - (m['nu21'] + m['nu03']) ** 2)
        + 4 * m['nu11'] * (m['nu30'] + m['nu12']) * (m['nu21'] + m['nu03']),  # I6

        (3 * m['nu21'] - m['nu03']) * (m['nu30'] + m['nu12']) * (
            (m['nu30'] + m['nu12']) ** 2 - 3 * (m['nu21'] + m['nu03']) ** 2)
        - (m['nu30'] - 3 * m['nu12']) * (m['nu21'] + m['nu03']) * (
            3 * (m['nu30'] + m['nu12']) ** 2 - (m['nu21'] + m['nu03']) ** 2),  # I7
        m['nu11'] * ((m['nu30'] + m['nu12']) ** 2 - (m['nu03'] + m['nu21']) ** 2)
        - (m['nu20'] - m['nu02']) * (m['nu30'] + m['nu12']) * (m['nu03'] + m['nu21'])  # I8

    ]
