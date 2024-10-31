# Blockchain Data Streaming 

## Table of Contents
- [Introduction](#introduction)
- [System Architecture](#system-architecture)
- [Technologies](#technologies)
- [Getting Started](#getting-started)


## Introduction

This repository contains a personal project designed to enhance my skills in Data Engineering. It covers each stage from data ingestion to processing and finally to storage, utilizing a robust tech stack that includes Apache Airflow, Python, Apache Kafka, Apache Zookeeper, Apache Spark, and Cassandra. 

## System Architecture
![System Architecture](https://github.com/hunglk25/blockchain-data-streaming/blob/653c49b350cfe5c4e7de31d59d7cbcf6a9ac38c4/image.png)

The project is designed with the following components:

- **Data Source**: We use Coingecko API to take data about blockchain for our pipeline.
- **Apache Airflow**: Responsible for orchestrating the pipeline and storing fetched data in a PostgreSQL database.
- **Amazon S3**: Storage destination for processed data.

## Technologies

- Apache Airflow
- Python
- PostgreSQL
- Docker
- Amazon S3

## Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/hunglk25/real-time-data-streaming.git](https://github.com/hunglk25/blockchain-data-streaming.git
    ```

2. Navigate to the project directory:
    ```bash
    cd blockchain-data-streaming
    ```
3. Run virtual environment:
    ```bash
    source venv/bin/activate
    ```

4. Modify the file ```config/config.conf```

5. Run Docker Compose to spin up the services:
    ```bash
    docker compose up
    ```
