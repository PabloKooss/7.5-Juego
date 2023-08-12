import random

def cartaAzar(cartas):
    cartas_temp = list(cartas)
    registro_aleatorio = random.choice(cartas_temp)
    return registro_aleatorio


def agregarj1(carta,jugador1):
    return jugador1.append(carta)


def quitarCarta(carta,cartas):
    cartas_temp = list(cartas)
    quitar = cartas_temp.remove(carta)
    return quitar