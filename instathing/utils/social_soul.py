# Imports
import numpy as np
from pandas.core.frame import DataFrame

from .image_manipulation import create_ig_story_image_from_offer


# Global Variables
DEFAULT_PATH_TO_STORY_TEMPLATE = './rsc/img/tmpl_story_720x1280_final.png'
DEFAULT_STORY_IMAGES_OUTPUT_FOLDER = './tmp/img/'


# Refine Dataframe function
def dataframe_refine(df:DataFrame) -> DataFrame:
    """
    Refines a pandas dataframe with raw offers data from Social Soul XML file

    Parameters:
        df (DataFrame): a pandas dataframe
    
    Returns:
        df (DataFrame): a pandas dataframe
    """
    # Select columns of interest and clip dataframe
    # (Uncomment/comment to keep/remove a column)
    df = df.loc[:,[
        'offerName',            # Offer description
        #'sellerId',
        #'sellerThumbnail',
        'offerLink',            # URL to offer
        'offerThumbnail',       # Photo of product in white background (most of the time)
        'priceFrom',            # Price without discount (price before)
        #'sellerName',
        'priceTo',              # Price with discount (price after)
        #'sku',
        #'categoryName',
        #'categoryId',
    ]]

    # Cast prices from str to float64
    df['priceFrom'] = df['priceFrom'].astype('float64')
    df['priceTo'] = df['priceTo'].astype('float64')

    # Clean empty cells (replace NaN with None)
    df = df.replace(np.nan, None)

    # Return dataframe
    return df


# Dataframe Generate IG Stories function
def dataframe_generate_ig_story_images(
    df:DataFrame = None,
    output_folder = DEFAULT_STORY_IMAGES_OUTPUT_FOLDER
) -> DataFrame:
    """ 
    Generates IG story images, appends column of image paths to dataframe, removes columns no longer needed.
    
    Parameters:
        df (DataFrame): a pandas dataframe containing offer data
        output_folder (str): path to folder were images will be stored

    Returns:
        df (DataFrame): same pandas dataframe with less columns but a new one
    """

    # Create empty list of IG Stories images
    ig_stories_images = []
    
    # For each offer in offers dataframe:
    for i in range(len(df)):
        
        # Generate IG Stories image
        ig_stories_images.append(
            create_ig_story_image_from_offer(
                base_image=DEFAULT_PATH_TO_STORY_TEMPLATE,
                offer_thumbnail= df.loc[i, 'offerThumbnail'],
                offer_name= df.loc[i, 'offerName'],
                offer_price_from= df.loc[i, 'priceFrom'],
                offer_price_to= df.loc[i, 'priceTo'],
                output_path= f'{output_folder}offer{str(i).zfill(3)}.png' # e.g.: 'offer001.png',
            )
        )
    
    # Add IG Stories images list as column in dataframe
    df['storiesImage'] = ig_stories_images
    
    # Drop columns no longer needed
    df.drop(
        labels=['offerThumbnail', 'priceFrom', 'priceTo'],
        axis='columns',
        inplace=True
    )
    
    # Return dataframe
    return df