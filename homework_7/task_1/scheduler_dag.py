from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from app_processing import AppProcessing

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
    start_date=datetime(2021, 5, 13, 20, 14),
    default_args=default_args
)

t1 = PythonOperator(
    task_id='scheduler_processing',
    dag=dag,
    python_callable=callable,
    provide_context=True
)
