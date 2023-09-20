import argparse
import sys
import socket
import struct
import threading

lock = threading.Lock()

def run_server(server_ip, server_port):
    """
    listens to a certain adress, reads the first four bytes, which tell it the lenght of the rest of
    the message, then reads the next amount of chracters indicated by the first four
    """
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind((server_ip, server_port))
    serv.listen()
    while True:
      conn, addr = serv.accept()
      #this is where we should create a new thread that didn't accept the request and is still available,
      #I just need to figure out how to do that
      while True:
        lock.acquire()
        initial_data = conn.recv(4)
        if not initial_data: break
        data_length = struct.unpack("<L", initial_data)[0]
        data = conn.recv(data_length)
        print (data.decode())
      conn.close()

def get_args():
    '''
    gets the ip and port from the command line
    '''
    parser = argparse.ArgumentParser(description='Receive data from client.')
    parser.add_argument('server_ip', type=str,
                        help='the server\'s ip')
    parser.add_argument('server_port', type=int,
                        help='the server\'s port')
    return parser.parse_args()


def main():
    args = get_args()
    try:
        run_server(args.server_ip, args.server_port)
    except Exception as error:
        print(f'ERROR: {error}')
        return 1


if __name__ == '__main__':
    while True:
        main()