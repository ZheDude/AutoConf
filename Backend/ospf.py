class OSPFgenerator:
    def __init__(self, ospf_data, template_file):
        self.ospf_data = ospf_data
        self.process_id = ospf_data["process_id"]
        self.router_id = ospf_data["router_id"]
        self.timer_dead = ospf_data["timer_dead"]
        self.timer_hello = ospf_data["timer_hello"]
        self.passive_interfaces = ospf_data["passive_interfaces"]
        self.networks = []
        for network in ospf_data["networks"]:
            network_json = {
                "network": network["network"],
                "area_id": network["area_id"],
                "wildcard": network["wildcard"]
            }
            self.networks.append(network_json)
        self.template_file = template_file

    def display_config(self):
        print(self.networks)
        print(self.process_id)
        print(self.router_id)
        print(self.timer_dead)
        print(self.timer_hello)
        print(self.passive_interfaces)

    def generate_script(self):
        try:
            with open(self.template_file, 'r') as file:
                template = file.read()

            passive_if_str = "\n".join([f"passive-interface {iface}" for iface in self.passive_interfaces])

            networks_str = "\n".join(
                [f"network {network['network']} {network['wildcard']} area {network['area_id']}" for network in
                 self.networks])

            ospf_script = template.replace("${process_id}", str(self.process_id)) \
                .replace("${router_id}", self.router_id) \
                .replace("${passive_interfaces}", passive_if_str) \
                .replace("network ${network} ${wildcard} area ${area_id}", networks_str) \
                .replace("${timer_hello}", str(self.timer_hello)) \
                .replace("${timer_dead}", str(self.timer_dead))

            return ospf_script

        except FileNotFoundError:
            return f"Template file '{self.template_file}' not found."


ospf_data = {
    "process_id": 10,
    "networks": [
        {
            "network": "10.0.0.0",
            "area_id": 10,
            "wildcard": "0.0.0.255"
        },
        {
            "network": "172.0.0.0",
            "area_id": 10,
            "wildcard": "0.0.0.3"
        },
        {
            "network": "69.0.0.0",
            "area_id": 10,
            "wildcard": "0.0.0.3"
        }
    ],
    "router_id": "10.0.0.1",
    "timer_dead": 30,
    "timer_hello": 10,
    "passive_interfaces": [
        "GigabitEthernet0/1",
        "GigabitEthernet0/2"
    ]
}
if __name__ == "__main__":
    ospf_gen = OSPFgenerator(ospf_data, "Configurations/ospf_template.txt")
    # ospf_gen.display_config()
    ospf_script = ospf_gen.generate_script()
    print(ospf_script)
