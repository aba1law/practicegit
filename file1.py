def networkdevices(
    ip_address: str,
    username: str,
    password: str,
    port: int = 22
):    
    print(ip_address)
    print(username)
    print(password)
    print(port)

networkdevices(
    "192.168.1.10",
    "admin",
    "password123",
    2222
)