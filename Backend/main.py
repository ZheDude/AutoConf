from Switch_configs.switches import PortsecurityGenerator
from Switch_configs.switches import AccessInterfacesGenerator
from Switch_configs.switches import EdgePortGenerator
from Switch_configs.switches import Etherchannelgenerator
from Switch_configs.switches import STPGenerator
from Switch_configs.switches import TrunkGenerator
from Switch_configs.switches import VlanGenerator
from Switch_configs.switches import VTPGenerator

def main():
    from connections import SSHConnection
    from switch_meta_vars import switch_meta_vars
    switch = switch_meta_vars("172.16.2.126", "cisco", "cisco")
    print("Interfaces:")
    print(switch.extract_interfaces())
    print("Neighbors:")
    print(switch.extract_neighbors())
    #dev1 = SSHConnection("172.16.2.126", "cisco", "cisco")
    #dev1.send_command_imprvd("configure terminal\n    ")




vlan_data = {
    "VLAN": [
        {
            "number": 10,
            "name": "VLAN_NAME"
        },
        {
            "number": 20,
            "name": "VLAN_NAME"
        },
        {
            "number": 30,
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
            "hello_timer": "1",
            "max_age": "10",
            "vlan": ["10", "20", "30"],
            "forward_timer": "7"
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


if __name__ == '__main__':
    main()
