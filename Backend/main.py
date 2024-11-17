def main():
    from connections import SSHConnection
    # from connections import TelnetConnection
    dev1 = SSHConnection("172.16.2.127", "cisco", "cisco")
    result = dev1.send_command_imprvd("configure terminal\n    ")
    print(result)
    result = dev1.send_command_imprvd("do-exec show version\n    ")
    print(result)
    result = dev1.send_command_imprvd("do-exec show ip interface brief\n    ")
    print(result)


if __name__ == '__main__':
    main()
