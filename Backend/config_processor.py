import json

from Backend.Router_configs.bgp import BGPgenerator
from Backend.Router_configs.dhcp import DHCPGenerator
from Backend.Router_configs.gre import GRETunnelGenerator
from Backend.Router_configs.hsrp import HSRPGenerator
from Backend.Router_configs.interface import InterfaceGenerator
from Backend.Router_configs.key_chain import KEYCHAINgenerator
from Backend.Router_configs.ospf import OSPFgenerator
from Backend.Router_configs.rip import RIPGenerator
from Backend.Router_configs.static_routes import StaticRoutesGenerator


# TODO SAI default console mode soll configuration mode sein (end, conf t)

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


def get_list_of_konfigurations(json_content: str) -> []:
    config_data = json.loads(json_content)
    processor = ConfigProcessor(config_data)
    json_outputs = processor.process_config()
    top_level_names: list = get_element_names(config_data)
    konfigurations_liste = list()
    # print(json_outputs)
    # print(type(json_outputs))
    # print(len(json_outputs))

    for index, json_output in enumerate(json_outputs):

        json_list: dict = json.loads(json_output)

        name = list(json_list.keys())[0]
        # print(name)

        if name == "OSPF":
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
        elif name == "Key-Chain":
            key_chain_data = json_list.get("Key-Chain")
            # print(key_chain_data)
            key_chain_gen = KEYCHAINgenerator(key_chain_data)
            key_chain_script = key_chain_gen.generate_script()
            konfigurations_liste.append(key_chain_script)
        elif name == "Static-Routes":
            static_route_data = json_list.get("Static-Routes")
            # print(static_route_data)
            static_route_gen = StaticRoutesGenerator(static_route_data)
            static_route_script = static_route_gen.generate_script()
            konfigurations_liste.append(static_route_script)
        elif name == "GRE":
            gre_data = json_list.get("GRE")
            # print(gre_data)
            gre_gen = GRETunnelGenerator(gre_data)
            gre_script = gre_gen.generate_script()
            konfigurations_liste.append(gre_script)
        elif name == "Interface":
            interface_data = json_list.get("Interface")
            # print(interface_data)
            interface_gen = InterfaceGenerator(interface_data)
            interface_script = interface_gen.generate_script()
            konfigurations_liste.append(interface_script)
        elif name == "HSRP":
            hsrp_data = json_list.get("HSRP")
            # print(hsrp_data)
            hsrp_gen = HSRPGenerator(hsrp_data)
            hsrp_script = hsrp_gen.generate_script()
            konfigurations_liste.append(hsrp_script)
        elif name == "DHCP":
            dhcp_data = json_list.get("DHCP")
            # print(dhcp_data)
            dhcp_gen = DHCPGenerator(dhcp_data)
            dhcp_script = dhcp_gen.generate_script()
            konfigurations_liste.append(dhcp_script)

        ### MEHMET TUST DU HIER DEINE COD

    return konfigurations_liste


if __name__ == '__main__':
    data = read_file("Configurations/Example_Json.json")
    konfig_liste = get_list_of_konfigurations(data)
    # print(konfig_liste)
    for element in konfig_liste:
        ...
        # print(element)
