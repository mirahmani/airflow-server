from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def print_hello():
    return 'Hello'

def print_world():
    print('World')

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 2),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG('hello_world',
          default_args=default_args,
          description='A simple HelloWorld DAG',
          schedule_interval=timedelta(minutes=10),
          catchup=False,
          )

start_task = DummyOperator(
    task_id='start_task',
    dag=dag,
)

hello_task = PythonOperator(
    task_id='hello_task',
    python_callable=print_hello,
    dag=dag,
)

world_task = PythonOperator(
    task_id='world_task',
    python_callable=print_world,
    dag=dag,
)

start_task >> hello_task >> world_task
