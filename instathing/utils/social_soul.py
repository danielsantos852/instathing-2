# External imports
import pandas as pd
import numpy as np

# Internal imports
from .ig_image_processing import generate_ig_stories_image


# Refine Dataframe (Social Soul) function
def refine_dataframe(df:pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    
    # STEP 1: Select columns of interest
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
    # Select columns of interest only
    df = df.loc[:,columns_of_interest]
    
    
    # STEP 2: Cast prices from STR to FLOAT64
    df['priceFrom'] = df['priceFrom'].astype('float64')
    df['priceTo'] = df['priceTo'].astype('float64')
    
    
    # STEP 3: Clean absent values
    # Replace NaN (Not a Number) with None
    df = df.replace(np.nan, None)
    
    
    # Return refined dataframe
    return df


# Add Instagram Stories Images To Dataframe function
def add_ig_stories_images_to_df(df:pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    
    # Create empty list of IG Stories images
    ig_stories_images = []
    
    # For each offer in offers dataframe:
    for i in range(len(df)):
        
        # Generate IG Stories image
        ig_stories_images.append(
            generate_ig_stories_image(
                offer_thumbnail= df.loc[i, 'offerThumbnail'],
                offer_name= df.loc[i, 'offerName'],
                offer_price_from= df.loc[i, 'priceFrom'],
                offer_price_to= df.loc[i, 'priceTo'],
                file_path= f'../temp/ig_stories_images/offer_{i}.png',
            )
        )
    
    # Add IG Stories images list as column in dataframe
    df['storiesImage'] = ig_stories_images
    
    # Drop (now) unnecessary columns
    df.drop(
        labels=['offerThumbnail', 'priceFrom', 'priceTo'],
        axis='columns',
        inplace=True
    )
    
    # Return dataframe
    return df