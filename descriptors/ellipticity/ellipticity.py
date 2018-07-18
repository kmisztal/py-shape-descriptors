import math
from descriptors.utils.moments.moments import moments


def ellipticity(image, method='moment_invariants'):
    """
    There are 4 methods to define ellipticity:
    Moment invariants: E_I
    Elliptic variance: E_V
    Euclidean ellipticity: E_E
    DFT: E_F
    http://dicella.chrispi.webfactional.com/wp-content/uploads/2018/07/download.pdf

    This function implements the moment invariants so far.
    :param image: np.ndarray
    :return: float \in [0, 1]
    """
    if method == 'moment_invariants':
        m = moments(image)
        # I_1 pierwszy moment afiniczny
        i_1 = (m['mu20'] * m['mu02'] - m['mu11'] ** 2) / m['mu00'] ** 4

        # I_1 for unit radius circle
        ic = 1 / (16 * math.pi ** 2)
        if i_1 <= ic:
            return 16 * math.pi ** 2 * i_1
        else:
            return 1 / (16 * math.pi ** 2 * i_1)
    else:
        print("Wrong method.")
