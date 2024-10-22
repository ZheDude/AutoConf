import json


class ConfigProcessor:
    def __init__(self, config_data):
        self.config_data = config_data

    def process_config(self):
        json_outputs = []

        for item in self.config_data:
            for key, value in item.items():
                json_str = json.dumps({key: value}, indent=4)
                json_outputs.append(json_str)

        return json_outputs

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"File '{file_path}' not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"


def get_element_names(config_data: list) -> list[str]:
    top_level_names: list = list()
    for entry in config_data:
        top_level_names.append(list(entry.keys())[0])

    return top_level_names






if __name__ == "__main__":
    config_data = read_file("Configurations/Example_Json.json")
    config_data = json.loads(config_data)
    processor = ConfigProcessor(config_data)
    json_outputs = processor.process_config()
    top_level_names: list = get_element_names(config_data)

    for json_output in json_outputs:
        print("----------------")
        json_list: list = json.loads(json_output)
        print(json_list)



