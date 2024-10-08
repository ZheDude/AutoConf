import json

class BGPgenerator:
    def __init__(self, bgp_data, template_file):
        # Store the whole BGP configuration as JSON-like objects
        self.bgp_data = bgp_data

        # Assign values to instance variables
        self.neighbor = bgp_data["neighbor"]
        self.networks = bgp_data["networks"]
        self.timer_bgp = bgp_data["timer_bgp"]
        self.hold_time = 90  # Default hold time, can be adjusted

        # Store the path to the template file
        self.template_file = template_file

    # Method to generate network statements
    def generate_network_statements(self):
        network_statements = "\n".join([f"network {network['network']} mask {network.get('subnetmask', network.get('submask', ''))}" for network in self.networks])
        return network_statements

    # Method to generate neighbor settings
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

    # Method to generate the BGP script by substituting the template
    def generate_script(self, local_as):
        # Read the template file
        try:
            with open(self.template_file, 'r') as file:
                template = file.read()

            # Generate BGP neighbor configuration
            neighbor_configs = "\n".join([self.generate_neighbor_config(neigh) for neigh in self.neighbor])

            # Generate network advertisement statements
            network_statements = self.generate_network_statements()

            # Replace placeholders in the template
            bgp_script = template.replace("${local_as}", str(local_as)) \
                                 .replace("${ip_of_neighbor}", self.neighbor[0]['ip_of_neighbor']) \
                                 .replace("${neighbor_as}", str(self.neighbor[0]['as'])) \
                                 .replace("${update_source}", self.neighbor[0]['update_source']) \
                                 .replace("${next_hop_self}", "neighbor {} next-hop-self".format(self.neighbor[0]['ip_of_neighbor']) if self.neighbor[0].get("next_hop_self") else "") \
                                 .replace("${route_reflector}", "neighbor {} route-reflector-client".format(self.neighbor[0]['ip_of_neighbor']) if self.neighbor[0].get("route_reflector") else "") \
                                 .replace("${default_originate}", "neighbor {} default-originate".format(self.neighbor[0]['ip_of_neighbor']) if self.neighbor[0].get("default_originate") else "") \
                                 .replace("${network_statements}", network_statements) \
                                 .replace("${timer_bgp}", str(self.timer_bgp)) \
                                 .replace("${hold_time}", str(self.hold_time))

            return bgp_script

        except FileNotFoundError:
            return f"Template file '{self.template_file}' not found."



bgp_data = {
    "neighbor": [
        {
            "ip_of_neighbor": "192.168.0.1",
            "as": 100,
            "update_source": "Loopback1",
            "next_hop_self": True,
            "route_reflector": True,
            "default_originate": True
        }
    ],
    "networks":[
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
    "local_as": 100
}

if __name__ == "__main__":

    # Instantiate the BGPgenerator class with the bgp_data
    bgp_gen = BGPgenerator(bgp_data, "Configurations/bgp_template.txt")

    # Generate and display the BGP configuration script based on the template
    local_as = 65000  # Local Autonomous System number
    bgp_script = bgp_gen.generate_script(local_as)
    print(bgp_script)
