import glob
import os
import shutil
import tempfile
import urllib.request
import zipfile

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

TEMP = tempfile.gettempdir()
path = TEMP + os.sep + 'databases' + os.sep


def _fetch_zipfile_from_url(url, file_name):
    if not os.path.exists(path):
        os.makedirs(path)

    if not os.path.exists(path + file_name + '.zip'):
        with urllib.request.urlopen(url) as response, open(path + file_name + '.zip', 'wb') as out_file:
            shutil.copyfileobj(response, out_file)

    if not os.path.exists(path + file_name):
        with zipfile.ZipFile(path + file_name + '.zip') as zf:
            zf.extractall(path + file_name)


def load_dataset(dataset_name='MPEG7dataset', kind='all', black=0, white=1, size='all'):
    """

    :param dataset_name:
    :param kind:
    :param black:
    :param white:
    :param size:
    :return: dictionary with file name as a key and array of 0 and 1 representing image as a corresponding value
    """
    ret = {}
    if dataset_name == 'MPEG7dataset':
        # http://www.dabi.temple.edu/~shape/MPEG7/dataset.html
        url = 'http://misztal.edu.pl/static/media/uploads/databases/MPEG7dataset.zip'
        _fetch_zipfile_from_url(url, dataset_name)
        kinds = [
            'apple', 'bat', 'beetle', 'bell', 'bird', 'bone', 'bottle', 'brick', 'butterfly', 'camel',
            'car', 'carriage', 'cattle', 'cellphone', 'chicken', 'child', 'chopper', 'classic', 'comma', 'crown',
            'cup', 'deer', 'device0', 'device1', 'device2', 'device3', 'device4', 'device5', 'device6', 'device7',
            'device8', 'device9', 'dog', 'elephant', 'face', 'fish', 'flatfish', 'fly', 'fork', 'fountain',
            'frog', 'glas', 'guitar', 'hammer', 'hat', 'hcircle', 'heart', 'horse', 'horseshoe', 'jar',
            'key', 'lizzard', 'imfixh', 'misk', 'octopus', 'pencil', 'car', 'pocket', 'rat', 'ray',
            'seasnake', 'shoe', 'spoon', 'spring', 'stef', 'teddy', 'tree', 'truck', 'turtle', 'watch',
        ]
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

    elif dataset_name == 'regular_polygons':
        # http://www.dabi.temple.edu/~shape/MPEG7/dataset.html
        url = 'http://misztal.edu.pl/static/media/uploads/databases/regular_polygons.zip'
        _fetch_zipfile_from_url(url, dataset_name)
        kinds = [
            'r03', 'r04', 'r05', 'r06', 'r07', 'r08', 'r09', 'r10', 'r11', 'r12',
        ]
        ext = "*.png"

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

    for file in glob.glob(path + dataset_name + os.sep + kind + ext):
        img = Image.open(file)
        try:
            data = np.asarray(img, dtype='uint8')
        except SystemError:
            data = np.asarray(img.getdata(), dtype='uint8')
        img.close()

        if np.unique(data).tolist() == [0, 255]:
            data = data // 255
        elif np.unique(data).tolist() == [0, 1] and dataset_name == 'regular_polygons':
            data = data ^ 1
        else:
            raise ValueError("Wrong type of image")

        ret[os.path.basename(file)] = data
        size -= 1
        if size == 0:
            break

    return ret


if __name__ == "__main__":
    images = load_dataset('regular_polygons', kind='r03', size=1)
    # images = load_dataset('MPEG7dataset', kind='apple', size=1)
    print(images)
    for v in images.values():
        print(np.unique(v))
        im = Image.fromarray(v)
        plt.imshow(v, interpolation='nearest')
        plt.show()
