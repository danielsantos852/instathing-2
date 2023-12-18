# Imports
import numpy as np
from pandas.core.frame import DataFrame

import config as cfg
from .image_manipulation import create_ig_story_image_from_offer


# Global Variables
COLUMNS_OF_INTEREST = cfg.COLUMNS_OF_INTEREST_LIST
PATH_TO_IMG_OUTPUT_FOLDER = cfg.DEFAULT_PATH_TO_TMP_IMAGE_FOLDER
PATH_TO_IG_STORY_TEMPLATE_IMG = cfg.DEFAULT_PATH_TO_STORY_TEMPLATE


# Refine Dataframe function
def dataframe_refine(df:DataFrame) -> DataFrame:
    """
    Refines a pandas dataframe with raw offers data from Social Soul XML file

    Parameters:
        df (DataFrame): a pandas dataframe
    
    Returns:
        df (DataFrame): a pandas dataframe
    """
    # Clip dataframe using columns of interest (configurable in config.py)
    df = df.loc[:, COLUMNS_OF_INTEREST]

    # Cast prices from str to float64
    df['priceFrom'] = df['priceFrom'].astype('float64')
    df['priceTo'] = df['priceTo'].astype('float64')

    # Clean empty cells (replace NaN with None)
    df = df.replace(np.nan, None)

    # Return dataframe
    return df


# Generate IG Story Images from Dataframe function
def gen_ig_story_imgs_from_df(
    df:DataFrame = None,
    output_folder = PATH_TO_IMG_OUTPUT_FOLDER
) -> DataFrame:
    """ 
    Generates offer images for IG story posting using data from input df, 
    saves images in output_folder. Appends column of image paths to input df, 
    also removes columns no longer needed.
    
    Parameters:
        df (DataFrame): a pandas dataframe containing offer data
        output_folder (str): path to folder were images will be stored

    Returns:
        df (DataFrame): same pandas dataframe with less columns but a new one
    """
    # Create empty list of IG Stories images
    ig_story_images = []
    
    # For each offer in offers dataframe:
    for i in range(len(df)):
        
        # Generate IG Stories image
        ig_story_images.append(
            create_ig_story_image_from_offer(
                base_image=PATH_TO_IG_STORY_TEMPLATE_IMG,
                offer_thumbnail= df.loc[i, 'offerThumbnail'],
                offer_name= df.loc[i, 'offerName'],
                offer_price_from= df.loc[i, 'priceFrom'],
                offer_price_to= df.loc[i, 'priceTo'],
                output_path= f'{output_folder}offer{str(i).zfill(3)}.png' # e.g.: 'offer001.png',
            )
        )
    
    # Add IG Stories images list as column in dataframe
    df['igStoryImage'] = ig_story_images
    
    # Drop columns no longer needed
    df.drop(
        labels=['offerThumbnail', 'priceFrom', 'priceTo'],
        axis='columns',
        inplace=True
    )
    
    # Return dataframe
    return df