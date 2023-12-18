# External imports
from pandas.core.frame import DataFrame
import pyarrow as pa
import pyarrow.parquet as pq


# DataFrame to Parquet function
def df_to_parquet(
    input_df:DataFrame = None,
    output_folder:str = None,
    output_file_name:str = 'df_to_parquet_output'
) -> None:
    """
    Exports a pandas DataFrame object as a parquet file.

    Parameters:
        input_df (DataFrame): a pandas dataframe object
        output_folder (str): path to folder where export file will appear
        output_file_name (str): name of the export file

    Returns:
        None
    """
    # Create pyarrow Table obj from input df
    table = pa.Table.from_pandas(input_df)
    
    # Mount path to output file
    output_file_path = f'{output_folder}{output_file_name}.parquet'

    # Get a ParquetWriter obj to output file
    pqwriter = pq.ParquetWriter(where=f'{output_file_path}', schema=table.schema)
    
    # Add table to parquet file
    pqwriter.write_table(table=table)
    
    # Close parquet file
    pqwriter.close()
    
    # Return nothing
    return None