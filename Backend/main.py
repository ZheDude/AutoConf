import asyncio

def main():
    from connections import SSHConnection
    from connections import TelnetConnection
    dev1 = TelnetConnection("172.16.244.128", 5000)
    result = asyncio.run(dev1.send_command("do show version\n    "))
    print(result)
    
if __name__ == '__main__':
    main()
    


