import socket
import sys
import pickle
from game import Juego


class Bot():
    def __init__(self):
        pass

    def connect(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            port = int(port)
            print(f"Using ip: {ip} and port: {port}")
            self.s.connect((ip, port))
            print("[+]: Connected")

        except Exception as e:
            print(f'[!]: Connection refused: {e}')
            sys.exit(0)

    def disconnect(self):
        self.s.close()

    def register(self, func):
        self.func = func

    def start(self):
        while (1):
            try:
                data = self.s.recv(Juego.__sizeof__(Juego))
                if data is None:
                    raise Exception("Invalid data")
                state: Juego = pickle.loads(data)
                self.s.send(pickle.dumps(self.func(state)))
            except Exception as e:
                print("[-] Error:", e)
                return
