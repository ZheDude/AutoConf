import telnetlib3 as tlnt

class Connection:
    tn = None
    
    def __init__(self, host, port = 23):
        self.host = host
        self.port = port
        self.tn = tlnt.open_connection(host=host, port=port)
        
    def send(self, data): 
        self.tn.send(data)
    