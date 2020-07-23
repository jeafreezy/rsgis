# rsgis
A python package for basic to Advanced GIS operations.

## Current release 
- Landsat metadata support module

## Future release 
- Metadata support for other file formats(sentinel,NetCDF etc)
- A one liner for basic to advanced GIS operations
 
## Installation
#### Python version 3.0 +<br>
    pip install rsgis
    
#### Extracting files <br>
     #import the class
    from rsgis import landsat
    
    #Extract all files
    data = landsat.extract(path/to/landsat/dataset)
    
    #To check path to extracted data
    data.path
    
    #Extract specific bands
    #Here we will extract the metadata = 0, band1 = 1 and band2 = 2
    data = landsat.extract(path/to/landsat/dataset, bands = [0, 1, 2]
    
    #Get metadata path
    data.get_metadata()
    
    #Get path(s) to specific band(s)
    #In this example, we will be gettng band4 and band5
    data.get_bands(4, 5)
    
#### Using the Metadata module <br>
     #import the class
    from rsgis import Metadata
    
    #instantiate the class
    mtd=Metadata(path/to/landsat/metadata/file)
    
    #usage
    mtd.get('SUN') #to get a single parameter. Might return a list of dict if found multiple match. Be specific to avoid this.
    
    met.get_all() #returns a dict of all available parameters in the metadata file
    
    mtd.get_some(['sun','path','row']) #To get multiple parameters. Returns a list of values.
    
## Command line Use
Change directory into the rsgis folder to run

        python main.py --dir_path [path/to/metadata/file] --get [parametr to get]
        
        #This command returns the result of the --get query 
        
## Running the tests

 Paste a metadata file in the data dir(delete old one) in tests and cd into the test dir then run in terminal<br>

    python metadata_test.py 
 If no error,then you can go ahead to do some magic.
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

