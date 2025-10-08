from threading import Thread
import socket
from game import Action, Game, Jugador
import pickle
from message import Message


clients = []


def listen_for_connections(s):
    while True:
        conn, addr = s.accept()
        c = Client(conn, addr)

        print(f"New client. Client count: {len(clients)}")

        c.start()

        if len(clients) == 2:
            start_game()


def consume_messages():
    while True:
        m = Message.get(block=True)
        print(f"{m.action} from {m.client}")


def start_game():
    game = Game([Jugador(c) for c in clients])
    game.play()
    # for c in clients:
    #     c: Client
    #     to_send = Juego()
    #     c.conn.send(pickle.dumps(to_send))


class Client:
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr

    def listen_for_messages(self):
        while True:
            try:
                data = self.conn.recv(Action.__sizeof__(Action))
                if not data:
                    raise Exception("Couldn't read")

            except Exception:
                return

            else:
                Message.put(Message(self, pickle.loads(data)), block=True)

    def start(self):
        clients.append(self)
        t = Thread(target=self.listen_for_messages)
        t.start()

    def __str__(self):
        return f"{self.addr[0]}:{self.addr[1]}"

    def __repr__(self):
        return self.__str__()


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        SERVER_HOST = socket.gethostbyname(socket.gethostname())
        SERVER_PORT = 5001

        try:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((SERVER_HOST, SERVER_PORT))
            print(f'[+]: Binded to: {SERVER_PORT}')

        except socket.error as e:
            print(f'[!]: Error while connecting to {SERVER_PORT}: {e}')

        s.listen()
        print(f"[>]: Listening as {SERVER_HOST}:{SERVER_PORT}")

        t = Thread(target=listen_for_connections, args=[s])
        t.start()
        consume_messages()

        t.join()
