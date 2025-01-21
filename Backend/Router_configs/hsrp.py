class HSRPGenerator:
    def __init__(self, hsrp_data):
        self.data = hsrp_data

    def generate_script(self):
        commands = []

        for entry in self.data:
            group = entry.get("group")
            version = entry.get("version", 2)
            interface = entry.get("interface")
            ip = entry.get("ip")
            priority = entry.get("priority", 100)
            preempt = entry.get("preempt", False)
            timers = entry.get("timers", {})

            if not all([group, interface, ip]):
                print(f"Skipping incomplete HSRP entry: {entry}")
                continue

            commands.append(f"interface {interface}")
            commands.append(f"standby version {version}")
            commands.append(f"standby {group} ip {ip}")
            commands.append(f"standby {group} priority {priority}")
            if preempt:
                commands.append(f"standby {group} preempt")
            if "hello" in timers and "hold" in timers:
                commands.append(
                    f"standby {group} timers {timers['hello']} {timers['hold']}"
                )
            commands.append("exit")  # Add a blank line for separation

        return "\n".join(commands)


if __name__ == "__main__":
    data = [
        {
            "group": 10,
            "version": 2,
            "interface": "GigabitEthernet0/0.1",
            "ip": "1.1.1.1",
            "priority": 10,
            "preempt": True,
            "timers": {"hello": 10, "hold": 30},
        },
        {
            "group": 10,
            "version": 2,
            "interface": "GigabitEthernet0/0.1",
            "ip": "1.1.1.1",
            "priority": 10,
            "preempt": True,
            "timers": {"hello": 10, "hold": 30},
        }
    ]
    hsrp_gen = HSRPGenerator(data)
    script = hsrp_gen.generate_script()
    print(script)
