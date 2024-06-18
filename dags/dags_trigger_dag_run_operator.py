from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow import DAG
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id='dags_trigger_dag_run_operator',
    schedule= None,
    start_date=pendulum.datetime(2024, 6, 18, tz='Asia/Seoul'),
) as dag:
    start_task = BashOperator(
        task_id='start_task',
        bash_command='echo "start!"',
    )

    trigger_dag_task = TriggerDagRunOperator(
        task_id='trigger_dag_task',
        trigger_dag_id='dags_python_operator',
        trigger_run_id='ne',
        logical_date=None,
        reset_dag_run=True,
        wait_for_completion=False,
        poke_interval=60,
        allowed_states=['success'],
        failed_states=None,
    )

    start_task >> trigger_dag_task