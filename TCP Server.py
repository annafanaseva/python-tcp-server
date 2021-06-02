from socket import *
import os

# данные сервера
host = 'localhost'
port = 2348
addr = (host, port)

tcp_socket = socket(AF_INET, SOCK_STREAM)

tcp_socket.bind(addr)

tcp_socket.listen(1)

while True:

    question = input('Do you want to quit? y\\n: ')
    if question == 'y': break

    print('wait connection...')

    conn, addr = tcp_socket.accept()
    print('client addr: ', addr)

    data = conn.recv(1024)

    if not data:
        conn.close()
        break
    else:
        print(data)
        data = data.decode()
        os.system(data)

        conn.send(b'Hello from server!')

        conn.close()

# import os
#

#
# dir_name = inputDir
# print(dir_name)
#
# def deleteFile(dir_name):
#     print("Content:", os.listdir(dir_name))
#     for i in os.listdir(dir_name):
#         if os.path.isdir(dir_name + "/" + i):
#             deleteFile(dir_name + "/" + i)
#         else:
#             format_1 = i.split('.')[-1]
#             if ((format_1 == 'tmp') and (os.path.getsize(dir_name + "/" + i) > inputSize)):
#                 os.remove(dir_name + "/" + i)
# deleteFile(dir_name)

tcp_socket.close()