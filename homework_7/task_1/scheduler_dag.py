import os
import sys

from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from app_processing import AppProcessing

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


def callable(**kwargs):
    AppProcessing().run()


default_args = {
    'owner': 'airflow',
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'retries': 2
}

dag = DAG(
    'scheduler_dag',
    description='Scheduler DAG',
    schedule_interval='@hourly',
    start_date=datetime(2021, 5, 13, 22, 32),
    default_args=default_args
)

t1 = PythonOperator(
    task_id='scheduler_processing',
    dag=dag,
    python_callable=callable,
    provide_context=True
)
