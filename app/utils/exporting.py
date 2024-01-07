# External imports
from pandas.core.frame import DataFrame
from pyarrow import Table
from pyarrow.parquet import ParquetWriter


# DataFrame to Parquet function
def df_to_parquet(
    input_df:DataFrame|None = None,
    output_folder:str|None = None,
    output_file_name:str|None = None
) -> None:
    """
    Exports a pandas DataFrame object as a parquet file.

    Parameters:
    - input_df (DataFrame): a pandas dataframe object;
    - output_folder (str): path to folder where export file will appear;
    - output_file_name (str): name of the export file.

    Returns nothing.
    """
    # Create pyarrow Table obj from input df
    table = Table.from_pandas(input_df)
    
    # Mount path to output file
    output_file_path = f'{output_folder}{output_file_name}.parquet'

    # Get a ParquetWriter obj to output file
    pqwriter = ParquetWriter(where=f'{output_file_path}', schema=table.schema)
    
    # Add table to parquet file
    pqwriter.write_table(table=table)
    
    # Close parquet file
    pqwriter.close()
    
    # Return nothing
    return None