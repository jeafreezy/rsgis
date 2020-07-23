"""
******************************************
MODULE FOR METADATA FILE ACCESS
******************************************
Author: Jolaiya Emmanuel -> jolaiyaemmanuel@gmail.com
License: Apache
******************************************
"""

########
# HOW TO USE

"""
To get a particular parameter from the metadata file:
 
 #import
 from rsgis import Metadata
 mtd=Metadata('path\to\downloaded\landsat\file')
 
mtd.get('Solar Angle') = Returns the solar angle value in the metadata file
 
 metadata.get_some(['Solar Angle','RADIANCE']) = Return a list of the queried values in the metadata file
 
 metadata.get_all() = Return a dictionary of all the parameters in the metadata file
 
 
"""

import os

class Metadata:
    """
        This class handles the metadata files parameter access and query.

        Args:

         path(file path:str): path to metadata file

        exception:
         KeyError,TypeError

    """

    def __init__(self,path):

        self.path = path

    def _utility(self) -> dict:

        """Utility class to read metadata file and convert to dictionary"""

        #LANDSAT
        file=os.path.basename(self.path)
        assert isinstance(file, str), 'path must be of type string'

        assert 'LC0' in file.split('.')[0],'This is not a landsat metadata file. Check your file and retry'

        assert file.lower().endswith('.txt'), 'Landsat Metadata file must be in .txt(text) format'

        if file is not None and os.path.exists(self.path):

            try:
                # print('*_*' * 30)
                # print('\t\t\t\t\t -------------> LANDSAT METADATA <------------')

                metadata_dict = {}
                with open(self.path, mode='r') as metadata:
                    # assert metadata.readlines(),'File could not be opened. Pass in a valid metadata file'
                    for parameters in metadata.readlines():
                        parameters_list = parameters.split('=')
                        param_cleaned = ''.join(parameters_list[0].strip())
                        value_cleaned = ''.join(parameters_list[-1].strip())
                        metadata_dict[param_cleaned] = value_cleaned
                return metadata_dict

            except Exception as err:
                print(
                    'An error just occurred. Check the file to be sure it is a valid metadata file and check the parameters for possible error'
                    '\n You can also try the get_all() method to see'
                    'all the metadata parameters ')

                raise err

    def _incomplete_str_support(self, param:'str', metadata_dict:'dict') -> str:

        """
        A private method to guess incomplete query strings
        :param param:
        :param metadata_dict:
        :return: str or/and dict of guesses
        """

        try:

            assert isinstance(param, str), 'parameter must be of type str'

            multi_keys = {}

            for text in metadata_dict.keys():

                if param.upper() in text:
                    multi_keys[text] = metadata_dict.get(text)

            if len(multi_keys) > 1:

                print(
                    f'It seems your query **{param}** matches several parameters.Try to be  more specific to access your desired value, \n however, you can still make use of my guesses below')

                return multi_keys


            elif len(multi_keys) == 1:

                guess = list(multi_keys.keys())[0]

                print(
                    f'It seems you entered an incomplete query parameter. Was it **{guess}** you meant? If yes, see the result below.\n If no, try the get_all() method to see all'
                    f' available parameters.')

                return multi_keys.get(guess)

            else:

                return 'Could not find a match for your parameter. Try the .get_all() method to see available parameters \n or be more specific with your query parameter.'




        except Exception as err:

            print('Invalid query parameter. Ensure the spelling is correct and retry')

            raise err

    def get(self, param: 'str') -> str:

        """
            This method returns the value of any metadata parameter query if found,raises error if not found and suggest likely search pattern
            Args:
                 param: parameter to query
            return:

             str of value or dictionary if multiple match found

            exception:

             AssertionError

        """
        assert isinstance(param,
                          str), f'Argument must be a string and not {type(param)}. Try get_some() or get_all() method instead'
        metadata_dict = self._utility()

        param = param.upper()

        if param in metadata_dict:

            return metadata_dict.get(param)

        else:

            return self._incomplete_str_support(param, metadata_dict)

    def get_some(self, query_list: 'list') -> list:
        """
            This method returns the value of any metadata parameter query if found and raises error if not found
            Args:
                path: for command_line use
                query_list: list of strings of parameters to query

                values_list: Values of query found in order of argument

             :exception:
                AssertionError

        """

        try:

            assert isinstance(query_list,
                              list), 'It seems you have passed a wrong argument. The query list must be of type list'

            metadata_dict = self._utility()

            query_list = [query.upper() for query in query_list]

            values_list = []

            for queries in query_list:

                if queries in metadata_dict:

                    values_list.append(metadata_dict.get(queries))

                else:

                    values_list.append(self._incomplete_str_support(queries, metadata_dict))

            return values_list

        except Exception as err:

            raise err

    def get_all(self) -> dict:

        """
            This method returns the value of any metadata parameter query if found and raises error if not found
            args:
            path: for command_line use
            returns:

                A dictionary of all parameters in the metadata file

            :exception:

                AssertionError
        """


        return  self._utility()

###########COMMAND LINE SUPPORT####################

    def get_cli(self, param: 'str') -> str:

        """
            This method returns the value of any metadata parameter query if found,raises error if not found and suggest likely search pattern
            Args:
                 path: for command_line use
                 param: parameter to query
            return:

             str of value found

            exception:

             AssertionError

        """

        assert isinstance(param,
                          str), f'Argument must be a string and not {type(param)}. Try get_some() or get_all() method instead'
        metadata_dict = self._utility()

        param = param.upper()

        if param in metadata_dict:

            print(metadata_dict.get(param))

        else:

         print(self._incomplete_str_support(param, metadata_dict))

