from connections import SSHConnection
class switch_meta_vars():
    
    def __init__(self, ip, username, password):
        self.device = SSHConnection(ip, username, password)
        result = self.device.send_command_imprvd("configure terminal\n    ")
        print(result)

    def close(self):
        print("MADAM I WANT THIS CLOSED")
        self.device.close()

    def extract_interfaces(self):
        input: str = self.device.send_command_imprvd("do-exec show ip interface brief\n    ")
        output = []
        lines = input.split("\n")
        for line in lines:
            if "Interface" in line:
                continue
            elif ")#" in line or "do-exec" in line: 
                continue
            else:
                splitline = line.split()
                output.append({"Interfaces": splitline[0], "IP-Address": splitline[1], "OK?": splitline[2], 
                            "Method": splitline[3], "Status": splitline[4], "Protocol": splitline[5]})
        return output

    def extract_neighbors(self):
        """
        example input:
        S1#
        sh cdp neighbors 
        Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                    S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone, 
                    D - Remote, C - CVTA, M - Two-port Mac Relay 

        Device ID        Local Interface     Holdtime    Capability  Platform  Port ID
        R1.5CN           Gig 0/0           135              R B             Gig 0/0

        Total cdp entries displayed : 1
        S1#
        """
        input: str = self.device.send_command_imprvd("do-exec show cdp neighbors\n    ")
        output = []
        start_flag = False
        lines = input.split("\n")
        for line in lines:
            if "Device ID" in line:
                start_flag = True
                continue
            elif ")#" in line or "do-exec" in line: 
                continue
            elif "Total cdp entries displayed" in line:
                start_flag = False
            elif start_flag:
                if line.split() == "":
                    continue
                field = line.split()
                print(field)
                if len(field) < 8:  # Handle cases where fields are missing
                    continue
                entry = {
                    "Device ID": field[0],
                    "Local Interface": field[1] + " " + field[2],
                    "Holdtime": field[3],
                    "Capability": " ".join(field[4:6]),  # Join Capability fields (if present)
                    "Platform": field[6] if len(field) > 8 else "",  # Check if Platform is present
                    "Port ID": " ".join(field[7:]) if len(field) > 8 else " ".join(field[6:])  # Join remaining fields for Port ID
                }
                output.append(entry)
                start_flag = False
        return output