from game import Action, Juego
from bot import Bot
import sys


def play(estado: Juego) -> Action:
    return Action("Hello 1")


def main():
    if (len(sys.argv) != 3):
        print(f"Usage: {sys.argv[0]} IP PORT")
        sys.exit(0)

    b = Bot()
    b.connect(*sys.argv[1:])
    b.register(play)
    b.start()
    b.disconnect()


if __name__ == '__main__':
    main()
