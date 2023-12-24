
'''from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import sys 
import os 






import requests
import json
import os

#with DAG("my_dag", start_date=(2023,12,20),schedule_interval="@daily",catchup=False)as dag:


# Define the default dag arguments.
default_args = {
    'owner': 'admin',
    'depends_on_past': False,
    'email': ['mekmeskassa@gmail.com'],
    'start_date': datetime(2023,12,21),
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
    catchup=False,
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

'''




from datetime import datetime, timedelta
from airflow import DAG
#from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python import PythonOperator

# Define default_args dictionary to specify the default parameters of the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Instantiate a DAG with the defined default_args
dag = DAG(
    'traffic_flow',
    default_args=default_args,
    description='A simple example DAG',
    schedule_interval=timedelta(days=1),  # Set the schedule interval to run daily
)


def task_a_function():
    print("Extracting Data")

task_a_task = PythonOperator(
    task_id='Extract',
    python_callable=task_a_function,
    dag=dag,
)


def task_b_function():
    print("loading data")

task_b_task = PythonOperator(
    task_id='load',
    python_callable=task_b_function,
    dag=dag,
)
def task_c_function():
    print("transforming data")

task_c_task = PythonOperator(
    task_id='transform',
    python_callable=task_c_function,
    dag=dag,
)


# Define the order and dependencies between tasks in the DAG
task_a_task >> task_b_task >> task_c_task
