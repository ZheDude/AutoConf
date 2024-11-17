import json


class VlanGenerator:
    def __init__(self, vlan_data, template_file):
        self.template_file = template_file
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
    def __init__(self, vtp_data, template_file):
        self.template_file = template_file
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
        fin_str = (f"vtp version {self.vtp['version']}\n" +
                   f"vtp mode {self.vtp['mode']}\n" +
                   f"vtp domain {self.vtp['domain']}\n" +
                   f"vtp password {self.vtp['password']}\n")
        if self.vtp['pruning']:
            fin_str += "vtp pruning\n"
        if self.vtp['is_primary']:
            if self.vtp['vlan']:
                fin_str += f"do-exec vtp primary vlan {self.vtp['vlan']}\n"
            else:
                fin_str += "do-exec vtp primary\n"
        return fin_str


class STPGenerator:
    def __init__(self, stp_data, template_file):
        self.template_file = template_file
        self.stp = {}
        for enumerate in stp_data['STP']:
            self.stp['mode'] = enumerate['mode']
            self.stp['priority'] = enumerate['priority']
            self.stp['hello_timer'] = enumerate['hello_timer']
            self.stp['forward_delay'] = enumerate['forward_delay']
            self.stp['max_age'] = enumerate['max_age']
            self.stp['interface'] = enumerate['interface']
            self.stp['vlan'] = enumerate['vlan']

    def display_config(self):
        print(self.stp['mode'])
        print(self.stp['priority'])
        print(self.stp['hello_timer'])
        print(self.stp['forward_delay'])
        print(self.stp['max_age'])
        print(self.stp['interface'])
        print(self.stp['vlan'])

    def generate_script(self):
        interface_string = ""
        for interface in self.stp['interface']:
            interface_string += (f"interface {interface['type']} {interface['number']}\n" +
                                 f"spanning-tree portfast\n" +
                                 f"spanning-tree bpduguard\n")

        vlan_string = ""
        for vlan in self.stp['vlan']:
            vlan_string += (f"spanning-tree vlan {vlan['number']} priority {vlan['priority']}\n")

        fin_str = (f"spanning-tree mode {self.stp['mode']}\n" +
                   f"spanning-tree priority {self.stp['priority']}\n" +
                   f"spanning-tree hello-time {self.stp['hello_timer']}\n" +
                   f"spanning-tree forward-time {self.stp['forward_delay']}\n" +
                   f"spanning-tree max-age {self.stp['max_age']}\n" +
                   f"{interface_string}" +
                   f"{vlan_string}")
        return fin_str


class PortsecurityGenerator:
    def __init__(self, portsecurity_data, template_file):
        self.template_file = template_file
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
    def __init__(self, trunk_data, template_file):
        self.template_file = template_file
        self.trunk = {}
        for enumerate in trunk_data['TRUNK']:
            self.trunk['interface'] = enumerate['interface']
            self.trunk['allowed_vlan'] = enumerate['allowed_vlan']
            self.trunk['native_vlan'] = enumerate['native_vlan']
            self.trunk['encapsulation'] = enumerate['encapsulation']
            self.trunk['mode'] = enumerate['mode']
            self.trunk['description'] = enumerate['description']
            self.trunk['shutdown'] = enumerate['shutdown']

    def display_config(self):
        print(self.trunk['interface'])
        print(self.trunk['allowed_vlan'])
        print(self.trunk['native_vlan'])
        print(self.trunk['encapsulation'])
        print(self.trunk['mode'])
        print(self.trunk['description'])
        print(self.trunk['shutdown'])

    def generate_script(self):
        vlan_string = ""
        for vlan in self.trunk['allowed_vlan']:
            vlan_string += f"switchport trunk allowed vlan {vlan}\n"

        fin_str = (f"interface {self.trunk['interface']}\n" +
                   f"switchport trunk allowed vlan {vlan_string}\n" +
                   f"switchport trunk native vlan {self.trunk['native_vlan']}\n" +
                   f"switchport trunk encapsulation {self.trunk['encapsulation']}\n" +
                   f"switchport mode {self.trunk['mode']}\n" +
                   f"switchport description {self.trunk['description']}\n" +
                   f"shutdown {self.trunk['shutdown']}")
        return fin_str


