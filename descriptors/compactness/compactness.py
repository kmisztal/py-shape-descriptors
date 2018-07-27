from descriptors.circularity import circularity


def compactness(image, method='perimeters_ratio', approx_contour=True):
    if method == 'perimeters_ratio':
        return circularity(image, method='Cst', approx_contour=approx_contour)
    else:
        print("Unknown method.")