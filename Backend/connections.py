
import socket
import time


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
            time.sleep(0.1)
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

    def send_command(self, command, prompt="(config)#", timeout=10):
        if not self.channel:
            raise Exception("SSH session not active")

        self.channel.send(command + '\n')
        output = ""
        self.channel.settimeout(timeout)

        # Continuously read until the prompt appears
        while True:
            if self.channel.recv_ready():
                output += self.channel.recv(2048).decode("utf-8")

                # Check if the prompt has appeared
                if prompt in output:
                    break
        print("Output ", output)
        return output

    def close(self):
        self.__del__()

    def __del__(self):
        self.client.close()

    def send_command_imprvd(self, command, timeout=10, prompt="(config)#"):
        if not self.channel:  # Ensure the channel is open
            raise Exception("SSH session not active")

        # Clear any existing output in the channel
        if self.channel.recv_ready():
            self.channel.recv(2048)

        # Send the command
        self.channel.send(command + '\n')

        output = ""
        start_time = time.time()

        while True:
            if self.channel.recv_ready():
                output += self.channel.recv(2048).decode("utf-8")

                # Check if the command prompt has returned in the output
                if output.strip().endswith(prompt):
                    break  # Break out if we see the prompt indicating the command is complete

            # Check for timeout to avoid infinite loop
            if time.time() - start_time > timeout:
                print("Timeout reached while waiting for command output.")
                break

            # Add a small delay to allow the buffer to fill up
            time.sleep(0.1)

        return output