import argparse
import sys
import socket
import struct


def send_data(server_ip, server_port, data):
    '''
    encode length of data and send to server, then send data.
    '''
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))
    client.send(struct.pack('<L', len(data)))
    client.send(bytes(data, 'utf-8'))
    client.close()


def get_args():
    parser = argparse.ArgumentParser(description='Send data to server.')
    parser.add_argument('server_ip', type=str,
                        help='the server\'s ip')
    parser.add_argument('server_port', type=int,
                        help='the server\'s port')
    parser.add_argument('data', type=str,
                        help='the data')
    return parser.parse_args()


def main():
    '''
    Implementation of CLI and sending data to server.
    '''
    args = get_args()
    try:
        send_data(args.server_ip, args.server_port, args.data)
        print('Done.')
    except Exception as error:
        print(f'ERROR: {error}')
        return 1


if __name__ == '__main__':
    sys.exit(main())