# External imports
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq


# Export Pandas DataFrame as Parquet function
def export_dataframe_as_parquet(df:pd.core.frame.DataFrame, path:str) -> None:
    
    # Create pyarrow table from pandas dataframe
    table = pa.Table.from_pandas(df)
    
    # Create parquet file
    pqwriter = pq.ParquetWriter(where=f'{path}.parquet', schema=table.schema)
    
    # Add table to parquet file
    pqwriter.write_table(table=table)
    
    # Close parquet file
    pqwriter.close()

    # Return nothing
    return None