FROM apache/airflow:2.6.2-python3.10 AS base
LABEL mantainer="Engineering Tools <jose.adelmar@hotmail.com>"

ENV AIRFLOW_VERSION=2.6.2
ENV AIRFLOW__CORE__DEFAULT_TASK_RETRIES=2
ENV AIRFLOW__SCHEDULER__CATCHUP_BY_DEFAULT="False"
ENV AIRFLOW__WEBSERVER__WARN_DEPLOYMENT_EXPOSURE="False"
ENV AIRFLOW__WEBSERVER__DEFAULT_UI_TIMEZONE="America/Sao_Paulo"
ENV AIRFLOW__CORE__MAX_ACTIVE_RUNS_PER_DAG=1

USER root
RUN apt-get update && \
  apt-get install -y \
  python3-distutils \
  python3-apt \
  libpq-dev \
  build-essential \
  wkhtmltopdf \
  xvfb

USER airflow
RUN pip install --upgrade pip setuptools wheel
COPY ./airflow/dags/ /opt/airflow/dags/
COPY ./airflow/include/ /opt/airflow/include/
COPY ./requirements/ /opt/requirements/

FROM base AS development
ENV ENVIRONMENT="development"
ENV AIRFLOW__WEBSERVER__INSTANCE_NAME="development"
ENV AIRFLOW__WEBSERVER__EXPOSE_CONFIG="True"
RUN pip install --no-cache-dir -r /opt/requirements/requirements_dev.txt
USER root
RUN mkdir -p /airflow_temp/
RUN chmod -R 777 /airflow_temp/
RUN chmod -R 777 /opt/
