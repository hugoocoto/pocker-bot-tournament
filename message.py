import queue


class Message:
    def __init__(self, client, action):
        self.client = client
        self.action = action

    def get_client(self): return self.client
    def get_action(self): return self.action

    def get(): return messages.get(block=True)
    def put(msg): messages.put(msg)


messages: queue.Queue[Message] = queue.Queue()
