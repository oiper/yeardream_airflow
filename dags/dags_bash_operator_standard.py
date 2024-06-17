import datetime
from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator

@dag(start_date=datetime.datetime(2023, 1, 1, tz="Asia/Seoul"), schedule="0 0 * * *", catchup=False)
def generate_dag():
    EmptyOperator(tesk_id="first")
