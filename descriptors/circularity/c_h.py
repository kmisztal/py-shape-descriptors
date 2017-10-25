from math import pi

from descriptors.utils.moments import m00_f, mu02_f, mu20_f


def C_h(img):
    m00 = m00_f(img)

    mu20 = mu20_f(img)
    mu02 = mu02_f(img)

    return (m00 * m00) / (2.0 * pi * (mu20 + mu02))
