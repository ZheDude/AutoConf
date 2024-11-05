import asyncio


def main():
    from connections import SSHConnection
    # from connections import TelnetConnection
    dev1 = SSHConnection("172.16.2.1", "cisco", "cisco")
    result = dev1.send_command("do show version\n    ")
    print(result)


if __name__ == '__main__':
    main()