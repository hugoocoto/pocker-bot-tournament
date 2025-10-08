from evaluador import puntuar_mano_7


class Action:
    text: str
    opciones = ["Pasar", "Apostar", "Igualar", "Subir", "Retirarse"]

    def __init__(self, text):
        self.text = text
        pass

    def __str__(self):
        return self.text


class Card:
    number: int
    name: str
    short: str

    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.short = self._get_short()
        pass

    def _get_short(self):
        name = ['A', *[str(a) for a in range(1, 10+1)], 'J', 'Q', 'K']
        suit = ['C', 'D', 'T', 'P']
        return name[self.number // 13] + suit[self.number % 13]

    def __str__(self):
        return self.name + ": " + self.short

    def get_num(self): return self.num


jugador_id: int = 0


class Jugador:
    cartas_llevadas: list[Card]
    puntos: int
    mano: list[Card]

    def __init__(self, client):
        self.client = client
        self.id = jugador_id

    def set_mano(self, m):
        self.mano = m

    def get_apuesta(self, mesa): pass

    def __str__(self):
        return f"Jugador {self.id}"


class Baraja:
    cards: list[Card] = []

    def __init__(self, type: str):
        match (type):
            case "poker52":
                self.create_poker52()
            case _:
                raise Exception("Invalid Baraja type: "+type)

    def create_poker52(self):
        n = 1
        for suit in ["Corazones", "Diamantes", "Tréboles", "Picas"]:
            for num in ["As", *[str(n) for n in range(2, 10+1)], "Sota", "Reina", "Rey"]:
                self.cards.append(Card(f"{num} de {suit}", n))
                n += 1

    def print_cards(self, cards: list[Card] = None):
        if cards is None:
            cards = self.cards
        for c in cards:
            print(c)

    def suffle(self):
        self.cards.suffle()

    # pick N cards
    def pick(self, n: int):
        if len(self.cards) < n:
            raise Exception("No that many cards in baraja")
        return [self.cards.pop() for _ in range(n)]


class Juego:
    jugadores: list[Jugador]
    mesa: list[Card]
    baraja: Baraja

    def __init__(self, baraja="poker52"):
        self.mesa = []
        self.baraja = Baraja(baraja)

    def set_jugadores(self, j):
        self.jugadores = j

    def get_jugadores(self): return self.jugadores
    def get_mesa(self): return self.mesa
    def mesa_add(self, *cards): self.mesa.extend(cards)
    def pick(self, n): return self.baraja.pick(n)


class Game:

    def __init__(self, jugadores: list[Jugador]):
        self.partida: Juego = Juego()
        self.partida.set_jugadores(jugadores)

    def play(self):
        def start(self):
            for j in self.partida.get_jugadores():
                j.set_mano(self.partida.pick(5))

        def preflop(self):
            for j in self.partida.get_jugadores():
                j.get_apuesta()

        def flop(self):
            self.partida.mesa_add(self.partida.pick(3))
            for j in self.partida.get_jugadores():
                j.get_apuesta()

        def turn(self):
            self.partida.mesa_add(self.partida.pick())
            for j in self.partida.get_jugadores():
                j.get_apuesta()

        def river(self):
            self.partida.mesa_add(self.partida.pick())
            for j in self.partida.get_jugadores():
                j.get_apuesta()

        def showdown(self):

            [puntuar_mano_7(j.get_mano + self.partida.get_mesa)
             for j in self.partida.get_jugadores()]

        start()
        preflop()
        flop()
        turn()
        river()
