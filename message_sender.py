import socket
import textwrap


class MessageSender:
    def __init__(self, host="localhost", port=12333, block_size=16):
        self.chunk_size = block_size
        self.host = host
        self.port = port
        self.buffer_size = 256

    def send(self, message):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            _ = s.recv(self.buffer_size)
            s.sendall(message.encode())
            response = b""
            while True:
                part = s.recv(self.buffer_size)
                response += part
                if len(part) < self.buffer_size:
                    break  # No more data to receive
            return textwrap.wrap(
                response.decode().strip().split()[-1], width=self.chunk_size * 2
            )
