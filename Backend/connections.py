
import socket
import time
from quopri import decodestring

import paramiko
# import asyncio_telnet as Telnet

class SSHConnection:
    def __init__(self, ip, username, password):
        self.ip = ip
        self.username = username
        self.password = password
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.client.connect(self.ip, username=self.username, password=self.password)
            self.channel = self.client.invoke_shell()
            time.sleep(5)
        except paramiko.ssh_exception.AuthenticationException:
            raise Exception("Authentication failed")
        except socket.gaierror:
            raise Exception("Invalid IP address")
        except paramiko.ssh_exception.NoValidConnectionsError:
            raise Exception("Connection failed NoValidConnectionsError")
        except paramiko.ssh_exception.BadHostKeyException:
            raise Exception("Connection failed BadHostKeyException")
        except paramiko.ssh_exception.SSHException:
            raise Exception("Connection failed SSHException")

    def send_command(self, command):
        if not self.channel:  # Ensure the channel is open
            raise Exception("SSH session not active")

        # Send command and read output
        self.channel.send(command + '\n')
        output = ""

        while not self.channel.recv_ready():
            pass  # Wait until data is ready to be read
        
        time.sleep(5)
        
        while self.channel.recv_ready():
            output += self.channel.recv(2048).decode("utf-8")

        return output
        # stdin, stdout, stderr = self.client.exec_command(command)
        # return stdout.read().decode("utf-8")

    def close(self):
        self.__del__()
    
    def __del__(self):
        self.client.close()
        
    
# class TelnetConnection:
#     def __init__(self, ip, port):
#         self.ip = ip
#         self.port = port
#         self.tn = Telnet.Telnet()
#     
#     async def send_command(self, command):
#         await self.tn.open(self.ip, self.port)
#         await self.tn.write(decodestring(command))
#         response = await self.tn.read_until_eof()
#         await self.tn.close()
#         return response
            