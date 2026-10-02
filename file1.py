import paramiko

class networkdevices:
    def __init__(self, ip_address: str, username: str, password: str, port: int = 22):
        self.ip_address = ip_address
        self.username = username
        self.password = password
        self.port = port

    def connect(self):
        try:
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_client.connect(self.ip_address, username=self.username, password=self.password, port=self.port)
            print(f"Successfully connected to {self.ip_address}")
        except Exception as e:
            print(f"Failed to connect to {self.ip_address}: {e}")

router1 = networkdevices("192.168.1.10", "admin", "password123", 2222)
router1.connect()