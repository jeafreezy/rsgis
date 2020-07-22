import unittest
from rsgis import Metadata
import os

class MetadataTest(unittest.TestCase):

    def test_file(self):

        dir=os.getcwd() + '\data'

        for _ in os.listdir(dir):

            path = dir + '\\' + _

            if _.endswith('txt') and _.split('.')[0].endswith('_MTL'):

                try:

                    with open(path,'r') as file:

                        if file.readlines():

                            self.assertEqual(Metadata(path).path,path)

                except Exception as err:
                    raise err






if __name__ == '__main__':
    unittest.main()

