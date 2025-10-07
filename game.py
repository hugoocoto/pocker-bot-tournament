class State:
    def __init__(self):
        pass


class Action:
    def __init__(self, text):
        self.text = text
        pass

    def __str__(self):
        return self.text


class Card:
    def __init__(self):
        pass


class Jugador:
    cartas_llevadas: list[Card]
    puntos: int


class Juego:
    jugadores: list[Jugador]
    mano: list[Card]
    mesa: list[Card]

    def __init__(self):
        pass
