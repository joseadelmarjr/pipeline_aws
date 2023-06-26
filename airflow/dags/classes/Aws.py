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


# def escrever_em_arquivo_s3(bucket, nome_arquivo, conteudo):
#     access_key = "AKIARWZ2U4JE5UXAUGOX"
#     secret_key = "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"
#     s3 = boto3.resource(
#         "s3", aws_access_key_id=access_key, aws_secret_access_key=secret_key
#     )
#     objeto = s3.Object(bucket, nome_arquivo)
#     objeto.put(Body=conteudo)


# # Configurações do S3
# nome_bucket = "datalake-igti-example"  # Substitua pelo nome do seu bucket
# nome_arquivo = "caminho/nome-do-arquivo.txt"  # Substitua pelo caminho e nome do arquivo desejado no bucket
# conteudo_arquivo = "Conteúdo a ser escrito no arquivo"

# # Escrever o conteúdo no arquivo do S3
# escrever_em_arquivo_s3(nome_bucket, nome_arquivo, conteudo_arquivo)
