import json
from socket import socket

from constants import HOST, PORT, ENCODING, BUFFER_SIZE

s = socket()
s.bind((HOST, PORT))
s.listen(5)

while True:
    client, address = s.accept()
    print('CLIENT: %s' % str(address))
    request = client.recv(BUFFER_SIZE)
    req_json = json.loads(request.decode(ENCODING))
    print('REQUEST: %s' % req_json)
    if 'action' in req_json and req_json['action'] == 'presence':
        client.send(json.dumps({'response': 200, 'alert': 'OK'}).encode(ENCODING))
    client.close()
