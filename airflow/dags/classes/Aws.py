import boto3
from dotenv import load_dotenv
import os


class S3:
    def __init__(self):
        load_dotenv()
        self.ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY")
        self.SECRET_ACCESS_KEY = os.getenv("AWS_ACCESS_SECRET_KEY")
        self.bucket = "datalake-igti-example"

    def __get_connection(self):
        s3 = boto3.resource(
            "s3",
            aws_access_key_id=self.ACCESS_KEY_ID,
            aws_secret_access_key=self.SECRET_ACCESS_KEY,
        )
        return s3

    def write_file_in_bucket(self, file_path, content):
        s3 = self.__get_connection()
        object = s3.Object(self.bucket, file_path)
        object.put(Body=content)
