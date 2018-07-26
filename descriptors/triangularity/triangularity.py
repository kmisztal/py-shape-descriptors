from descriptors.utils.moments.moments import moments


def triangularity(image, method='moment_invariants'):
    """
    There are 4 methods to define triangularity:
    Moment invariants: T_I
    Polygonal triangle approximation: T_A
    Projections: T_P
    Minimum bounding triangle: T_B
    http://dicella.chrispi.webfactional.com/wp-content/uploads/2018/07/download.pdf

    This function implements the moment invariants so far.
    :param image: np.ndarray: binary mask
    :param method: method
    :return: float \in [0, 1]
    """
    if method == 'moment_invariants':
        m = moments(image)
        i_1 = (m['mu20'] * m['mu02'] - m['mu11'] ** 2) / m['mu00'] ** 4

        # I_1 for simple right angled triangle aligned with the axes after an affine transformation is applied
        it = 1 / 108
        if i_1 <= it:
            return i_1 / it
        else:
            return it / i_1
    else:
        print("Wrong method.")
