# Imports
import pandas as pd
import numpy as np
from .image_manipulation import create_ig_story_image_from_offer


# Refine Dataframe function
def dataframe_refine(df:pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    
    # Select columns of interest and clip dataframe
    # (Comment/uncomment to clip/keep a column)
    df = df.loc[
        :,[
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
        ]
    ]

    # Cast prices from STR to FLOAT64
    df['priceFrom'] = df['priceFrom'].astype('float64')
    df['priceTo'] = df['priceTo'].astype('float64')

    # Clean empty cells (replace NaN with None)
    df = df.replace(np.nan, None)

    # Return dataframe
    return df


# Dataframe Generate IG Stories function
def dataframe_generate_ig_story_images(
    df:pd.core.frame.DataFrame,
    output_folder='./temp/images/'
) -> pd.core.frame.DataFrame:
    
    # Parameters
    path_to_story_template_image = './resources/images/story_template_720x1280_final.png'

    # Create empty list of IG Stories images
    ig_stories_images = []
    
    # For each offer in offers dataframe:
    for i in range(len(df)):
        
        # Generate IG Stories image
        ig_stories_images.append(
            create_ig_story_image_from_offer(
                base_image=path_to_story_template_image,
                offer_thumbnail= df.loc[i, 'offerThumbnail'],
                offer_name= df.loc[i, 'offerName'],
                offer_price_from= df.loc[i, 'priceFrom'],
                offer_price_to= df.loc[i, 'priceTo'],
                output_path= f'{output_folder}offer{str(i).zfill(3)}.png' # e.g.: 'offer001.png',
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