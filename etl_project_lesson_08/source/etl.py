#%%
import os # para navegar nas pastas
import glob # para listar os arquivos que estao no path passado
import pandas as pd
from loguru import logger


logger.add("C:/Users/User/Documents/repos/python_course/etl_project_lesson_08/etl_log.log", level="DEBUG", rotation="1 MB")

# Extract
def read_files(extract_path: str) -> pd.DataFrame:
    files = glob.glob(os.path.join(extract_path, '*.json'))

    if not files: # se nao houver arquivos json na lista files que usou o glob.glob pra buscar somente json files:
        logger.critical('json files not found')
        return pd.DataFrame()
    
    logger.info(f'{len(files)} JSON files found. Reading....')
    
    df_list = []
    for file in files:
        try: # Tenta ler os arquivos e se der pau em algum o codigo nao quebra porque ele vira exceçao
            df_file = pd.read_json(file)
            df_list.append(df_file)
            logger.info(f'Successfully read: {file}')
        except Exception as e:
            logger.exception(f'Failed to read file: {file}')

    if not df_list:
        logger.critical(f'All file reads failed.')

    df = pd.concat(df_list).reset_index()
    logger.info('Files successfully read and concatenated.')
    return df

# Transform
def calculate_total_of_sales(df: pd.DataFrame, new_column:str, col1:str, col2:str) -> pd.DataFrame:
    logger.info(f"Calculating column '{new_column}' as {col1} * {col2}")
    try:
        df[new_column] = df[col1] * df[col2]
        logger.debug(f'Calculation completed')
    except Exception as e:
        logger.exception(f'Error during calculation: {e}')
    return df

# Load
def load_df(df:pd.DataFrame, load_path:str, output_format:str):
        logger.info(f"Saving file to {load_path} as {output_format}")
        try:
            if output_format == 'csv':
                return df.to_csv(load_path)
            elif output_format == 'parquet':
                return df.to_parquet(load_path)
        except Exception as e:
            logger.debug('Format not supported. Please try another.')

def pipeline(extract_path:str, load_path:str, output_format:str):
    df = read_files(extract_path)
    df = calculate_total_of_sales(df=df,new_column='Total Venda', col1='Venda', col2='Quantidade')
    return load_df(df=df, load_path=load_path,output_format=output_format)

    
    
