# Imports
from json import loads as json_loads
from xml.etree import ElementTree

from pandas import read_parquet
from pandas.core.frame import DataFrame


def import_xml_as_df(path:str|None = None) -> DataFrame:
    """
    Import contents of a XML file to a pandas dataframe

    :param path: XML file path
    :type path: str|None
    :return: A pandas dataframe
    :rtype: pandas.core.frame.DataFrame|None
    """
    # Try this:
    try:

        # Parse XML file data
        tree = ElementTree.parse(source=path)

    # If file not found:
    except FileNotFoundError:
        
        # Return None
        return None

    # Write parsed data to a list
    data = []
    for element in tree.getroot():
        row={}
        for subelement in element:
            row[subelement.tag] = subelement.text
        data.append(row)    
    
    # Create dataframe with data from list
    df = DataFrame(data)
    
    # Return dataframe
    return df


def import_parquet_as_df(path:str|None = None) -> DataFrame|None:
    """
    Import contents of a parquet file to a pandas dataframe

    :param path: parquet file path
    :type path: str|None
    :return: A pandas dataframe
    :rtype: pandas.core.frame.DataFrame|None
    """
    # Try this:
    try:

        # Create dataframe with data from parquet file
        df = read_parquet(path)
        
        # Return dataframe
        return df
    
    # If file not found:
    except FileNotFoundError:
        
        # Return None
        return None


def import_json_as_dict(path:str|None = None) -> dict|None:
    """
    Import contents of a JSON file to a python dict

    :param path: JSON file path
    :type path: str|None
    :return: A python dict
    :rtype: dict|None
    """
    # Try this:
    try:
        
        # Open JSON file in read mode
        with open(path, 'r') as file:
            
            # Get file contents to a dict
            dict = json_loads(file.read())

            # Return dict
            return dict
    
    # If file not found:
    except FileNotFoundError:
        
        # Return None
        return None