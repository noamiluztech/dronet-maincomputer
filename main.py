# DroNet-2023
# Main Computer

import socket
import threading

from log import configure_logger


if __name__ == "__main__":
    # set local machine IP
    host = '0.0.0.0' # need to edit

    # Configure the logger with the file handler
    logger, log_file = configure_logger()
    logger.info("***** Starting Process *****")   

    logger.info("check 1")
    logger.info (f"Host IP is - {host}")


    # start the server
    start_server()





    def handle_client(clientsocket, addr):
        print("Got a connection from %s" % str(addr))

        # receive data from the client
        data = clientsocket.recv(1024)
        number = int(data.decode('utf-8'))

        # perform any necessary processing on the data
        result = number * 2

        # send the result back to the client
        clientsocket.send(str(result).encode('utf-8'))

        # close the connection
        clientsocket.close()

    def start_server():
        # create a socket object
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # bind the socket to a public host, and a port
        serversocket.bind((host, 9999))

        # become a server socket
        serversocket.listen(5)

        print("Server started. Waiting for client connections...")

        while True:
            # accept a new connection
            clientsocket, addr = serversocket.accept()

            # create a new thread to handle the connection
            client_thread = threading.Thread(target=handle_client, args=(clientsocket, addr))
            client_thread.start()

            #TODO:two systems + compiling the data + presenting.


