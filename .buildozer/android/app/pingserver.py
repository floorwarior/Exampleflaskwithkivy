# surprisingly pings the server
import http.client
import time
# Under Testing
import socket

def is_port_open(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)  # Set a timeout for the connection attempt
        result = s.connect_ex((host, port))  # Try connecting
        return result == 0  # If result is 0, the port is open


def waitforserver():
    noserver = True
    while noserver:
        print("not connected.")
        noserver = not is_port_open("localhost",5000)
        time.sleep(1)

    print("connected!")

#waitforserver()