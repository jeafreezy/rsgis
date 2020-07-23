"""
******************************************
MODULE FOR METADATA FILE ACCESS
******************************************
Author1: Jolaiya Emmanuel -> jolaiyaemmanuel@gmail.com
Author2: Oke Matthew -> matthewoke16@gmail,com
This package is developed for the department of Remote Sensing and GIS
License: Apache
******************************************
"""

#HOW TO USE
"""
To extract file(s) from the downloaded landsat compressed data
To perform other specific operations on landsat images.


>>> from rsgis import landsat
>>> data = landsat.unzip(path_to_file)


"""
import tarfile, os

class unzipper(object):
    """
    This is the class that decompresses the compressed file(s) by calling the extract function.

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
            self.bands_dir = all_band_dirs(self.path, self.bands_dir)
        else:
            self.tar.extractall(self.path)
            self.bands_dir = all_band_dirs(self.path, self.bands_dir)
        self.tar.close()

    def band_searcher(self):
        self.band_searches = {}
        for i in self.bands:
            if i > 0: self.band_searches['_B{}.TIF'.format(i)] = i
            else: self.band_searches['_MTL.txt'] = i
        for tarinfo in self.tar:
            if tarinfo.name.endswith(tuple(list(self.band_searches))): yield tarinfo

    def get_bands(self, *args):
        """
        This is used to get the path to particular landsat file(s).

        >>> from rsgis import landsat
        >>> data = landsat.extract(path_to_downloaded_file)
        >>> data.get_bands(1, 2)
        >>> [1: 'path_to_band_1', 2:'path_to_band_2']

        Parameters:
        args(int): number of band path(s) to be returned

        Returns:
        dict: Returns a dictionary containing band numbers as key and bands as values
        
        """

        paths = {}
        for i in args:
            try:
                paths[i] = self.bands_dir[i]
            except KeyError:
                print("The particular file/ band {} has not been unzipped".format(i))
        return paths

    def get_metadata(self):
        """
        This function is used for getting the path to only the metadata file
        
        >>> from rsgis import landsat
        >>> data = landsat.extract(path_to_downloaded_file)
        >>> data.get_metadata()

        Returns:
        str: returns the path leading to the metadata file
        """

        metadata_path = self.get_bands(0)
        metadata_path = metadata_path[0]
        return metadata_path

def all_band_dirs(path, bands_dir = {}):
    for root, dir, name in os.walk(path):
        for i in name:
            if i.endswith('_MTL.txt'): bands_dir[0] = os.path.join(root, i)
            else: bands_dir[int(i[-5])] = os.path.join(root, i)
        break
    return bands_dir

def extract(path, bands = []):
    """ This is the function used for uncompressing files.
    >>> from rsgis import landsat
    >>> path = '/home/user/compresion.tar.xz'
    >>> landsat.extract(path)

    Parameters:
        path (str): path to the file to be unzipped
        bands (list): list of specific bands to extract
                0 - metadata file
                1 - band1
                2 - band2, etc
    >>> from rsgis import landsat
    >>> path = '/home/user/compresion.tar.xz'
    >>> landsat.extract(path, bands = [0,1,2])
    """

    assert type(bands) == list,'Your bands should be in a list format and not {}'.format(type(bands))
    assert all(type(i) == int for i in bands), 'bands parameter only accept integer values'
    data = unzipper(path, bands)
    data._unzip()
    return data
