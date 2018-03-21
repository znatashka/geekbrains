import json
import time
from socket import socket

from constants import BUFFER_SIZE, HOST, PORT, ENCODING
from logger.logger import log


@log
def main_loop(my_socket):
    while True:
        try:
            action = int(input('Put a number: '))
            if action == 1:
                send_request(my_socket)
                read_response(my_socket)
            if action == 2:
                my_socket.close()
                exit(0)
        except ValueError as e:
            print(e)
            print('Try again')


@log
def read_response(my_socket):
    response = my_socket.recv(BUFFER_SIZE)
    if len(response) is not 0:
        print('RESPONSE: %s' % json.loads(response))


@log
def send_request(my_socket):
    my_socket.send(json.dumps({'action': 'presence', 'time': time.ctime(time.time())}).encode(ENCODING))


@log
def init_socket():
    s = socket()
    s.connect((HOST, PORT))
    return s


if __name__ == '__main__':
    print("""
    1 - send a message
    2 - exit
    """)
    main_loop(init_socket())
