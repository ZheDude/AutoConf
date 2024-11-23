class StaticRoutesGenerator:
    def __init__(self, static_route_data):
        self.static_route_data = static_route_data

    def generate_script(self):
        script = []
        for route in self.static_route_data:
            source = route.get("source", "0.0.0.0")
            mask = route.get("mask", "0.0.0.0")
            destination = route.get("destination", "")
            interface = route.get("interface", "")
            distance = route.get("distance", 1)

            if destination:
                cmd = f"ip route {source} {mask} {destination} {distance}"
            elif interface:
                cmd = f"ip route {source} {mask} {interface} {distance}"
            else:
                continue

            script.append(cmd)

        return "\n".join(script)


if __name__ == "__main__":
    data = {
        "Static-Routes": [
            {
                "source": "0.0.0.0",
                "mask": "255.255.255.123",
                "destination": "1.1.1.1",
                "interface": "",
                "distance": 1
            },
            {
                "source": "1.1.1.0",
                "mask": "0.2.1.12",
                "destination": "",
                "interface": "GigabitEthernet0/3",
                "distance": 12
            }
        ]
    }
    static_route_gen = StaticRoutesGenerator(data)
    script = static_route_gen.generate_script()
    print(script)
