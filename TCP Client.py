from socket import *
import sys

host = 'localhost'
port = 2348
addr = (host, port)

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.connect(addr)

data = input('write to server: ')
if not data:
    tcp_socket.close()
    sys.exit(1)

data = str.encode(data)
tcp_socket.send(data)
data = bytes.decode(data)
data = tcp_socket.recv(1024)
print(data)

inputDir = input()

tcp_socket.close()
