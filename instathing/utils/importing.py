# Imports
import pandas as pd
import json
import xml.etree.ElementTree as ET


# Import Pandas DataFrame from XML file function
def import_dataframe_from_xml(path:str) -> pd.core.frame.DataFrame:
    
    # Extracted from:
    # https://saturncloud.io/blog/converting-xml-to-python-dataframe-a-comprehensive-guide/
    
    # Parse the XML file
    tree = ET.parse(path)
    root = tree.getroot()
    
    # Extract data
    data = []
    for element in root:
        row={}
        for subelement in element:
            row[subelement.tag] = subelement.text
        data.append(row)    
    
    # Convert data to DataFrame
    df = pd.DataFrame(data)
    
    # Return DataFrame
    return df


# Import Pandas DataFrame from Parquet file function
def import_dataframe_from_parquet(path:str) -> pd.core.frame.DataFrame:

    # Load dataframe from parquet file
    df = pd.read_parquet(path=path)
    
    # Return loaded dataframe
    return df


# Import Credentials from JSON function
def import_credentials_from_json(path:str) -> dict:

    # Try to:
    try:
        
        # Open JSON file in read mode
        with open(path, 'r') as file:
            
            # Return file contents as a dict
            return json.loads(file.read())
    
    # If file not found:
    except FileNotFoundError:
        
        # Return empty dictionary
        return {}