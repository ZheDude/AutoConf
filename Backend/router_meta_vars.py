from connections import SSHConnection
class router_meta_vars:
    def init(self, ip, username, password):
        """
        This function initializes the SSH connection to the router.
        """
        self.device = SSHConnection(ip, username, password)
    