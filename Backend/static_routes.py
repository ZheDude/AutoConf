import json

class StaticRoutesGenerator:
    def __init__(self, key_chain_data):
        ...

    def generate_script(self):
        ...


if __name__ == "__main__":
    data = {
        "Static-Routes": [
            {
                "source": "0.0.0.0",
                "mask": "0.0.0.0",
                "destination": "1.1.1.1",
                "interface": "GigabitEthernet0/0",
                "distance": 1
            },
            {
                "source": "1.1.1.0",
                "mask": "0.2.1.12",
                "destination": "1.1.1.1",
                "interface": "GigabitEthernet0/3",
                "distance": 12
            }
        ]
    }
    static_route_gen = StaticRoutesGenerator(data)
    script = static_route_gen.generate_script()
    print(script)
