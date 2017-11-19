from math import pi


def C_h(img):
    m00 = m00(img)

    mu20 = mu20(img)
    mu02 = mu02(img)

    return (m00 * m00) / (2.0 * pi * (mu20 + mu02))
