import json
import time
from socket import socket

from constants import BUFFER_SIZE, HOST, PORT, ENCODING

s = socket()
s.connect((HOST, PORT))
s.send(json.dumps({'action': 'presence', 'time': time.time()}).encode(ENCODING))
response = s.recv(BUFFER_SIZE)
s.close()
if len(response) is not 0:
    print('RESPONSE: %s' % json.loads(response.decode(ENCODING)))
