import json

class Etherchannelgenerator:
    def __init__(self, etherchannel_data, template_file):
        self.number = etherchannel_data['number']
        self.mode = etherchannel_data['mode']
        self.interfaces = []
        for x in etherchannel_data['interfaces']:
            


def display_config(self):
        ...

    def generate_script(self):
        try:
            with open(self.template_file, 'r') as file:
                template = file.read()

            passive_if_str = "\n".join([f"passive-interface {iface}" for iface in self.passive_interfaces])

            networks_str = "\n".join([f"network {network['network']} {network['wildcard']} area {network['area_id']}" for network in self.networks])

            ospf_script = template.replace("${process_id}", str(self.process_id)) \
                .replace("${router_id}", self.router_id) \
                .replace("${passive_interfaces}", passive_if_str) \
                .replace("network ${network} ${wildcard} area ${area_id}", networks_str) \
                .replace("${timer_hello}", str(self.timer_hello)) \
                .replace("${timer_dead}", str(self.timer_dead))

            return ospf_script

        except FileNotFoundError:
            return f"Template file '{self.template_file}' not found."


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
if __name__ == "__main__":
    ospf_gen = Etherchannelgenerator(etherchannel_data, "Configurations/etherchannel_template.txt")
    #ospf_gen.display_config()
    ospf_script = ospf_gen.generate_script()
    print(ospf_script)
