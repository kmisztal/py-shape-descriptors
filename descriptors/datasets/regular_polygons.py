from descriptors.datasets.common import _load_dataset

kinds = [
    'r03', 'r04', 'r05', 'r06', 'r07', 'r08', 'r09', 'r10', 'r11', 'r12',
]


def load_data(kind='all', black=0, white=1, size='all'):
    """
    Loads regular polygons images.

        :return: dictionary with file name as a key and array of 0 and 1 representing image as a corresponding value
    """

    url = 'http://misztal.edu.pl/static/media/uploads/databases/regular_polygons.zip'

    ext = "*.png"

    if kind != 'all' and kind not in kinds:
        raise ValueError('Not proper kind, should be one of ' + str(kinds))

    if kind == 'all':
        kind = ''

        if size == 'all':
            size = 10
        if isinstance(size, str):
            try:
                size = int(size)
            except:
                raise ValueError("Wrong size number value, should be number or string 'all'")

    return _load_dataset(url=url, dataset_name='regular_polygons', ext=ext, kind=kind, black=black, white=white,
                         size=size)
