# Import Libraries
import pandas as pd
import xml.etree.ElementTree as ET


# Main function
def main():
    
    pass


# Refine Dataframe (Social Soul) function
def refine_dataframe_social_soul(df:pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    
    # Set columns of interest
    columns_of_interest = [
        'offerName',
        #'sellerId',
        #'sellerThumbnail',
        'offerLink',
        'offerThumbnail',
        'priceFrom',
        #'sellerName',
        'priceTo',
        #'sku',
        #'categoryName',
        #'categoryId',
    ]
    
    # Create refined dataframe using columns of interest
    df_refined = df.loc[:,columns_of_interest]
    
    # Return refined dataframe
    return df_refined


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


# If this is the script being run:
if __name__=='__main__':
    
    # Call main function
    main()