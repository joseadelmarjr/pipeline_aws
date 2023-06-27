from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.master("spark://spark:7077")
    .appName(f"notebook_spark")
    .getOrCreate()
)
