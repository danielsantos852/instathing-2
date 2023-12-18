# Imports
import config as cfg
from utils import df_from_xml, refine_df, gen_ig_story_imgs_for_df, df_to_parquet


# Global Variables
PATH_TO_INPUT_XML_FILE = cfg.PATH_TO_EXAMPLE_SOCIAL_SOUL_INPUT_XML_FILE
PATH_TO_OUTPUT_FOLDER = cfg.DEFAULT_PATH_TO_TMP_PARQUET_FOLDER
OUTPUT_PARQUET_FILE_NAME = cfg.DEFAULT_IG_READY_PARQUET_FILE_NAME


# Main Function
def main():

    # Load XML file with offer data as a pandas dataframe
    df_offers_raw = df_from_xml(input_xml=PATH_TO_INPUT_XML_FILE)

    # Clean offer data in dataframe
    df_offers_refined = refine_df(df=df_offers_raw)

    # Generate IG story offer images for the dataframe
    df_offers_ig_ready = gen_ig_story_imgs_for_df(df=df_offers_refined)
    
    # Export IG-ready dataframe to a parquet file
    df_to_parquet(input_df=df_offers_ig_ready,
                  output_folder=PATH_TO_OUTPUT_FOLDER,
                  output_file_name=OUTPUT_PARQUET_FILE_NAME)


# If this is the script being run, call main()
if __name__=='__main__': main()