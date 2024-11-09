import json

from Backend.bgp import BGPgenerator
from Backend.ospf import OSPFgenerator
from Backend.rip import RIPGenerator


# TODO SAI the following things have to be done
# key-chain
# gre
# interface
# static routes
# hsrp
# dhcp
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
    print(top_level_names)
    konfigurations_liste = list()
    for json_output in json_outputs:
        print("----------------")
        json_list: dict = json.loads(json_output)
        print(json_list)
        name = list(json_list.keys())[0]
        json_string = str(json_list)

        if name == "DHCP":
            ...
        elif name == "OSPF":
            list_ospf = json_list.get(name)
            for element in list_ospf:
                # print(element, "hello")
                ospf_gen = OSPFgenerator(element, "Configurations/ospf_template.txt")
                # fertiges OSPF script
                ospf_script = ospf_gen.generate_script()
                konfigurations_liste.append(ospf_script)
                # print(ospf_script)

        elif name == "RIP":
            rip_gen = RIPGenerator(json_list, "Configurations/rip_template.txt")
            # fertiges RIP script
            rip_script = rip_gen.generate_script()
            # print(rip_script)
            konfigurations_liste.append(rip_script)
        elif name == "BGP":
            bgp_data = json_list.get("BGP")
            bgp_gen = BGPgenerator(bgp_data, "Configurations/bgp_template.txt")
            bgp_script = bgp_gen.generate_script()
            konfigurations_liste.append(bgp_script)

        print(name)
    for element in konfigurations_liste:
        print("-----------")
        print(element)
