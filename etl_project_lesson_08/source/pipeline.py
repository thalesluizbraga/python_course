#%%
from etl import pipeline
import os


extract_path = 'C:/Users/User/Documents/repos/python_course/etl_project_lesson_08/data'
load_path = 'C:/Users/User/Documents/repos/python_course/etl_project_lesson_08/data/data.csv'
pipeline(extract_path=extract_path, load_path=load_path,output_format='csv')
