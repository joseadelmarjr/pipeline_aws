import json
from bson import json_util


class Utility:
    def __init__(self):
        pass

    def save_json_to_file(self, data, local_file):
        with open(local_file, "a") as file:
            json.dump(data, file)
        file.close()
        file = open(local_file, "a")
        file.write("\n")
        file.close()

    def parse_json(self, data):
        return json.loads(json_util.dumps(data))
