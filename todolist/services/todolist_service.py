
from http_server import http_server
from helper_functions import format_response
import json
import sys

todo_items = [
    {
        'id':1,
        'summary':'network presentation',
        'status':'DONE'
    },
    {
        'id':2,
        'summary':'network loadbalancer',
        'status':'TODO'
    }
]

class todolist_service(http_server):

    def __init__(self, host, port):
        super().__init__(host=host, port=port)

    def do_get(self, req):
        if(req['url'] == '/todolist'):
            return format_response(
                status_code=200,
                headers={'Content-Type':'application/json'},
                body=json.dumps(todo_items))
        else:
            return self.not_found()

def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    todolist_service('0.0.0.0', port ).listen()

if __name__ == '__main__':
    main()
