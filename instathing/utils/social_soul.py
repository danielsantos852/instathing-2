# Imports
from textwrap import wrap

import numpy as np
from pandas.core.frame import DataFrame
from PIL import Image
import requests

import config as cfg
from .image_manipulation import add_text_to_image


# Global Variables
COLUMNS_OF_INTEREST = cfg.COLUMNS_OF_INTEREST_LIST
PATH_TO_IMG_OUTPUT_FOLDER = cfg.DEFAULT_PATH_TO_TMP_IMAGE_FOLDER
PATH_TO_IG_STORY_TEMPLATE = cfg.PATH_TO_DEFAULT_STORY_TEMPLATE_IMG


# Refine Dataframe function
def refine_df(df:DataFrame) -> DataFrame:
    """
    Refines a pandas dataframe with raw offer data from Social Soul.

    Parameters:
        df (DataFrame): a pandas dataframe.

    Returns:
        df (DataFrame): same dataframe, refined.
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


# Generate IG Story Images for Dataframe function
def gen_ig_story_imgs_for_df(
    df:DataFrame = None,
    output_folder = PATH_TO_IMG_OUTPUT_FOLDER
) -> DataFrame:
    """ 
    Generates offer images for IG story posting using offer data from df, 
    saves images in output_folder, appends column of image paths to df, also 
    removes no longer necessary columns from df.
    
    Parameters:
        df (DataFrame): a pandas dataframe containing refined offer data;
        output_folder (str): path to folder where images will be stored.

    Returns:
        df (DataFrame): input dataframe with less columns but a new one.
    """
    # Create empty list of IG story images
    ig_story_images = []
    
    # For each offer in offers dataframe:
    for i in range(len(df)):
        
        # Generate IG story image
        ig_story_images.append(
            gen_offer_ig_story_img(
                output_file= f'{output_folder}offer{str(i).zfill(3)}.png', # e.g.: "offer001.png",
                base_image=PATH_TO_IG_STORY_TEMPLATE,
                offer_thumbnail= df.loc[i, 'offerThumbnail'],
                offer_name= df.loc[i, 'offerName'],
                offer_price_from= df.loc[i, 'priceFrom'],
                offer_price_to= df.loc[i, 'priceTo'],
            )
        )
    
    # Add IG story images list as column in dataframe
    df['igStoryImage'] = ig_story_images
    
    # Drop columns no longer needed
    df.drop(
        labels=['offerThumbnail', 'priceFrom', 'priceTo'],
        axis='columns',
        inplace=True
    )
    
    # Return dataframe
    return df


# Generate Instagram Story Image from Offer function
def gen_offer_ig_story_img(
    output_file:str = './tmp/img/test.png',
    base_image:str = './rsc/img/tmpl_story_720x1280_blue.png',
    offer_thumbnail:str = './rsc/img/fake_offer_thumbnail_640x640.png',
    offer_name:str = 'Awesome shoes!',
    offer_price_from:str = '9999.99',
    offer_price_to:str = '0000.00',
) -> str:
    """
    Generates a 720x1280 offer image fit for an IG Stories post.
    
    Parameters:
        output_file (str): path to output image file
        base_image (str): path to 720x1280 template image
        offer_thumbnail (str): url to product thumbnail
        offer_name (str): product description
        offer_price_from (str): product price before discount
        offer_price_to (str): product price after discount

    Returns:
        output_file (str): same as input
    """
    # Create new IG story image from base image
    im_story = Image.open(fp=base_image)
    
    # Download and paste offer thumbnail to IG story image
    im_thumbnail = Image.open(requests.get(offer_thumbnail, stream=True).raw)
    im_thumbnail = im_thumbnail.resize(size=(640,640))
    im_story.paste(im=im_thumbnail,box=(40, 130))
    
    # Clip offer name if max length exceeded
    max_name_length = 50
    if len(offer_name) > max_name_length:
        if offer_name[max_name_length-4]==' ':
            offer_name = f'{offer_name[:max_name_length-4]}...'
        else:
            offer_name = f'{offer_name[:max_name_length-3]}...'

    # Add offer name to IG story image
    im_story = add_text_to_image(
        im=im_story,
        font_size=40,
        x=27.5, # (10+17.5)
        y=827.5, # (100+700+20+7.5)
        text= '\n'.join(wrap(text=offer_name, width=30)),
        text_align='left'
    )
    
    # Prepare offer price text
    offer_price_to = f'{offer_price_to:.2f}'.replace('.',',')
    if offer_price_from == None:
        price_text = f'Por apenas R${offer_price_to}'
    else:
        offer_price_from = f'{offer_price_from:.2f}'.replace('.',',')
        price_text = f'De R${offer_price_from} por apenas R${offer_price_to}'
    
    # Add offer price text to IG story image
    im_story = add_text_to_image(
        im=im_story,
        font_size=37.5,
        x=27.5, # (10+17.5)
        y=982.5, # (100+700+15+140+15+12.5)
        text=price_text,
        text_align='left'
    )
    
    # Save IG story image as PNG file
    im_story.save(fp=output_file)
    
    # Return output path
    return output_file