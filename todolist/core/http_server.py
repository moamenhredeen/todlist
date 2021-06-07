
from tcp_server import tcp_server
from helper_functions import *
import logging

class http_server(tcp_server):
    def start(self):
        self.listen()

    def handle_request(self, request):
        req = parse_request(request)
        if req['method'] == 'GET' :
            return self.do_get(req)
        # handle oher http methods
        else :
            return format_response(status_code= 501)

    def do_get(self, req):
        return format_response(status_code=200, body="default implemenatation")

    def not_found(self):
        return format_response(status_code=501, body="page not found")



def main():
    server = http_server()
    logging.basicConfig(filename="./file.log", level=logging.INFO)
    server.start()


if __name__ == '__main__':
    main()