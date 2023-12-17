# Imports
import config as cfg
from utils import dataframe_from_xml, dataframe_refine, dataframe_generate_ig_story_images, dataframe_to_parquet


# Global Variables
PATH_TO_INPUT_XML_FILE = cfg.PATH_TO_SOCIAL_SOUL_INPUT_XML_EXAMPLE
PATH_TO_OUTPUT_PARQUET_FILE = f'{cfg.DEFAULT_PATH_FOR_TMP_PARQUET_FOLDER}df_offers_ig_ready.parquet'


# Main Function
def main():

    # Generate raw offers dataframe from XML file
    df_offers_raw = dataframe_from_xml(path=PATH_TO_INPUT_XML_FILE)

    # Refine offers dataframe
    df_offers_refined = dataframe_refine(df=df_offers_raw)

    # Add IG Stories images to dataframe (and drop unnecessary columns)
    df_offers_ig_ready = dataframe_generate_ig_story_images(df=df_offers_refined)

    # Export Instagram-ready offers dataframe to parquet file
    dataframe_to_parquet(df=df_offers_ig_ready, path_to_file=PATH_TO_OUTPUT_PARQUET_FILE)


# If this is the script being run, call Main Function
if __name__=='__main__':
    main()