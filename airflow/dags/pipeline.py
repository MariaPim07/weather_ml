import os
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import timedelta, datetime
from script.extract_data import extract_data
from script.tranform_data import transform_data
from script.train import train

default_args = {
    'retries': 2,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    dag_id='data_pipeline',
    start_date=datetime(2025, 3, 1),
    schedule_interval='0 0 1 * *',
    default_args=default_args,
    catchup=False
)

extract_data_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag
)

transform_data_task = PythonOperator(
    task_id='tranform_data',
    python_callable=transform_data,
    dag=dag
)

train_task = PythonOperator(
    task_id='train',
    python_callable=train,
    dag=dag
)

extract_data_task >> transform_data_task >> train_task