import json


class RIPGenerator:
    def __init__(self, rip_data, template_file):
        self.rip_data = rip_data

        self.version = rip_data["RIP"]["version"]
        self.auto_summary = rip_data["RIP"]["auto-summary"]
        self.networks = rip_data["RIP"]["networks"]
        self.neighbor = rip_data["RIP"]["neighbor"]
        self.timer_update = str(rip_data["RIP"]["timer_update"])  + " 180 180 240"
        self.passive_interface = rip_data["RIP"]["passive_interface"]
        # self.redistribute = rip_data["RIP"]["redistribute"]

        self.template_file = template_file

    def display_config(self):
        print(json.dumps(self.rip_data, indent=4))

    def generate_script(self):
        try:
            with open(self.template_file, 'r') as file:
                template = file.read()

            passive_if_str = "\n".join([f"passive-interface {iface}" for iface in self.passive_interface])

            # redistribute_str = "\n".join([f"redistribute {protocol}" for protocol in self.redistribute])

            networks_str = "\n".join([f"network {network['network']}" for network in self.networks])

            rip_script = template.replace("${version}", str(self.version)) \
                .replace("${auto_summary}", "no auto-summary" if not self.auto_summary else "auto-summary") \
                .replace("network ${network}", networks_str) \
                .replace("${neighbor}", self.neighbor) \
                .replace("${timer_update}", str(self.timer_update)) \
                .replace("${passive_interface}", passive_if_str) \
                #.replace("${redistribute}", redistribute_str)

            rip_script += "\nexit\n"
            
            return rip_script

        except FileNotFoundError:
            return f"Template file '{self.template_file}' not found."


rip_data = {
    "RIP": {
        "version": 2,
        "auto-summary": True,
        "networks": [
            {
                "network": "10.0.0.0"
            },
            {
                "network": "172.0.0.0"
            }
        ],
        "neighbor": "10.0.0.3",
        "timer_update": 30,
        "passive_interface": [
            "GigabitEthernet0/1",
            "GigabitEthernet0/2"
        ],

    }
}

if __name__ == "__main__":
    # Instantiate the RIPGenerator class with the rip_data
    rip_gen = RIPGenerator(rip_data, "../Configurations/rip_template.txt")

    # Call the method to display the configuration in JSON structure
    rip_gen.display_config()

    # Generate and display the RIP configuration script based on the template
    rip_script = rip_gen.generate_script()
    print(rip_script)
