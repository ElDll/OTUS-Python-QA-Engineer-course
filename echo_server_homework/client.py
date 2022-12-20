import socket
import sys

HOST = "127.0.0.1"
PORT = None

try:
    PORT = int(sys.argv[1])
except IndexError:
    print("Pass a port for connection")
    exit(1)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"Connecting to {HOST}:{PORT}")
    s.connect((HOST, PORT))

    message = (
        "GET / HTTP/1.1\r\n"
        "Host: localhost\r\n"
        "Port: 4324\r\n"
        "User-Agent: curl/7.83.1\r\n"
        "Path: https://disqus.com/recommendations/?status=404&f=metanitcom&t_u=https%3A%2F%2Fmetanit.com\r\n"
        "Number: 123\r\n"
        "\r\nAccept: */*\r\n\r\n"
    )
    s.send(bytes(message, "utf-8"))
    data = s.recv(1024)

    print('Received back:\n' + data.decode("utf-8"))
