from distutils.core import setup

setup(
    name='py-shape-descriptors',
    version='0.0.1',
    packages=['tests', 'tests.circularity', 'descriptors', 'descriptors.utils', 'descriptors.utils.moments',
              'descriptors.datasets', 'descriptors.convexity', 'descriptors.elongation', 'descriptors.circularity',
              'descriptors.compactness', 'descriptors.ellipticity', 'descriptors.triangularity',
              'descriptors.rectangularity'],
    url='https://github.com/kmisztal/py-shape-descriptors',
    license='MIT',
    author='Krzysztof Misztal',
    author_email='krzysztof.misztal@gmail.com',
    description='Same shape descriptors implemented in Python3'
)
