from math import sqrt

from descriptors.utils.moments import moments


def elongation(image, method=None):
    central_moments = moments(image, kind='central')
    numerator = (central_moments['mu20'] - central_moments['mu02']) ** 2 + 4 * central_moments['mu11'] ** 2
    numerator = sqrt(numerator)
    denominator = central_moments['mu20'] + central_moments['mu02']
    return numerator / denominator
