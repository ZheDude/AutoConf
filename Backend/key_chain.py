import json


class KEYCHAINgenerator:
    def __init__(self, key_chain_data):
        self.data = key_chain_data



    def generate_script(self):
        commands = []

        for key in self.data:
            name = key.get("name")
            number = key.get("number")
            password = key.get("password")
            algo = key.get("ALGO", "hmac-sha-256")

            if not all([name, number, password, algo]):
                print(f"Skipping incomplete key chain entry: {key}")
                continue

            commands.append(f"key chain {name}")
            commands.append(f"key {number}")
            commands.append(f"key-string {password}")
            commands.append(f"cryptographic-algorithm {algo}")
            commands.append("")

        return "\n".join(commands)


if __name__ == "__main__":
    data = {
        "Key-Chain": [
            {
                "number": 12,
                "name": "key-name-chain",
                "password": "PASSWORD",
                "ALGO": "hmac-sha-512"
            },
            {
                "number": 112341232,
                "name": "NA1234123ME",
                "password": "PASSWO123412RD",
                "ALGO": "hmac-sha-256"
            }
        ]
    }
    keychain_gen = KEYCHAINgenerator(data.get("Key-Chain"))
    script = keychain_gen.generate_script()
    print(script)
