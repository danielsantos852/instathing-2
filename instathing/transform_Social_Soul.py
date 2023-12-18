# Imports
import config as cfg
from utils import df_from_xml, dataframe_refine, gen_ig_story_imgs_from_df, df_to_parquet


# Global Variables
PATH_TO_INPUT_XML_FILE = cfg.PATH_TO_EXAMPLE_SOCIAL_SOUL_INPUT_XML_FILE
PATH_TO_OUTPUT_FOLDER = cfg.DEFAULT_PATH_TO_TMP_PARQUET_FOLDER
OUTPUT_PARQUET_FILE_NAME = cfg.IG_READY_DF_FILE_NAME


# Main Function
def main():

    # Generate raw offers dataframe from XML file
    df_offers_raw = df_from_xml(path=PATH_TO_INPUT_XML_FILE)

    # Refine offers dataframe
    df_offers_refined = dataframe_refine(df=df_offers_raw)

    # Add IG Stories images to dataframe (and drop unnecessary columns)
    df_offers_ig_ready = gen_ig_story_imgs_from_df(df=df_offers_refined)
    
    # Export Instagram-ready offers dataframe to parquet file
    df_to_parquet(input_df=df_offers_ig_ready,
                  output_folder_path=PATH_TO_OUTPUT_FOLDER,
                  output_file_name=OUTPUT_PARQUET_FILE_NAME)


# If this is the script being run, call Main Function
if __name__=='__main__':
    main()