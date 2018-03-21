import json
import select
import time
from socket import socket

from constants import HOST, PORT, ENCODING, BUFFER_SIZE, CLIENTS_NUMBER
from logger.logger import log

clients = []


@log
def main_loop(my_socket):
    print('Server started at %s' % time.ctime(time.time()))
    while True:
        add_client(my_socket)
        write = get_list_to_write()

        for client in write:
            request = read_request(client)
            if 'action' in request and request['action'] == 'presence':
                write_response(client, 'Ok')


@log
def write_response(client, message):
    client.send(json.dumps({'response': 200, 'alert': message}).encode(ENCODING))


@log
def read_request(client):
    try:
        req = client.recv(BUFFER_SIZE)
        req_json = json.loads(req)
        print('REQUEST: %s' % req_json)
        return req_json
    except Exception as e:
        print(e)
        clients.remove(client)
        print('REMOVED CLIENT: %s' % client)
        return {}


@log
def get_list_to_write():
    w = []
    if len(clients) > 0:
        try:
            _, w, _ = select.select([], clients, [], 0)
        except Exception as e:
            print(e)
    return w


@log
def add_client(my_socket):
    try:
        client, _ = my_socket.accept()
    except OSError:
        pass
    else:
        clients.append(client)
        print('ADDED CLIENT: %s' % str(client))


@log
def init_socket():
    s = socket()
    s.bind((HOST, PORT))
    s.listen(CLIENTS_NUMBER)
    s.settimeout(0.2)
    return s


if __name__ == '__main__':
    main_loop(init_socket())
