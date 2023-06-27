from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

dag_parameters = {
    "0wner": "jose",
    "start_date": datetime(2023, 6, 26),
    "catchup": False,
}


def get_ibge_info():
    from classes.Ibge import Regiao, MesoRegiao, MicroRegiao

    regiao = Regiao()
    mesoregiao = MesoRegiao()
    microregiao = MicroRegiao()

    regiao.get_data()
    mesoregiao.get_data()
    microregiao.get_data()

    regiao.save_data("regiao.json")
    mesoregiao.save_data("mesoregiao.json")
    microregiao.save_data("microregiao.json")


def get_mongodb_info():
    from classes.Mongodb import MongoDB
    from classes.Utility import Utility
    from classes.Aws import S3
    import json

    mongodb_client = MongoDB()
    utility = Utility()
    s3 = S3()
    criterial = {"sexo": "Mulher", "idade": {"$gte": 20, "$lte": 40}}

    result_list = mongodb_client.get_data(criterial)

    result_parsed = utility.parse_json(result_list)
    s3.write_file_in_bucket(f"mongodb/data.json", json.dumps(result_parsed))


with DAG(
    dag_id="pipeline",
    default_args=dag_parameters,
    description="Dag responsable from get IBGE and MongoDB info, send to Bucket and transform to DW.",
    tags=["mongodb", "api_rest", "s3"],
    schedule=None,
) as dag:
    start_pipeline = EmptyOperator(task_id="start_pipeline")

    get_ibge_info = PythonOperator(
        task_id="get_ibge_info",
        python_callable=get_ibge_info,
    )

    get_mongodb_info = PythonOperator(
        task_id="get_mongodb_info",
        python_callable=get_mongodb_info,
    )

    end_pipeline = EmptyOperator(task_id="end_pipeline")

    # Orchestration
    start_pipeline >> get_ibge_info
    start_pipeline >> get_mongodb_info
    get_ibge_info >> end_pipeline
    get_mongodb_info >> end_pipeline
