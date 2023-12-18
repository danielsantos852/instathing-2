# Imports
import config as cfg
from utils import df_from_parquet, get_available_devices, connect_to_device, post_ig_story


# Global variables
DF_SRC = f'{cfg.DEFAULT_PATH_TO_TMP_PARQUET_FOLDER}{cfg.IG_READY_DF_FILE_NAME}.parquet'
LINK_STICKER_TEXT = cfg.DEFAULT_LINK_STICKER_TXT


# Main Function
def main():
    
    # Load offers dataframe
    df_offers = df_from_parquet(path=DF_SRC)

    # Connect to first available android device
    device = connect_to_device(get_available_devices()[0].serial)

    # For each offer in offers dataframe:
    for i in range(len(df_offers)):

        # Post offer as IG Story
        post_ig_story(
            device=device,
            img_src=df_offers.loc[i, 'storiesImage'],
            stckr_url=df_offers.loc[i, 'offerLink'],
            stckr_text=LINK_STICKER_TEXT,
            close_friends=True,
            restart_ig_app=True,
        )


# If this is the script being run
if __name__=='__main__':

    # Call Main Function
    main()