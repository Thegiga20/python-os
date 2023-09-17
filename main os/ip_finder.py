import socket
def ipfinder():
    hostname = socket.gethostname()
    ipfinder = socket.gethostbyname(hostname)
    print('your ip is ', ipfinder)