
from http_server import http_server
from helper_functions import format_response
import json
import sys

users = [
    {
        'id':1,
        'name':'maomen'
    },
    {
        'id':2,
        'name':'imam'
    }
]

class user_service(http_server):

    def __init__(self, host, port):
        super().__init__(host=host, port=port)

    def do_get(self, req):
        if(req['url'] == '/users'):
            return format_response(headers={'Content-Type':'application/json'}, body=json.dumps(users))
        else:
            return self.not_found()



def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    user_service('0.0.0.0', port).listen()

if __name__ == '__main__':
    main()