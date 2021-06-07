############### import modules #####################
import socket
import logging


################ Http Server ###################
class tcp_server():
    def __init__(self, host='0.0.0.0', port=8080):
        # AF_INET : use IPV4
        # SOCK_STREAM : use TCP Protocol
        self.port = port
        self.host = host
        self.logger = logging.getLogger( name= __name__ )
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((host, port))

    def listen(self):
        self.socket.listen(1)
        self.logger.warning("Server listen on Port : {} ".format(self.socket.getsockname()))
        while(True):
            # wait for client connections
            client_connection, client_address = self.socket.accept()
            self.logger.warning("server listen on port : {}".format(self.port))
            # get the request
            request = client_connection.recv(1024)
            self.logger.warning("recieved request : {} ".format(request))

            # map the requests to request handlers
            response = self.handle_request(request)

            # send response
            client_connection.sendall(response)
            client_connection.close()


    def handle_request(self, request):
        return request

