class VlanGenerator:
    def __init__(self, vlan_data):
        self.vlan = {}
        for enumerate in vlan_data['VLAN']:
            self.vlan['number'] = enumerate['number']
            self.vlan['name'] = enumerate['name']

    def display_config(self):
        print(self.vlan['number'])
        print(self.vlan['name'])

    def generate_script(self):
        fin_str = (f"vlan {self.vlan['number']}\n" +
                   f"name {self.vlan['name']}")
        return fin_str


class VTPGenerator:
    def __init__(self, vtp_data):
        self.vtp = {}
        for enumerate in vtp_data['VTP']:
            self.vtp['version'] = enumerate['version']
            self.vtp['mode'] = enumerate['mode']
            self.vtp['domain'] = enumerate['domain']
            self.vtp['password'] = enumerate['password']
            self.vtp['pruning'] = enumerate['pruning']
            self.vtp['is_primary'] = enumerate['is_primary']
            self.vtp['vlan'] = enumerate.get('vlan')

    def display_config(self):
        print(self.vtp['version'])
        print(self.vtp['mode'])
        print(self.vtp['domain'])
        print(self.vtp['password'])
        print(self.vtp['pruning'])
        print(self.vtp['is_primary'])

    def generate_script(self):
        fin_str = (f"vtp mode {self.vtp['mode']}\n" +
                   f"vtp domain {self.vtp['domain']}\n" +
                   f"vtp password {self.vtp['password']}\n" +
                   f"vtp version {self.vtp['version']}\n")

        if self.vtp['pruning']:
            fin_str += "vtp pruning\n"
        if self.vtp['is_primary']:
            if self.vtp['vlan']:
                fin_str += f"do-exec vtp primary vlan {self.vtp['vlan']}\n"
            else:
                fin_str += "do-exec vtp primary\n"
        return fin_str


class STPGenerator:
    def __init__(self, stp_data):
        self.stp = {}
        for enumerate in stp_data['STP']:
            self.stp['mode'] = enumerate['mode']
            self.stp['priority'] = enumerate['priority']
            self.stp['hello_timer'] = enumerate['hello_timer']
            self.stp['forward_timer'] = enumerate['forward_timer']
            self.stp['max_age'] = enumerate['max_age']
            self.stp['vlan'] = enumerate['vlan']

    def display_config(self):
        print(self.stp['mode'])
        print(self.stp['priority'])
        print(self.stp['hello_timer'])
        print(self.stp['forward_timer'])
        print(self.stp['max_age'])
        print(self.stp['vlan'])

    def generate_script(self):
        fin_str = (f"spanning-tree mode {self.stp['mode']}\n")
        for vlan in self.stp['vlan']:
            fin_str += f"spanning-tree vlan {vlan} priority {self.stp['priority']}\n"
            fin_str += f"spanning-tree vlan {vlan} hello-time {self.stp['hello_timer']}\n"
            fin_str += f"spanning-tree vlan {vlan} forward-time {self.stp['forward_timer']}\n"
            fin_str += f"spanning-tree vlan {vlan} max-age {self.stp['max_age']}\n"
        return fin_str


class PortsecurityGenerator:
    # WARNING: port has to be static (not dtp)
    def __init__(self, portsecurity_data):
        self.portsecurity = {}
        for enumerate in portsecurity_data['Portsecurity']:
            self.portsecurity['interface'] = enumerate['interface']
            self.portsecurity['maximum'] = enumerate['maximum']
            self.portsecurity['violation'] = enumerate['violation']
            self.portsecurity['mac_address'] = enumerate['mac_address']

    def display_config(self):
        print(self.portsecurity['interface'])
        print(self.portsecurity['maximum'])
        print(self.portsecurity['violation'])
        print(self.portsecurity['mac_address'])

    def generate_script(self):
        fin_str = (f"interface {self.portsecurity['interface']}\n" +
                   f"switchport port-security maximum {self.portsecurity['maximum']}\n" +
                   f"switchport port-security violation {self.portsecurity['violation']}\n" +
                   f"switchport port-security mac-address {self.portsecurity['mac_address']}")
        return fin_str


