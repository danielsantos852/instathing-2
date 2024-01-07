# Imports
import config as cfg
from utils import (df_from_parquet, 
                   get_available_devices, 
                   connect_to_device,
                   launch_ig_app, 
                   post_ig_story,
                   time_sleep)


# Global variables
INPUT_PARQUET = (f'{cfg.DEFAULT_TEMP_PARQUET_FOLDER}'
                 f'{cfg.DEFAULT_LOAD_READY_PARQUET_FILE_NAME}.parquet')
LINK_STICKER_TEXT = cfg.DEFAULT_LINK_STICKER_TEXT


# Main Function
def main():
    
    # Load offers dataframe
    df_offers = df_from_parquet(input_parquet=INPUT_PARQUET)

    # Connect to first available android device
    device = connect_to_device(device_serial=get_available_devices()[0].serial)

    # Restart IG app on device
    # launch_ig_app(device=device,
    #               force_stop=True)

    # For each offer in offers dataframe:
    for i in range(len(df_offers)):

        # Post offer as IG Story
        post_ig_story(
            device=device,
            img_src=df_offers.loc[i, 'igStoryImage'],
            stckr_url=df_offers.loc[i, 'offerLink'],
            stckr_text=LINK_STICKER_TEXT,
            close_friends=True,
            restart_ig_app=True,
        )

        # Wait a little
        time_sleep(5.0, 0.0)


# If this is the script being run, call main()
if __name__=='__main__': main()