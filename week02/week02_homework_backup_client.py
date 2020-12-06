# Author:Bred

import socket
import sys
import os
from pathlib import Path

HOST = "localhost"
PORT = 10000


def backup_file_client(inputFilePath: str):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    receivedBinary = b''

    try:
        with open(inputFilePath, "rb") as f:
            data = f.read(1024)
            while data:
                print(data)
                s.sendall(data)
                receivedBinary += s.recv(1024)
                data = f.read(1024)

    except Exception as e:
        print("The file cannot be open or file is not exist: {}".format(e))
        sys.exit(1)

    try:
        p = Path(inputFilePath)
        suffix = p.suffix
        inputName = p.stem
        parentPath = os.path.split(os.path.realpath(__file__))[0]

        if suffix:
            outputFilePath = "".join(
                (parentPath + "\\" + inputName + "_bak", suffix))
        else:
            outputFilePath = parentPath + "\\" + inputName + "_bak"

        with open(outputFilePath, "wb") as f:
            f.write(receivedBinary)
    except Exception as e:
        print("Cannot backup the file: {}".format(e))
        sys.exit(2)

    s.close()


if __name__ == "__main__":
    target_filename = input('target_filename: ')
    backup_file_client(target_filename)
