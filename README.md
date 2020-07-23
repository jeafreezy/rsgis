# rsgis
A python package for basic GIS operations.

## Current release 
- Metadata file module

## Future release 
- Metadata file for other file formats(sentinel,NetCDF etc)
- A one liner for basic to advanced GIS operations
 
## Installation
#### Python version 3.0 +<br>
    pip install rsgis
#### Using the Metadata module <br>
     #import the class
    from rsgis import Metadata
    
    #instantiate the class
    mtd=Metadata(path/to/landsat/metadata/file)
    
    #usage
    mtd.get('SUN') #to get a single parameter. Might return a list of dict if found multiple match. Be specific to avoid this.
    
    met.get_all() #returns a dict of all available parameters in the metadata file
    
    mtd.get_some(['sun','path','row']) #To get multiple parameters. Returns a list of values.
    

## Running the tests

 Paste a metadata file in the data dir(delete old one) in tests and cd into the test dir then run in terminal<br>

    python metadata_test.py 
 If no error,then the file is valid. You can go ahead to using the class.
## Contributing.

 PRs and issues are welcomed and not limited to the following:
 - Code documentation
 - Refactoring
 - Adding support for other metadata file types etc
 
## Authors:
**Jolaiya Emmanuel** - [Twitter](https://twitter.com/jeafreezy), [Email](jolaiyaemmanuel@gmail.com) <br>
**Oke Matthew** - [Email](matthewoke16@gmail.com) <br>

## License
This project is licensed under the Apache 2.0 License - see the [LICENSE.md](LICENSE.md) file for details

