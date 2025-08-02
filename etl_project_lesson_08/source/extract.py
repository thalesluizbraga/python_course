import os # para navegar nas pastas
import glob # para listar os arquivos que estao no path passado
import pandas as pd

# Extract
def read_files(path: str) -> pd.DataFrame:
    files = glob.glob(os.path.join(path, '*.json'))
    df_list = []
    for file in files:
        df_file = pd.read_json(file)
        df_list.append(df_file)
    df = pd.concat(df_list).reset_index()
    return df