class TrunkGenerator:
    def __init__(self, trunk_data):
        self.trunk = {}
        for enumerate in trunk_data['Trunks']:
            self.trunk['interfaces'] = []
            for interface in trunk_data['Trunks']['Interfaces']:
                self.trunk['interfaces'].append(interface)
            self.trunk['interface_ranges'] = []
            for interface_range in trunk_data['Trunks']['InterfaceRanges']:
                self.trunk['interface_ranges'].append(interface_range)

    def display_config(self):
        print(self.trunk['interfaces'])
        print(self.trunk['interface_ranges'])

    def generate_script(self):
        fin_str = ""
        for interface in self.trunk['interfaces']:
            fin_str += (f"interface {interface['name']}\n" +
                        f"switchport trunk allowed vlan {interface['allowed_vlan']}\n" +
                        f"switchport trunk native vlan {interface['native_vlan']}\n" +
                        f"switchport trunk encapsulation {interface['encapsulation']}\n" +
                        f"switchport mode {interface['mode']}\n" +
                        f"no shutdown\n")
        for interface_range in self.trunk['interface_ranges']:
            fin_str += (
                        f"interface range {interface_range['startInterface']} - {interface_range['endInterface'][-1]}\n" +
                        f"switchport trunk allowed vlan {interface_range['allowed_vlan']}\n" +
                        f"switchport trunk native vlan {interface_range['native_vlan']}\n" +
                        f"switchport trunk encapsulation {interface_range['encapsulation']}\n" +
                        f"switchport mode {interface_range['mode']}\n" +
                        f"no shutdown\n")
        return fin_str


class Etherchannelgenerator:
    def __init__(self, etherchannel_data):
        self.etherchannel = {}
        for enumerate in etherchannel_data['EtherChannels']:
            self.etherchannel['interfaces'] = []
            for interface in enumerate['Interfaces']:
                self.etherchannel['interfaces'].append(interface)
            self.etherchannel['interface_ranges'] = []
            for interface_range in enumerate['InterfaceRanges']:
                self.etherchannel['interface_ranges'].append(interface_range)
            self.etherchannel['mode'] = enumerate['mode']
            self.etherchannel['number'] = enumerate['number']

    def display_config(self):
        print(self.etherchannel['interfaces'])
        print(self.etherchannel['interface_ranges'])
        print(self.etherchannel['mode'])
        print(self.etherchannel['number'])

    def generate_script(self):
        fin_str = ""
        for interface in self.etherchannel['interfaces']:
            fin_str += (f"interface {interface['name']}\n" +
                        f"channel-group {self.etherchannel['number']} mode {self.etherchannel['mode']}\n" +
                        f"no  shutdown\n")
        for interface_range in self.etherchannel['interface_ranges']:
            fin_str += (
                        f"interface range {interface_range['startInterface']} - {interface_range['endInterface'][-1]}\n" +
                        f"channel-group {self.etherchannel['number']} mode {self.etherchannel['mode']}\n" +
                        f"no shutdown\n")
        return fin_str


class EdgePortGenerator:
    def __init__(self, edgeport_data):
        self.edgeport = {}
        for enumerate in edgeport_data['EdgePorts']:
            self.edgeport['interfaces'] = []
            for interface in edgeport_data['EdgePorts']['Interfaces']:
                self.edgeport['interfaces'].append(interface)
            self.edgeport['interface_ranges'] = []
            for interface_range in edgeport_data['EdgePorts']['InterfaceRanges']:
                self.edgeport['interface_ranges'].append(interface_range)

    def display_config(self):
        print(self.edgeport['interfaces'])
        print(self.edgeport['interface_ranges'])

    def generate_script(self):
        fin_str = ""
        for interface in self.edgeport['interfaces']:
            fin_str += (f"interface {interface['name']}\n")
            if interface['portfast']:
                fin_str += "spanning-tree portfast edge\n"
            if interface['bpduguard']:
                fin_str += "spanning-tree bpduguard enable\n"
        for interface_range in self.edgeport['interface_ranges']:
            fin_str += (
                f"interface range {interface_range['startInterface']} - {interface_range['endInterface'][-1]}\n")
            if interface['portfast']:
                fin_str += "spanning-tree portfast edge\n"
            if interface['bpduguard']:
                fin_str += "spanning-tree bpduguard enable\n"

        return fin_str


