# DroNet-2023

import socket

# create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# specify the server IP address and port
server_address = ('192.168.23.145', 9000) # need to edit

# connect to the server
clientsocket.connect(server_address)

# send a number to the server
number = 656
clientsocket.send(str(number).encode('utf-8'))

# receive the result from the server
result = clientsocket.recv(1024)
result = int(result.decode('utf-8'))

print("The result is %d" % result)

# close the client socket
clientsocket.close()