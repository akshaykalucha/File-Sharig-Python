import socket
import os

import protocol_consts
import protocol_exceptions

class ReceivingServer:
    def __init__(self, dstdir: str) -> None:
        self._DST = dstdir

        self._HOST = socket.gethostbyname(socket.gethostname())
        print("In order for the sender machine to locate this machine in the local network, the following local IP will be needed:", self._HOST)

        self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server_socket.bind((self._HOST, protocol_consts.PORT))
        self._transfer_socket = None
    
    def listen_and_connect_to_client(self) -> None:
        self._server_socket.listen()
        self._transfer_socket, client_addr = self._server_socket.accept()

        print("Sender has connected with address:", client_addr)