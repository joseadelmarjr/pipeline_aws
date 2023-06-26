class local:
    def __init__(self, type):
        self.type = type
        available_types = ["regioes", "mesorregioes", "microrregioes"]
        if type in available_types:
            self.url = f"https://servicodados.ibge.gov.br/api/v1/localidades/{type}"
        else:
            print("Tipo nao cadastrado")

    def get_data(self):
        import requests

        data = requests.request("GET", self.url)
        data = data.json()
        self.data = data

    def save_data(self, local_file):
        from classes.Aws import S3
        import json

        s3 = S3()
        s3.write_file_in_bucket(f"ibge_{self.type}/data.json", json.dumps(self.data))


class Regiao(local):
    def __init__(self):
        super().__init__("regioes")


class MesoRegiao(local):
    def __init__(self):
        super().__init__("mesorregioes")


class MicroRegiao(local):
    def __init__(self):
        super().__init__("microrregioes")
