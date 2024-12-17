from connections import SSHConnection
class switch_meta_vars():
    
    def __init__(self, ip, username, password):
        self.device = SSHConnection(ip, username, password)
        self.device.send_command_imprvd("configure terminal\n    ")

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

        Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
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
                splitline = line.split()
                if splitline == []:
                    continue
                output.append({"Device ID": splitline[0], "Local Interface": splitline[1], "Holdtime": splitline[2], 
                            "Capability": splitline[3], "Platform": splitline[4], "Port ID": splitline[5]})
        return output