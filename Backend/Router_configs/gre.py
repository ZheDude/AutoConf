class GRETunnelGenerator:
    def __init__(self, tunnel_data):
        self.data = tunnel_data

    def generate_script(self):
        commands = []

        for tunnel in self.data:
            tunnel_name = tunnel.get("tunnel")
            source_interface = tunnel.get("source")
            source_ip = tunnel.get("source_ip")
            destination = tunnel.get("destination")
            ip_address = tunnel.get("ip")
            subnet_mask = tunnel.get("subnetmask")

            if not all([tunnel_name, destination, ip_address, subnet_mask]):
                print(f"Skipping incomplete tunnel entry: {tunnel}")
                continue

            commands.append(f"interface {tunnel_name}")
            if source_interface:
                commands.append(f"tunnel source {source_interface}")
            elif source_ip:
                commands.append(f"tunnel source {source_ip}")
            else:
                print(f"Skipping tunnel entry due to missing source: {tunnel}")
                continue

            commands.append(f"tunnel destination {destination}")
            commands.append(f"ip address {ip_address} {subnet_mask}")
            commands.append("no shut")
            commands.append("exit")

        return "\n".join(commands)


if __name__ == "__main__":
    data = [
        {
            "tunnel": "Tunnel0",
            "source": "GigabitEthernet0/0",
            "source_ip": "",
            "destination": "1.1.1.1",
            "ip": "1.1.1.1",
            "subnetmask": "255.255.255.0"
        },
        {
            "tunnel": "Tunnel123",
            "source": "",
            "source_ip": "192.168.1.1",
            "destination": "212.12.1.1",
            "ip": "1.1.1.1",
            "subnetmask": "255.255.255.0"
        }
    ]

    gre_gen = GRETunnelGenerator(data)
    script = gre_gen.generate_script()
    print(script)
