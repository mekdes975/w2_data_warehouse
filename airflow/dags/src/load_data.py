import psycopg2
import sys
import os

current_directory = os.getcwd()
parent_directory = os.path.abspath(os.path.join(current_directory, '.'))

if parent_directory not in sys.path:
    sys.path.insert(0, parent_directory)


from sqlalchemy import create_engine
from src.extract_data_source import CSVDataReader


import psycopg2
from psycopg2 import sql
from sqlalchemy import create_engine

csv_reader = CSVDataReader('/home/hp/Downloads/20181024_d1_0830_0900(2).csv')
csv_reader.read_data()
df_track = csv_reader.df_track
df_Trajectory = csv_reader.df_Trajectory

# Define your PostgreSQL connection parameters
connection_params = {
    "dbname": 'trafficflow',
    "user": "postres",
    "password": "1234",
    "host": "localhost",
    "port": "5438"
}

# Establish a connection to PostgreSQL
conn = psycopg2.connect(**connection_params)
cursor = conn.cursor()

# Create a schema if it doesn't exist
schema_name = 'trafficdata'
cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {schema_name}")
conn.commit()


# Define table creation query for the track table
create_track_table_query = """
    CREATE TABLE IF NOT EXISTS trafficdata.track (
        track_id INT,
        type VARCHAR(50),
        avg_speed FLOAT,
        traveled_d FLOAT
    )
"""


# Define table creation query for the trajectory table
create_trajectory_table_query = """
    CREATE TABLE IF NOT EXISTS trafficdata.trajectory (
        track_id INT,
        lat FLOAT,
        lon FLOAT,
        speed FLOAT,
        lon_acc FLOAT,
        lat_acc FLOAT,
        time FLOAT
    )
"""


# Execute table creation queries
cursor.execute(create_track_table_query)
cursor.execute(create_trajectory_table_query)
conn.commit()

# Create SQLAlchemy engine
engine = create_engine('postgresql://postgres:1234@localhost:5438/trafficflow')

# Load df_track and df_Trajectory into respective tables
df_track.to_sql('track', engine, schema=schema_name, if_exists='replace', index=False)
df_Trajectory.to_sql('trajectory', engine, schema=schema_name, if_exists='replace', index=False)

# Close the cursor and connection
cursor.close()
conn.close()

