from math import pi

from descriptors.utils import moments as m


def C_h(img):
    m00 = m.m00(img)

    mu20 = m.mu20(img)
    mu02 = m.mu02(img)

    return (m00 * m00) / (2.0 * pi * (mu20 + mu02))
