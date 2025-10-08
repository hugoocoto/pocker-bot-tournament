from itertools import combinations
from collections import Counter

VALORES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
           '7': 7, '8': 8, '9': 9, '10': 10,
           'J': 11, 'Q': 12, 'K': 13, 'A': 14}

# Vive coded -- no aseguro que funcione


def puntuar_mano_5(mano):
    valores = sorted([VALORES[c[:-1]] for c in mano], reverse=True)
    palos = [c[-1] for c in mano]
    conteo = Counter(valores)
    orden = sorted(conteo.items(), key=lambda x: (-x[1], -x[0]))
    grupos = [v for v, _ in orden]
    rep = [n for _, n in orden]
    color = len(set(palos)) == 1
    escalera = all(valores[i] - 1 == valores[i + 1] for i in range(4))
    if valores == [14, 5, 4, 3, 2]:
        escalera, valores = True, [5, 4, 3, 2, 1]
    if color and escalera and valores[0] == 14:
        base = 9000000
    elif color and escalera:
        base = 8000000
    elif 4 in rep:
        base = 7000000
    elif 3 in rep and 2 in rep:
        base = 6000000
    elif color:
        base = 5000000
    elif escalera:
        base = 4000000
    elif 3 in rep:
        base = 3000000
    elif rep.count(2) == 2:
        base = 2000000
    elif 2 in rep:
        base = 1000000
    else:
        base = 0
    extra = sum(v * (100 ** (len(grupos) - i - 1))
                for i, v in enumerate(grupos))
    return base + extra


def puntuar_mano_7(cartas):
    cartas = [str(c) for c in cartas]
    return max(puntuar_mano_5(comb) for comb in combinations(cartas, 5))
