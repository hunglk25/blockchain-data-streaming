from airflow import DAG
from datetime import datetime
import os
import sys
from airflow.operators.python import PythonOperator
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pipelines.blockchain_pipelines import blockchain_pipeline
from pipelines.aws_s3_pipeline import upload_s3_pipeline
default_args = {
    'owner': 'hwnglk25',
    'start_date': datetime(2024, 10, 20)
}

file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG(
    dag_id = 'etl_blockchain_pipeline',
    default_args=default_args,
    schedule_interval='0 16 * * *',
    catchup=False,
    tags=['blockchain', 'etl', 'pipeline']
)


extract = PythonOperator(
    task_id = 'blockchain_extraction',
    python_callable=blockchain_pipeline,
    dag=dag
)

upload_to_s3 = PythonOperator(
    task_id = 'upload_to_s3',
    python_callable=upload_s3_pipeline,
    dag = dag
)

extract >> upload_to_s3