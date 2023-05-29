# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import socket
import time

# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    # create a socket object
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get local machine name
    host = '192.168.161.8'

    # bind the socket to a public host, and a port
    serversocket.bind((host, 9000))

    # become a server socket
    serversocket.listen(1)

    print("Server started. Waiting for client connection...")

    while True:
        # establish a connection
        clientsocket, addr = serversocket.accept()

        print("Got a connection from %s" % str(addr))

        # receive data from the client
        data = clientsocket.recv(1024)
        number = int(data.decode('utf-8'))
        print("Center point" + number)

        # perform any necessary processing on the data
        result = "recieved"

        # send the result back to the client
        clientsocket.send(str(result).encode('utf-8'))

        # close the connection
        clientsocket.close()
        time.sleep(1)



