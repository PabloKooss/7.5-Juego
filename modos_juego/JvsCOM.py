from cartas.acciones import *
import time
import os

def juego_jvscom(cartas):
    turnos = [True, True]
    jugador1 = []
    jugador2 = []
    suma_J1 = 0
    suma_J2 = 0
    cartas_temp = list(cartas)
    eleccion = ["Si","si","No","no"]
    while True:
        if turnos[0] == True:
            carta = cartaAzar(cartas_temp)
            print("_"*30,"\nJugador 1, tu carta es:\n", carta)
            jugador1.append(carta)
            print("Tus cartas son:", jugador1)
            cartas_temp.remove(carta)
            time.sleep(4)
            resp = input("¿Quieres salir J1?\n")
            if resp == "si" or resp == "Si":
                suma_J1 = sum(numero for _, numero in jugador1 if isinstance(numero, (int, float)))
                print("Elegiste salir J1")
                turnos[0] = False
                os.system("clear")
        if turnos[1] == True:
            carta = cartaAzar(cartas_temp)
            print("_"*30,"\nComputadora, tu carta es:\n", carta)
            jugador2.append(carta)
            print("Tus cartas son:", jugador2)
            cartas_temp.remove(carta)
            time.sleep(4)
            resp = random.choice(eleccion)
            if resp == "si" or resp == "Si":
                suma_J2 = sum(numero for _, numero in jugador2 if isinstance(numero, (int, float)))
                print("Elegiste salir J2")
                turnos[1] = False
                os.system("clear")
        if not any(turnos):  # Utilizamos 'not any' para verificar si ambos turnos son False
            print("El tablero del Jugador 1 es:", suma_J1, "\nEl tablero del Jugador 2 es:", suma_J2)
            if suma_J1 > 7.5 and suma_J2 > 7.5:
                print("Ambos jugadores perdieron")
            elif suma_J1 == suma_J2:
                print("Ambos jugadores empataron")
            elif suma_J1 <= 7.5 and suma_J2 > 7.5:
                print("El Jugador 1 ¡¡¡GANO!!!")
            elif suma_J2 <= 7.5 and suma_J1 > 7.5:
                print("El Jugador 2 ¡¡¡GANO!!!")
            elif suma_J1 <= 7.5 and suma_J1 > suma_J2:
                print("El Jugador 1 ¡¡¡GANO!!!")
            elif suma_J2 <= 7.5 and suma_J2 > suma_J1:
                print("El Jugador 2 ¡¡¡GANO!!!")
            else:
                print("Error")
            print("Ambos decidieron salir")
            time.sleep(5)
            os.system("clear")
            break
