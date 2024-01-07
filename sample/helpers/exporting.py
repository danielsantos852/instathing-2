# Imports
from pandas.core.frame import DataFrame
from pyarrow import Table
from pyarrow.parquet import ParquetWriter


def export_df_to_parquet(
    df:DataFrame|None = None,
    output_dir:str|None = None,
    output_file_name:str|None = None
) -> str:
    """
    Exports a pandas dataframe to a parquet file

    :param df: Dataframe to export
    :type df: pandas.core.frame.DataFrame
    :param output_dir: Output directory
    :type output_dir: str|None
    :param output_file_name: Output file name
    :type output_file_name: str|None
    :return: Output file path
    :rtype: str
    """
    # Generate output file path
    output_file_path = f'{output_dir}{output_file_name}.parquet'

    # Create pyarrow table with df data
    table = Table.from_pandas(df)

    # Create empty output parquet file
    pqwriter = ParquetWriter(where=output_file_path,
                             schema=Table.schema)

    # Write pyarrow table to parquet file
    pqwriter.write_table(table)
    
    # Close parquet file
    pqwriter.close()
    
    # Return output file path
    return output_file_path