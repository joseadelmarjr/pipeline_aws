from classes.Mongodb import MongoDB
from classes.Utility import Utility
from classes.Aws import S3
import json

mongodb_client = MongoDB()
utility = Utility()
s3 = S3()
criterial = {"sexo": "Mulher", "idade": {"$gte": 20, "$lte": 40}}

result_list = list(mongodb_client.get_data(criterial))

result_parsed = utility.parse_json(result_list)
s3.write_file_in_bucket(f"mongodb/data.json", json.dumps(result_parsed))
