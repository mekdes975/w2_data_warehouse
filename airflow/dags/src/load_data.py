import psycopg2
import sys
import os

current_directory = os.getcwd()
parent_directory = os.path.abspath(os.path.join(current_directory, '.'))

if parent_directory not in sys.path:
    sys.path.insert(0, parent_directory)


from sqlalchemy import create_engine
from src.extract_data_source import get_data



import psycopg2
from sqlalchemy import create_engine
import pandas as pd

# Load data from CSV files into DataFrames
data1 = get_data.get_data1  #  get_data1() returns DataFrame for track table
data2 = get_data.get_data2  #  get_data2() returns DataFrame for trajectory table

# Merge the DataFrames into a single DataFrame
merged_data = pd.concat([data1, data2], axis=1)  # Combine columns

# Create the connection string
engine = create_engine('postgresql://postgres:1234@localhost:5432/trafficflow')

# Load data into PostgreSQL table
merged_data.to_sql('trafficflow', engine, if_exists='replace', index=False)

   