class Etherchannelgenerator:
    def __init__(self, etherchannel_data, template_file):
        self.template_file = template_file
        self.group = {}
        for enumerate in etherchannel_data['Etherchannel']:
            self.group['number'] = enumerate['number']
            self.group['mode'] = enumerate['mode']
            self.group['interfaces'] = []
            for x in enumerate['interface']:
                self.group['interfaces'].append(x)

    def display_config(self):
        print(self.group['number'])
        print(self.group['mode'])
        print(self.group['interfaces'])

    def generate_script(self):
        interface_range_string = " ".join(self.group['interfaces'])

        fin_str = (f"interface range {interface_range_string}\n" +
                   f"port-channel group {self.group['number']}\n" +
                   f"port-channel mode {self.group['mode']}")
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

stp_data = {
    "STP": [
        {
            "mode": "rapid-pvst",
            "priority": 4096,
            "hello_timer": 10,
            "forward_delay": 10,
            "max_age": 10,
            "interface": [
                {
                    "type": "GigabitEthernet0",
                    "number": 0,
                    "portfast": True,
                    "bpduguard": True
                }
            ],
            "vlan": [
                {
                    "number": 10,
                    "name": "VLAN_NAME",
                    "priority": 10
                }
            ]
        }
    ]
}

portsecurity_data = {
    "Portsecurity": [
        {
            "interface": "GigabitEthernet0/0",
            "maximum": 10,
            "violation": "shutdown",
            "mac_address": "mac_address"
        }
    ]
}

trunk_data = {
    "TRUNK": [
        {
            "interface": "GigabitEthernet0/0",
            "allowed_vlan": [
                10,
                20
            ],
            "native_vlan": 10,
            "encapsulation": "dot1q",
            "mode": "on",
            "description": "This is a description",
            "shutdown": False
        }
    ]
}

etherchannel_data = {
    "Etherchannel": [
        {
            "number": 1,
            "interface": [
                "GigabitEthernet0/0",
                "GigabitEthernet0/1"
            ],
            "mode": "active"
        }
    ]
}

# [
#   
#   
#   {
#     "Interface": [
#       {
#         "type": "GigabitEthernet0",
#         "number": 0,
#         "ip_address": "0.0.0.0",
#         "subnetmask": "255.255.255.255",
#         "description": "This is a description",
#         "shutdown": false,
#         "ospf": {
#           "area_id": 10,
#           "cost": 10,
#           "priority": 10,
#           "network_type": "broadcast",
#           "authentication": {
#             "key_chain": "KEY_CHAIN",
#             "message_digest": true
#           }
#         }
#       }
#     ]
#   },

# ]


if __name__ == "__main__":
    etherchannel_gen = Etherchannelgenerator(etherchannel_data, "../Configurations/etherchannel_template.txt")
    etherchannel_script = etherchannel_gen.generate_script()
    print(etherchannel_script, "\n")
    vlan_gen = VlanGenerator(vlan_data, "../Configurations/vlan_template.txt")
    vlan_script = vlan_gen.generate_script()
    print(vlan_script, "\n")
    vtp_gen = VTPGenerator(vtp_data, "../Configurations/vtp_template.txt")
    vtp_script = vtp_gen.generate_script()
    print(vtp_script, "\n")
    stp_gen = STPGenerator(stp_data, "../Configurations/stp_template.txt")
    stp_script = stp_gen.generate_script()
    print(stp_script, "\n")
    portsecurity_gen = PortsecurityGenerator(portsecurity_data, "../Configurations/portsecurity_template.txt")
    portsecurity_script = portsecurity_gen.generate_script()
    print(portsecurity_script, "\n")
    trunk_gen = TrunkGenerator(trunk_data, "../Configurations/trunk_template.txt")
    trunk_script = trunk_gen.generate_script()
    print(trunk_script, "\n")
