#import module
from rsgis import Metadata

#path to metadata
path='../tests/data/LC08_L1TP_190055_20200214_20200225_01_T1_MTL.txt'

#instantiate class

mtd=Metadata(path)

#To access a particular parameter value

print(mtd.get('sun'))

# #To access a list of parameters in the metadata file
print(mtd.get_some(['GROUP','sun','path','row','radiance']))

# #To access all particular parameters in the metadata
print(mtd.get_all())
