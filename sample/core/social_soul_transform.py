# Imports

# Internal imports
from .context import config as cfg
from helpers import import_xml_as_df
                     
from utils import (df_from_xml, 
                   refine_df, 
                   gen_ig_story_imgs_for_df, 
                   df_to_parquet)


# Global Variables
INPUT_XML_PATH = cfg.SOCIAL_SOUL_EXAMPLE_XML_FILE
OUTPUT_PARQUET_FOLDER = cfg.DEFAULT_TEMP_PARQUET_FOLDER
OUTPUT_PARQUET_FILE_NAME = cfg.DEFAULT_LOAD_READY_PARQUET_FILE_NAME


# Main Function
def main():

    # Load XML file with offer data as a pandas dataframe
    df_offers_raw = df_from_xml(input_xml=INPUT_XML_PATH)

    # Clean offer data in dataframe
    df_offers_refined = refine_df(df=df_offers_raw)

    # Generate IG story offer images for the dataframe
    df_offers_ig_ready = gen_ig_story_imgs_for_df(df=df_offers_refined)
    
    # Export IG-ready dataframe to a parquet file
    df_to_parquet(input_df=df_offers_ig_ready,
                  output_folder=OUTPUT_PARQUET_FOLDER,
                  output_file_name=OUTPUT_PARQUET_FILE_NAME)


# If this is the script being run, call main()
if __name__=='__main__': main()