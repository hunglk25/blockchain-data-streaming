FROM apache/airflow:latest-python3.9

COPY requirements.txt /opt/airflow/

USER airflow

RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt