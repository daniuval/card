import argparse
import sys
import socket
import struct


def run_server(server_ip, server_port):
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind((server_ip, server_port))
    serv.listen()
    while True:
      conn, addr = serv.accept()
      from_client = ''
      while True:
        initial_data = conn.recv(4)
        if not initial_data: break
        data_length = struct.unpack("<L", initial_data)[0]
        data = conn.recv(data_length)
        from_client += data.decode()
        print (from_client)
      conn.close()

def get_args():
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