class AccessInterfacesGenerator:
    def __init__(self, access_interfaces_data):
        self.access_interfaces = {}
        for enumerate in access_interfaces_data['AccessInterfaces']:
            self.access_interfaces['interfaces'] = []
            for interface in access_interfaces_data['AccessInterfaces']['Interfaces']:
                self.access_interfaces['interfaces'].append(interface)
            self.access_interfaces['interface_ranges'] = []
            for interface_range in access_interfaces_data['AccessInterfaces']['InterfaceRanges']:
                self.access_interfaces['interface_ranges'].append(interface_range)

    def display_config(self):
        print(self.access_interfaces['interfaces'])
        print(self.access_interfaces['interface_ranges'])

    def generate_script(self):
        fin_str = ""
        for interface in self.access_interfaces['interfaces']:
            fin_str += (f"interface {interface['name']}\n" +
                        f"switchport mode access\n" +
                        f"switchport access vlan {interface['vlan']}\n" +
                        f"no shutdown\n")
        for interface_range in self.access_interfaces['interface_ranges']:
            fin_str += (
                        f"interface range {interface_range['startInterface']} - {interface_range['endInterface'][-1]}\n" +
                        f"switchport mode access\n" +
                        f"switchport access vlan {interface_range['vlan']}\n" +
                        f"no shutdown\n")
        return fin_str


vlan_data = {
    "VLAN": [
        {
            "number": 10,
            "name": "VLAN_NAME"
        }
    ]
}

vtp_data = {
    "VTP": [
        {
            "version": 3,
            "mode": "server",
            "domain": "DOMAIN",
            "password": "PASSWORD",
            "pruning": True,
            "is_primary": True,
            "vlan": 10
        },
        {
            "version": 3,
            "mode": "server",
            "domain": "DOMAIN",
            "password": "PASSWORD",
            "pruning": True,
            "is_primary": True
        }
    ]
}

# stp_data = {
#     "STP": [
#         {
#             "mode": "rapid-pvst",
#             "priority": 4096,
#             "hello_timer": 10,
#             "forward_delay": 10,
#             "max_age": 10,
#             "interface": [
#                 {
#                     "type": "GigabitEthernet0",
#                     "number": 0,
#                     "portfast": True,
#                     "bpduguard": True
#                 }
#             ],
#             "vlan": [
#                 {
#                     "number": 10,
#                     "name": "VLAN_NAME",
#                     "priority": 10
#                 }
#             ]
#         }
#     ]
# }

portsecurity_data = {
    "Portsecurity": [
        {
            "interface": "GigabitEthernet0/0",
            "maximum": 10,
            "violation": "shutdown",
            "mac_address": "sticky"
        }
    ]
}

stp_data = {
    "STP": [
        {
            "mode": "Rapid-PVST",
            "priority": "4096",
            "hello_timer": "10",
            "max_age": "10",
            "vlan": ["10", "20", "30"],
            "forward_timer": "10"
        }
    ]}

edgeport_data = {
    "EdgePorts": {
        "Interfaces": [
            {
                "name": "Gig0/1",
                "portfast": True,
                "bpduguard": True
            },
            {
                "name": "Gig0/0",
                "portfast": True,
                "bpduguard": True
            }
        ],
        "InterfaceRanges": [
            {
                "startInterface": "Gig0/2",
                "endInterface": "Gig0/3",
                "portfaste": True,
                "bpduguard": False
            },
            {
                "startInterface": "Gig1/2",
                "endInterface": "Gig1/3",
                "portfaste": True,
                "bpduguard": False
            }
        ]
    }
}

