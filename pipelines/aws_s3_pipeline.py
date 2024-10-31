from etls.aws_etl import connect_to_s3, create_bucket_if_not_exist, upload_data_to_s3
from utils.constants import AWS_BUCKET_NAME, AWS_BUCKET_FILENAME
from airflow import DAG

def upload_s3_pipeline(ti):
    df = ti.xcom_pull(task_ids='blockchain_extraction', key='return_value')

    s3 = connect_to_s3()
    create_bucket_if_not_exist(s3, AWS_BUCKET_NAME)
    upload_data_to_s3(s3, df, AWS_BUCKET_NAME, AWS_BUCKET_FILENAME)