### Content
 - [Current release](#Current_Release)
 - [Future release](#Future_Release)
 - [Installation](#Installation)
 - [Quick tutorial](#Quick_Tutorial)
 - [Command line Use](#Command_Line_Use)
 - [Running the tests](#Running_The_Tests)
 - [Authors](#Authors)
 - [License](#License)
 

# rsgis
A python package for basic to Advanced GIS operations.

# Current_Release 
- Metadata support module for landsat
- Landsat module for landsat bands extraction and manipulation

# Future_Release 
- Metadata support for other file formats(sentinel,NetCDF etc)
- A one liner for basic to advanced GIS operations
- NDVI,NDWI,NDBI
- Image subsetting/clipping support
 
# Installation
The package is available on the python package index(Pypi),to install use the command below;
### Python version 3.0 +<br>
  ```python
        pip install rsgis
  ```

# Quick_Tutorial
### Using the landsat module <br>
```python
     #import the module
    from rsgis import landsat
    
    #Extract all files
    data = landsat.extract(path/to/landsat/dataset)

    #To check path to extracted data
    data.path

    #Extract specific bands
    #Here we will extract the metadata = 0, band1 = 1 and band2 = 2

    data = landsat.extract(path/to/landsat/dataset, bands = [0, 1, 2])
    
    #Get metadata path
    data.get_metadata()
    
    #Get path(s) to specific band(s)
    #In this example, we will be getting band4 and band5
    data.get_bands(4, 5)

```
### Using the Metadata module with the Landsat Module <br>
```python
    #import the class
    from rsgis import Metadata,landsat
    data = landsat.extract(path/to/landsat/dataset)
    meta_path=data.get_metadata()
    mtd=Metadata(meta_path)
    #usage
    mtd.get('SUN') #to get a single parameter. Might return a list of dict if found multiple match. Be specific to avoid this.
    
    mtd.get_all() #returns a dict of all available parameters in the metadata file
    
    mtd.get_some(['sun','path','row']) #To get multiple parameters. Returns a list of values.
``` 
# Command_Line_Use
Change directory into the rsgis folder to run
```shell script

    python main.py --dir_path [path/to/metadata/file] --get [parametr to get]
    #This command returns the result of the --get query 
```      
# Running_The_Tests

 Paste a metadata file in the data dir(delete old one) in tests and cd into the test dir then run in terminal<br>

    python metadata_test.py 
 If no error,then you can go ahead to do some magic.
# Contributing

 PRs and issues are welcomed and not limited to the following:
 - Code documentation
 - Refactoring
 - Adding support for other metadata file types etc
 
# Authors
**Jolaiya Emmanuel** - [Twitter](https://twitter.com/jeafreezy), [Email](jolaiyaemmanuel@gmail.com) <br>
**Oke Matthew** - [Email](matthewoke16@gmail.com) <br>

# License
This project is licensed under the Apache 2.0 License - see the [LICENSE.md](LICENSE.md) file for details

