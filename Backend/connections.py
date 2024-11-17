
import socket
import time
import paramiko

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

        return output