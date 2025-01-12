class DHCPGenerator:
    def __init__(self, dhcp_data):
        self.data = dhcp_data

    def generate_script(self):
        commands = []

        for entry in self.data:
            pool = entry.get("pool")
            network = entry.get("network")
            subnetmask = entry.get("subnetmask")
            default_router = entry.get("default_router")
            dns = entry.get("dns")
            exclude = entry.get("exclude", [])
            exclude_range = entry.get("exclude-range", [])
            exclude_range_start = ""
            exclude_range_end = ""

            lease = entry.get("lease")

            for ip in exclude:
                commands.append(f"ip dhcp excluded-address {ip}")

            for exclude_element in exclude_range:
                exclude_range_start = exclude_element.get("start")
                exclude_range_end = exclude_element.get("end")
                commands.append(f"ip dhcp excluded-address {exclude_range_start} {exclude_range_end}")

            if not all([pool, network, subnetmask, default_router]):
                print(f"Skipping incomplete DHCP entry: {entry}")
                continue



            commands.append(f"ip dhcp pool {pool}")
            commands.append(f"network {network} {subnetmask}")
            commands.append(f"default-router {default_router}")
            if dns:
                commands.append(f"dns-server {dns}")
            if lease:
                commands.append(f"lease {lease}")
            commands.append("")

        return "\n".join(commands)


if __name__ == "__main__":
    data = [
        {
            "pool": "POOL",
            "network": "1.1.1.0",
            "subnetmask": "255.255.255.0",
            "default_router": "1.1.1.1",
            "dns": "as.dasd",
            "exclude": [
                "1.1.1.1"
            ],
            "lease": 10
        },
        {
            "pool": "POOL123123",
            "network": "1.1.1.0",
            "subnetmask": "255.255.255.0",
            "default_router": "1.1.1.1",
            "dns": "as.dasd",
            "exclude": ["1.1.1.1"],
            "exclude-range": [
                {
                    "start": "1.1.1.1",
                    "end": "2.2.2.2"
                },
                {
                    "start": "1.1.1.1",
                    "end": "3.2.2.2"
                }
            ],
            "lease": 10
        },
        {
            "pool": "",
            "network": "",
            "subnetmask": "",
            "default_router": "",
            "dns": "",
            "exclude": ["1.1.1.1"],
            "exclude-range": [
                {
                    "start": "6.2.1.1",
                    "end": "2.2.2.2"
                },
                {
                    "start": "1.1.1.1",
                    "end": "3.2.2.2"
                }
            ],
            "lease": 0
        }
    ]
    dhcp_gen = DHCPGenerator(data)
    script = dhcp_gen.generate_script()
    print(script)
