import datetime
from airflow.decorators import dag
from airflow.operators.bash import BashOperator
import pendulum

@dag(dag_id='dags_bash_operator_decorator',
    start_date=pendulum.datetime(2023, 1, 1, tz="Asia/Seoul"),
    schedule="0 0 * * *",
    catchup=False,
    tags=['homework']
)
def generate_dag():
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami"
    )
    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_cmmand="echo $HOSTNAME"
    )


    bash_t1 >> bash_t2

