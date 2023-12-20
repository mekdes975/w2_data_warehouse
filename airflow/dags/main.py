
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import sys 
import os 




from src.extract_data_source import get_data
from src.transform_data import transform_data
from src.load_data import load_data
import requests
import json
import os

#with DAG("my_dag", start_date=(2023,12,20),schedule_interval="@daily",catchup=False)as dag:


# Define the default dag arguments.
default_args = {
    'owner': 'admin',
    'depends_on_past': False,
    'email': ['mekmeskassa@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


# Define the dag, the start date and how frequently it runs.
# I chose the dag to run everday by .
dag = DAG(
    dag_id='new_dag',
    default_args=default_args,
    start_date=datetime(2023, 12, 19),
    schedule_interval= "@daily" ) 


# First task is to query get the weather from openweathermap.org.
task1 = PythonOperator(
    task_id='get_data',
    provide_context=True,
    python_callable=get_data,
    dag=dag)


# Second task is to transform the data
task2 = PythonOperator(
    task_id='load_data',
    provide_context=True,
    python_callable=load_data,
    dag=dag)

# Third task is to transform data into the database.
task3 = PythonOperator(
    task_id='transform_data',
    provide_context=True,
    python_callable=transform_data,
    dag=dag)

# Set task1 "upstream" of task2
# task1 must be completed before task2 can be started
task1 >> task2 >> task3