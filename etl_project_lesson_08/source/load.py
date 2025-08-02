import pandas as pd

# Load
def load_df(df:pd.DataFrame, load_path:str):
    return df.to_csv(load_path)