import json
from typing import Tuple, List, Any

from Backend.Router_configs.bgp import BGPgenerator
from Backend.Router_configs.dhcp import DHCPGenerator
from Backend.Router_configs.gre import GRETunnelGenerator
from Backend.Router_configs.hsrp import HSRPGenerator
from Backend.Router_configs.interface import InterfaceGenerator
from Backend.Router_configs.key_chain import KEYCHAINgenerator
from Backend.Router_configs.ospf import OSPFgenerator
from Backend.Router_configs.rip import RIPGenerator
from Backend.Router_configs.static_routes import StaticRoutesGenerator
from Backend.Switch_configs.switches import PortsecurityGenerator
from Backend.Switch_configs.switches import AccessInterfacesGenerator
from Backend.Switch_configs.switches import EdgePortGenerator
from Backend.Switch_configs.switches import Etherchannelgenerator
from Backend.Switch_configs.switches import STPGenerator
from Backend.Switch_configs.switches import TrunkGenerator
from Backend.Switch_configs.switches import VlanGenerator
from Backend.Switch_configs.switches import VTPGenerator


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


def get_list_of_konfigurations(json_content: str) -> tuple[str, list[Any]]:
    config_data = json.loads(json_content)
    processor = ConfigProcessor(config_data)
    json_outputs = processor.process_config()
    top_level_names: list = get_element_names(config_data)
    konfigurations_liste = list()
    # print(json_outputs)
    # print(type(json_outputs))
    # print(len(json_outputs))
    ssh_ip: str = ""

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
        ### Switch Configurations
        elif name == "VLAN":
            vlan_data = json_list.get("VLAN")
            # print(vlan_data)
            vlan_data = {"VLAN": vlan_data}
            vlan_gen = VlanGenerator(vlan_data)
            vlan_script = vlan_gen.generate_script()
            konfigurations_liste.append(vlan_script)
        elif name == "VTP":
            vtp_data = json_list.get("VTP")
            vtp_data = {"VTP": vtp_data}
            vtp_gen = VTPGenerator(vtp_data)
            vtp_script = vtp_gen.generate_script()
            konfigurations_liste.append(vtp_script)
        elif name == "STP":
            stp_data = json_list.get("STP")
            # print(stp_data)
            stp_data = {"STP": stp_data}
            stp_gen = STPGenerator(stp_data)
            stp_script = stp_gen.generate_script()
            konfigurations_liste.append(stp_script)
        elif name == "AccessInterfaces":
            access_interfaces_data = json_list.get("AccessInterfaces")
            # print(access_interfaces_data)
            access_interfaces_data = {"AccessInterfaces": access_interfaces_data}
            access_interfaces_gen = AccessInterfacesGenerator(access_interfaces_data)
            access_interfaces_script = access_interfaces_gen.generate_script()
            konfigurations_liste.append(access_interfaces_script)
        elif name == "EdgePorts":
            edge_port_data = json_list.get("EdgePorts")
            # print(edge_port_data)
            edge_port_data = {"EdgePorts": edge_port_data}
            edge_port_gen = EdgePortGenerator(edge_port_data)
            edge_port_script = edge_port_gen.generate_script()
            konfigurations_liste.append(edge_port_script)
        elif name == "EtherChannel":
            etherchannel_data = json_list.get("EtherChannel")
            # print(etherchannel_data)
            etherchannel_data = {"EtherChannel": etherchannel_data}
            etherchannel_gen = Etherchannelgenerator(etherchannel_data)
            etherchannel_script = etherchannel_gen.generate_script()
            konfigurations_liste.append(etherchannel_script)
        elif name == "Portsecurity":
            port_security_data = json_list.get("Portsecurity")
            # print(port_security_data)
            port_security_data = {"Portsecurity": port_security_data}
            port_security_gen = PortsecurityGenerator(port_security_data)
            port_security_script = port_security_gen.generate_script()
            konfigurations_liste.append(port_security_script)
        elif name == "Trunks":
            trunk_data = json_list.get("Trunks")
            # print(trunk_data)
            trunk_data = {"Trunks": trunk_data}
            trunk_gen = TrunkGenerator(trunk_data)
            trunk_script = trunk_gen.generate_script()
            konfigurations_liste.append(trunk_script)
        elif name == "SSH":
            ssh_data = json_list.get("SSH")
            ssh_ip = ssh_data['ip']

    return ssh_ip, konfigurations_liste


if __name__ == '__main__':
    data = read_file("Configurations/Example_Json.json")
    ssh_and_config = get_list_of_konfigurations(data)
    ip = ssh_and_config[0]
    konfig_liste = ssh_and_config[1]
    for element in konfig_liste:
        print(element)
