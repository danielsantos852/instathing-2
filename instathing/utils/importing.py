# Imports
from pandas.core.frame import DataFrame
import pandas as pd
import json
import xml.etree.ElementTree as ET


# DataFrame from XML function
def df_from_xml(
    input_xml:str = None
) -> DataFrame:
    """
    Loads the contents of a XML file to memory as a pandas DataFrame.

    Parameters:
        input_xml (str): path to input XML file.

    Returns:
        df (DataFrame): a pandas dataframe object.
    """
    # Extracted from:
    # https://saturncloud.io/blog/converting-xml-to-python-dataframe-a-comprehensive-guide/
    
    # Parse the XML file
    tree = ET.parse(input_xml)
    root = tree.getroot()
    
    # Extract data
    data = []
    for element in root:
        row={}
        for subelement in element:
            row[subelement.tag] = subelement.text
        data.append(row)    
    
    # Convert data to DataFrame
    df = DataFrame(data)
    
    # Return DataFrame
    return df


# DataFrame from parquet function
def df_from_parquet(input_parquet:str = None) -> DataFrame:
    """
    Loads the contents of a parquet file to memory as a pandas DataFrame.

    Parameters:
        input_parquet (str): path to input parquet file.

    Returns:
        df (DataFrame): a pandas dataframe object.
    """
    # Load dataframe from parquet file
    df = pd.read_parquet(path=input_parquet)
    
    # Return loaded dataframe
    return df


# Dict from JSON function
def dict_from_json(input_json:str) -> dict:
    """
    Loads the contents of a json file to memory as a Python dict.
    
    Parameters
        input_json (str): path to input json file.

    Returns:
        (dict): a Python dict object; or
        
        None, if input file not found.
    """
    # Try to:
    try:
        
        # Open JSON file in read mode
        with open(input_json, 'r') as file:
            
            # Return file contents as a dict obj
            return json.loads(file.read())
    
    # If file not found:
    except FileNotFoundError:
        
        # Return nothing
        return None