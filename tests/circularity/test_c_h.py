from unittest import TestCase

from descriptors.circularity.c_h import C_h
from descriptors.datasets import regular_polygons


class Test_C_h(TestCase):
    def test_C_h(self):
        images = regular_polygons.load_data()
        vals = {
            'r03': 0.8270,
            'r04': 0.9549,
            'r05': 0.9833,
            'r06': 0.9924,
            'r07': 0.9960,
            'r08': 0.9977,
            'r09': 0.9986,
            'r10': 0.9991,
            'r11': 0.9994,
            'r12': 0.9996
        }

        for k, v in images.items():
            print("{0} {1:.4f} {2:.4f}".format(k, C_h(v), vals[k[:-4]]))
            self.assertAlmostEqual(C_h(v), vals[k[:-4]], 4)
