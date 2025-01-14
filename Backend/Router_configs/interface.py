class InterfaceGenerator:
    def __init__(self, interface_data):
        self.data = interface_data

    def generate_script(self):
        commands = []

        for iface in self.data:
            interface = iface.get("interface")
            ip_address = iface.get("ip_address")
            subnet_mask = iface.get("subnetmask")
            description = iface.get("description")
            shutdown = iface.get("shutdown", False)
            ospf = iface.get("ospf", {})

            if not all([interface, ip_address, subnet_mask]):
                print(f"Skipping incomplete interface entry: {iface}")
                continue

            # Base interface configuration
            commands.append(f"interface {interface}")
            if description:
                commands.append(f"description {description}")
            commands.append(f"ip address {ip_address} {subnet_mask}")
            if shutdown:
                commands.append("shutdown")
            else:
                commands.append("no shutdown")

            # OSPF Configuration
            if ospf:
                area_id = ospf.get("area_id")
                cost = ospf.get("cost")
                priority = ospf.get("priority")
                network_type = ospf.get("network_type")
                authentication = ospf.get("authentication", {})

                if area_id is not None:
                    commands.append(f"ip ospf area {area_id}")
                if cost is not None:
                    commands.append(f"ip ospf cost {cost}")
                if priority is not None:
                    commands.append(f"ip ospf priority {priority}")
                if network_type:
                    commands.append(f"ip ospf network {network_type}")
                if authentication:
                    key_chain = authentication.get("key_chain")
                    message_digest = authentication.get("message_digest", False)
                    if key_chain:
                        commands.append(f"ip ospf authentication key-chain {key_chain}")
                    if message_digest:
                        commands.append("ip ospf authentication message-digest")

            commands.append("")

        return "\n".join(commands)


if __name__ == "__main__":
    data = [
        {
            "interface": "GigabitEthernet0/123",
            "ip_address": "0.0.0.0",
            "subnetmask": "255.255.255.255",
            "description": "This is a description",
            "shutdown": False,
            "ospf": {
                "area_id": 10,
                "cost": 10,
                "priority": 10,
                "network_type": "broadcast",
                "authentication": {
                    "key_chain": "KEY_CHAIN"

                }
            }
        },
        {
            "interface": "GigabitEthernet0/1",
            "ip_address": "0.0.0.0",
            "subnetmask": "255.255.255.255",
            "description": "This is a description",
            "shutdown": False
        }
    ]

    iface_config = InterfaceGenerator(data)
    script = iface_config.generate_script()
    print(script)
