# External imports
import pandas as pd
import numpy as np

# Internal imports
from .ig_image_processing import generate_ig_stories_image


# Add Instagram Stories Images To Dataframe function
def add_ig_stories_images_to_df(df_offers:pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    
    # Create empty list of IG Stories images
    ig_stories_images = []
    
    # For each offer in offers dataframe:
    for i in range(len(df_offers)):
        
        # Generate IG Stories image
        ig_stories_images.append(
            generate_ig_stories_image(
                offer_thumbnail= df_offers.loc[i, 'offerThumbnail'],
                offer_name= df_offers.loc[i, 'offerName'],
                offer_price_from= df_offers.loc[i, 'priceFrom'],
                offer_price_to= df_offers.loc[i, 'priceTo'],
                file_path= f'../temp/ig_stories_images/offer_{i}.png',
            )
        )
    
    # Add IG Stories images list as column in dataframe        
    df_offers['storiesImage'] = ig_stories_images
    
    # Return dataframe
    return df_offers


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