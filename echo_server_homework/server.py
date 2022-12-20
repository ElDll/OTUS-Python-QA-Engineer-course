import re
import socket
from http import HTTPStatus

END_OF_STREAM = '\r\n\r\n'

METHODS = ('GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE')

regex = r"(\bstatus=\b)([0-9]*)"


def data_parce(data: list):
    result = ""

    for i in range(len(data)):
        if data[i] in METHODS:
            result += f"Request Method: {data[i]}\r\n"
        if data[i] == "Host:":
            result += f"Request Source: (\'{data[i + 1]}\', "
        if data[i] == "Port:":
            result += f"{data[i + 1]})\r\n"
        if data[i] == "Path:":
            matches = re.search(regex, data[i + 1])
            if matches is not None:
                status_code = matches.group(2)
                if status_code in str(list(HTTPStatus)) and status_code != '':
                    for element in list(HTTPStatus):
                        if element.value == int(status_code):
                            phrase = element.phrase
                            result += f"Response Status: {status_code} {phrase}\r\n"
                else:
                    result += f"Response Status: 200 OK\r\n"
            else:
                result += f"Response Status: 200 OK\r\n"

    for i in range(len(data)):
        if data[i][-1] == ":":
            result += f"{data[i]} {data[i + 1]}\r\n"

    return result + "\r\n"


def handle_client(connection):
    client_data = ''
    with connection:
        while True:
            data = connection.recv(1024)
            print("Received:", data.decode("utf-8").strip().split())
            if not data:
                break
            client_data += data.decode()
            if END_OF_STREAM in client_data:
                break

        connection.send(data_parce(data.decode("utf-8").strip().split()).encode()
                        + f"\r\n".encode())


with socket.socket() as serverSocket:
    serverSocket.bind(("127.0.0.1", 40404))
    serverSocket.listen()

    while True:
        (clientConnection, clientAddress) = serverSocket.accept()
        handle_client(clientConnection)
        print(f"Sent data to {clientAddress}")
