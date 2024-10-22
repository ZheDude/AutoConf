import json


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
        try:
            with open(self.template_file, 'r') as file:
                template = file.read()

            interface_range_string = " ".join(self.group['interfaces'])

            fin_str = template.replace("${interface}", interface_range_string) \
                .replace("${number}", str(self.group['number'])) \
                .replace("${mode}", self.group['mode'])
            return fin_str
    
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
    etherchannel_gen = Etherchannelgenerator(etherchannel_data, "Configurations/etherchannel_template.txt")
    # etherchannel_gen.display_config()
    etherchannel_script = etherchannel_gen.generate_script()
    print(etherchannel_script)
