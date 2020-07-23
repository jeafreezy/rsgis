import tarfile, os
from tqdm import tqdm

class unzipper(object):
    """
    This is the class that decompresses the compressed file(s) by calling the unzip function.

    Parameters:
    path(str): This is the path to the compressed file.
    name(str): This is the name of the folder where the uncompressed files will be saved.

    Result:
    str: This function returns the path to the uncompressed file.
    """

    def __init__(self, path, bands,  name = 'extracted_data'): 
        self._path, self.name, self.bands = path, name, bands
        self.tar = tarfile.open(path)
        self.path = os.path.join(os.path.dirname(path), self.name)
        self.bands_dir = {}

    def _unzip(self):
        if not os.path.exists(self.path): os.mkdir(self.path)
        
        if self.bands:
            self.tar.extractall(path = self.path, members = self.band_searcher())
            self.tar.close()
            self.bands_dir = all_band_dirs(self.path, self.bands_dir)
        else:
            self.tar.extractall(self.path)
            self.tar.close()
            self.bands_dir = all_band_dirs(self.path, self.bands_dir)

    def band_searcher(self):
        self.band_searches = {}
        for i in self.bands:
            if i > 0: self.band_searches['_B{}.TIF'.format(i)] = i
            else: self.band_searches['_MTL.txt'] = i
        for tarinfo in self.tar:
            if tarinfo.name.endswith(tuple(list(self.band_searches))): yield tarinfo

    def get_band(self, *args):
        paths = {}
        for i in args:
            try:
                paths[i] = self.bands_dir[i]
            except KeyError:
                print("The particular file/ band {} has not been unzipped".format(i))
        return paths

def all_band_dirs(path, bands_dir):
    for root, dir, name in os.walk(path):
        for i in name:
            if i.endswith('_MTL.txt'): bands_dir[0] = os.path.join(root, i)
            else: bands_dir[int(i[-5])] = os.path.join(root, i)
        break
    return bands_dir

def unzip(path, bands = []):
    """ This is the function used for uncompressing files.
    >>> from rsgis import landsat
    >>> path = '/home/user/compresion.tar.xz'
    >>> landsat.unzip(path)

    Parameters:
        path (str): path to the file to be unzipped
        bands (list): list of specific bands to unzip
                0 - metadata file
                1 - band1
                2 - band2, etc
    >>> from rsgis import landsat
    >>> path = '/home/user/compresion.tar.xz'
    >>> landsat.unzip(path, bands = [0,1,2])
    """

    assert type(bands) == list,'Your bands should be in a list format and not {}'.format(type(bands))
    assert all(type(i) == int for i in bands), 'bands parameter only accept integer values'
    data = unzipper(path, bands)
    data._unzip()
    return data
