import pandas as pd

# Transform
def calculate_total_of_sales(df: pd.DataFrame, new_column:str, col1:str, col2:str) -> pd.DataFrame:
    df[new_column] = df[col1] * df[col2]
    return df
