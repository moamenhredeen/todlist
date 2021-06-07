

def format_response(
        status_code=200,
        headers={
            'Content-Type':'text/plain',
            'Author': 'Moamen Hraden'
        },
        body='empty body'
        ):
    statuses = {
        200:'200 OK',
        501 : '501 Not Implemented'
    }
    response_line = 'HTTP/1.1 {}'.format(statuses[status_code])
    headers = '\r\n'.join([ '{}: {}'.format(i, headers[i]) for i  in headers])
    response = "{}\r\n{}\r\n\r\n{}".format(response_line, headers, body)
    return response.encode()


def parse_request(request):
    request = request.decode()
    request_obj = {}
    lines = request.split('\r\n')

    # parse request line
    index = 0
    request_line = lines[0].split()
    index += 1
    request_obj['method'] = request_line[0]
    if(len(request_line) > 2 ):
        request_obj['url'] = request_line[1]
        request_obj['http-version'] = request_line[2]
    elif (len(request_line) > 1):
        request_obj['http_version'] = request_line[1]

    # parse headers
    headers = {}
    for line in lines[index:]:
        index += 1
        if(line == '' ):
            break
        else :
            splited = line.split(':')
            headers[splited[0]] = splited[1:]
    request_obj['headers'] = headers

    request_obj['body'] = ''.join(lines[index:])
    return request_obj