etherchannel_data = {
    "EtherChannels": [
        {
            "Interfaces": [
                {
                    "name": "Gig0/0"
                }
            ],
            "InterfaceRanges": [
                {
                    "startInterface": "Gig3/2",
                    "endInterface": "Gig3/3"
                }
            ],
            "mode": "Passive",
            "number": "1"
        }
    ]
}

trunk_data = {
    "Trunks": {
        "Interfaces": [
            {
                "name": "Gig0/1",
                "allowed_vlan": "10,30,40",
                "native_vlan": "20",
                "encapsulation": "Dot1q",
                "mode": "Dynamic Desirable",
                "shutdown": True
            },
            {
                "name": "Gig3/1",
                "allowed_vlan": "10,30,40",
                "native_vlan": "20",
                "encapsulation": "Dot1q",
                "mode": "Dynamic Desirable",
                "shutdown": True
            }
        ],
        "InterfaceRanges": [
            {
                "startInterface": "Gig0/2",
                "endInterface": "Gig0/3",
                "allowed_vlan": "10,20",
                "native_vlan": "10",
                "encapsulation": "Dot1q",
                "mode": "Dynamic Desirable",
                "shutdown": True
            },
            {
                "startInterface": "Gig2/2",
                "endInterface": "Gig2/3",
                "allowed_vlan": "10,20",
                "native_vlan": "10",
                "encapsulation": "Dot1q",
                "mode": "Dynamic Desirable",
                "shutdown": True
            }
        ]
    }}

access_interfaces_data = {
    "AccessInterfaces": {
        "Interfaces": [
            {
                "name": "Gig0/2",
                "allowed_vlan": "",
                "native_vlan": "",
                "encapsulation": "",
                "mode": "",
                "shutdown": True,
                "vlan": "20"
            },
            {
                "name": "Gig0/3",
                "allowed_vlan": "",
                "native_vlan": "",
                "encapsulation": "",
                "mode": "",
                "shutdown": True,
                "vlan": "20"
            }
        ],
        "InterfaceRanges": [
            {
                "startInterface": "Gig0/2",
                "endInterface": "Gig0/3",
                "allowed_vlan": "",
                "native_vlan": "",
                "encapsulation": "",
                "mode": "",
                "shutdown": True,
                "vlan": "20"
            }
        ]
    }
}

# trunk_data = {
#     "TRUNK": [
#         {
#             "interface": "GigabitEthernet0/0",
#             "allowed_vlan": [
#                 10,
#                 20
#             ],
#             "native_vlan": 10,
#             "encapsulation": "dot1q",
#             "mode": "on",
#             "description": "This is a description",
#             "shutdown": False
#         }
#     ]
# }

# etherchannel_data = {
#     "Etherchannel": [
#         {
#             "number": 1,
#             "interface": [
#                 "GigabitEthernet0/0",
#                 "GigabitEthernet0/1"
#             ],
#             "mode": "active"
#         }
#     ]
# }

if __name__ == "__main__":
    vlan_gen = VlanGenerator(vlan_data)
    vlan_script = vlan_gen.generate_script()
    print(vlan_script, "\n")

    vtp_gen = VTPGenerator(vtp_data)
    vtp_script = vtp_gen.generate_script()
    print(vtp_script, "\n")

    stp_gen = STPGenerator(stp_data)
    stp_script = stp_gen.generate_script()
    print(stp_script, "\n")

    trunk_gen = TrunkGenerator(trunk_data)
    trunk_script = trunk_gen.generate_script()
    print(trunk_script, "\n")

    portsecurity_gen = PortsecurityGenerator(portsecurity_data)
    portsecurity_script = portsecurity_gen.generate_script()
    print(portsecurity_script, "\n")

    etherchannel_gen = Etherchannelgenerator(etherchannel_data)
    etherchannel_script = etherchannel_gen.generate_script()
    print(etherchannel_script, "\n")

    edgeport_gen = EdgePortGenerator(edgeport_data)
    edgeport_script = edgeport_gen.generate_script()
    print(edgeport_script, "\n")

    access_interfaces_gen = AccessInterfacesGenerator(access_interfaces_data)
    access_interfaces_script = access_interfaces_gen.generate_script()
    print(access_interfaces_script, "\n")
