# Imports
from utils import dataframe_from_parquet
from utils import get_available_devices, connect_to_device, post_instagram_story


# Global variables
DF_SRC = './temp/parquet/df_offers_ig_ready.parquet'
OFFER_IMG_SRC = './resources/story_template_720x1280_final.png'
OFFER_IMG_DEST = '/storage/emulated/0/DCIM/temp/offer.png'
LINK_STICKER_TEXT = 'ver oferta'


# Main Function
def main():
    
    # Load offers dataframe
    df_offers = dataframe_from_parquet(path=DF_SRC)

    # Connect to first available android device
    device = connect_to_device(get_available_devices()[0].serial)

    # For each offer in offers dataframe:
    for i in range(len(df_offers)):

        # Post offer as IG Story
        post_instagram_story(
            device=device,
            offer_img_src=df_offers.loc[i, 'storiesImage'],
            offer_img_dest=OFFER_IMG_DEST,
            offer_url=df_offers.loc[i, 'offerLink'],
            link_sticker_text=LINK_STICKER_TEXT,
            close_friends=True,
            restart_app=True,
        )


# If this is the script being run
if __name__=='__main__':

    # Call Main Function
    main()