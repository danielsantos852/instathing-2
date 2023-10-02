# External imports
import pandas as pd
import xml.etree.ElementTree as ET


# Import XML as DataFrame function
def import_xml_as_df(path:str='') -> pd.core.frame.DataFrame:
    
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