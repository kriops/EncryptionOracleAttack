import random
import socketserver
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

HOST, PORT = "0.0.0.0", 12333

flag = open("flag.txt").read().strip()
key = os.urandom(16)


def encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    pt = pad(plaintext + flag.encode(), 16)
    return cipher.encrypt(pt).hex()


class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        self.request.sendall(b"Enter plaintext: ")
        user_input = self.request.recv(1024).strip()
        result = encrypt(key, user_input)
        self.request.sendall(f"Encrypted: {result}\n".encode())


if __name__ == "__main__":
    with socketserver.TCPServer((HOST, PORT), Handler) as server:
        server.serve_forever()
