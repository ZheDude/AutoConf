class BGPgenerator:
    def __init__(self, bgp_data_inside, template_file):
        self.bgp_data = bgp_data_inside

        self.neighbor = bgp_data_inside["neighbor"]
        self.local_as = bgp_data_inside['local_as']
        self.networks = bgp_data_inside["networks"]
        self.timer_bgp = bgp_data_inside["timer_bgp"]
        self.hold_time = bgp_data_inside["hold_time"]
        self.template_file = template_file

    def generate_network_statements(self):
        network_statements = "\n".join(
            [f"network {network['network']} mask {network.get('subnetmask', network.get('submask', ''))}" for network in
             self.networks])
        return network_statements

    def generate_neighbor_config(self, neighbor):
        config = f"neighbor {neighbor['ip_of_neighbor']} remote-as {neighbor['as']}\n"
        config += f"neighbor {neighbor['ip_of_neighbor']} update-source {neighbor['update_source']}\n"

        # Optional parameters
        if neighbor.get("next_hop_self"):
            config += f"neighbor {neighbor['ip_of_neighbor']} next-hop-self\n"
        if neighbor.get("route_reflector"):
            config += f"neighbor {neighbor['ip_of_neighbor']} route-reflector-client\n"
        if neighbor.get("default_originate"):
            config += f"neighbor {neighbor['ip_of_neighbor']} default-originate\n"

        return config

    def generate_script(self):
        try:
            with open(self.template_file, 'r') as file:
                template = file.read()

            neighbor_configs = "\n".join([self.generate_neighbor_config(neigh) for neigh in self.neighbor])
            network_statements = self.generate_network_statements()

            # Replace placeholders in the template
            bgp_script = template.replace("${local_as}", str(self.local_as)) \
                .replace("${neighbour_configurations}", neighbor_configs) \
                .replace("${network_statements}", network_statements) \
                .replace("${timer_bgp}", str(self.timer_bgp)) \
                .replace("${hold_time}", str(self.hold_time))

            return bgp_script

        except FileNotFoundError:
            return f"Template file '{self.template_file}' not found."


# Example BGP configuration data
bgp_data = {
    "neighbor": [
        {
            "ip_of_neighbor": "192.168.0.1",
            "as": 100,
            "update_source": "Loopback1",
            "next_hop_self": True,
            "route_reflector": True,
            "default_originate": True
        },
        {
            "ip_of_neighbor": "6.6.6.6",
            "as": 1234,
            "update_source": "Loopback1",
            "next_hop_self": True,
            "route_reflector": False,
            "default_originate": False
        }
    ],
    "networks": [
        {
            "network": "10.0.0.0",
            "subnetmask": "0.0.0.255"
        },
        {
            "network": "172.0.0.0",
            "submask": "0.0.0.3"
        }
    ],
    "timer_bgp": 30,
    "hold_time": 180,
    "local_as": 696969
}

if __name__ == "__main__":
    bgp_gen = BGPgenerator(bgp_data, "../Configurations/bgp_template.txt")
    bgp_script = bgp_gen.generate_script()
    print(bgp_script)
