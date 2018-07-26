from math import pi
# from descriptors.utils.moments.moments import moments
from descriptors.utils.moments import moments


def ellipticity(image, method='moment_invariants'):
    """
    There are 4 methods to define ellipticity:
    Moment invariants (in two similar versions): E_I
    Elliptic variance: E_V
    Euclidean ellipticity: E_E
    DFT: E_F
    http://dicella.chrispi.webfactional.com/wp-content/uploads/2018/07/download.pdf

    This function implements the moment invariants so far.
    :param image: np.ndarray, binary mask
    :return: float \in [0, 1]
    """
    if method == 'moment_invariants':
        m = moments(image)
        # I_1 affine moment invariant
        i_1 = (m['mu20'] * m['mu02'] - m['mu11'] ** 2) / m['mu00'] ** 4

        # I_1 for unit circle
        ic = 1 / (16 * pi ** 2)
        if i_1 <= ic:
            return i_1 / ic
        else:
            return ic / i_1
    else:
        print("Wrong method.")
