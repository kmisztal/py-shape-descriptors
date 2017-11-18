from descriptors.datasets.common import _load_dataset

kinds = [
    'apple', 'bat', 'beetle', 'bell', 'bird', 'bone', 'bottle', 'brick', 'butterfly', 'camel',
    'car', 'carriage', 'cattle', 'cellphone', 'chicken', 'child', 'chopper', 'classic', 'comma', 'crown',
    'cup', 'deer', 'device0', 'device1', 'device2', 'device3', 'device4', 'device5', 'device6', 'device7',
    'device8', 'device9', 'dog', 'elephant', 'face', 'fish', 'flatfish', 'fly', 'fork', 'fountain',
    'frog', 'glas', 'guitar', 'hammer', 'hat', 'hcircle', 'heart', 'horse', 'horseshoe', 'jar',
    'key', 'lizzard', 'imfixh', 'misk', 'octopus', 'pencil', 'car', 'pocket', 'rat', 'ray',
    'seasnake', 'shoe', 'spoon', 'spring', 'stef', 'teddy', 'tree', 'truck', 'turtle', 'watch',
]


def load_data(kind='all', black=0, white=1, size='all'):
    """
        Loads the MPEG-7 Core Experiment CE-Shape-1 Test Set
        from http://www.dabi.temple.edu/~shape/MPEG7/dataset.html

        :return: dictionary with file name as a key and array of 0 and 1 representing image as a corresponding value
    """

    url = 'http://misztal.edu.pl/static/media/uploads/databases/MPEG7dataset.zip'
    ext = "*.gif"

    if kind != 'all' and kind not in kinds:
        raise ValueError('Not proper kind, should be one of ' + str(kinds))

    if kind == 'all':
        kind = ''

    if size == 'all':
        size = 10 * 10
    if isinstance(size, str):
        try:
            size = int(size)
        except:
            raise ValueError("Wrong size number value, should be number or string 'all'")

    return _load_dataset(url=url, dataset_name='MPEG7dataset', ext=ext, kind=kind, black=black, white=white,
                         size=size)
