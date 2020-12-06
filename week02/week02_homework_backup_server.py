# Author:Bred

import socket

HOST = "localhost"
PORT = 10000


def backup_filename_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)

    while True:
        conn, addr = s.accept()
        print('connected by {}'.format(addr))

        while True:
            data = conn.recv(1024)
            print(data)

            if not data:
                print("client is disconnected")
                break
            conn.sendall(data)
        conn.close()
    s.close()

if __name__ == "__main__":
    backup_filename_server()
