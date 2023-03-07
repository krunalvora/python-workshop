from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    "depends_on_past": False,
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

with DAG(
    "first_dag",
    default_args=default_args,
    description="First dag",
    start_date=datetime(2023,3,6),
    catchup=False,
    tags=["first_dag"]
) as dag:
    t1 = BashOperator(
        task_id="print_date",
        bash_command="date"
    )

    t2 = BashOperator(
        task_id="print_date_again",
        bash_command="date"
    )

t1 >> t2