import json


class OSPFConfigGenerator:
    def __init__(self, template_file, config_file):
        self.template_file = template_file
        self.config_file = config_file
        self.config = {}
        self.template = ""

    def load_template(self):
        """Load the OSPF configuration template from the file."""
        with open(self.template_file, 'r') as file:
            self.template = file.read()

    def load_config(self):
        """Load the configuration from the JSON file."""
        with open(self.config_file, 'r') as file:
            data = json.load(file)
            self.config = data['OSPF']  # Access the OSPF part of the JSON

    def substitute_placeholders(self):
        """Substitute placeholders in the template with actual values from the config."""
        for key, value in self.config.items():
            # Check if the value is a dictionary (for nested attributes)
            print(key, value)
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    placeholder = f"${{{sub_key}}}"
                    self.template = self.template.replace(placeholder, str(sub_value))
            elif isinstance(value, list):
                if key == "passive_interfaces":
                    # Format passive interfaces
                    passive_str = "\n  ".join(f"passive-interface {interface}" for interface in value)
                    placeholder = f"${{{key}}}"
                    self.template = self.template.replace(placeholder, passive_str)
            else:
                placeholder = f"${{{key}}}"
                self.template = self.template.replace(placeholder, str(value))

    def generate_config(self):
        """Generate the final OSPF configuration."""
        self.load_template()
        self.load_config()

        # Prepare the necessary parameters for substitution
        print(self.config['network'])
        print(self.config['network']['wildcard'])
        print(self.config['network']['area_id'])
        print(self.config)
        print(self.config.items())
        network_config = self.config['network']

        # Flatten the network configuration
        self.config['network'] = network_config['network']  # This is the actual network address
        self.config['wildcard'] = network_config['wildcard']  # This is the wildcard mask
        self.config['area_id'] = network_config['area_id']  # This is the area ID

        # Substitute placeholders with actual values
        self.substitute_placeholders()
        return self.template

    def save_config(self, output_file):
        """Save the generated configuration to a file."""
        with open(output_file, "w") as file:
            file.write(self.template)


# Example usage:
if __name__ == "__main__":
    # File names for the template and configuration
    template_file = "Configurations/ospf_template.txt"
    config_file = "Configurations/ospf_config.json"
    output_file = "generated_ospf_config.txt"

    # Create an instance of the OSPFConfigGenerator class
    ospf_generator = OSPFConfigGenerator(template_file, config_file)

    # Generate the OSPF configuration
    generated_config = ospf_generator.generate_config()
    print(generated_config)

    # Save the generated configuration to a file
    ospf_generator.save_config(output_file)
