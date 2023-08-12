from modos_juego.JvsJ import *
import os
import time

cartas = [
        ("As♠",1),("2♠",2),("3♠",3),("4♠",4),("5♠",5),("6♠",6),("7♠",7),("10♠",0.5),("11♠",0.5),("12♠",0.5),
        ("As♡ ",1),("2♡ ",2),("3♡ ",3),("4♡ ",4),("5♡ ",5),("6♡ ",6),("7♡ ",7),("10♡ ",0.5),("11♡ ",0.5),("12♡",0.5),
        ("As♢",1),("2♢",2),("3♢",3),("4♢",4),("5♢",5),("6♢",6),("7♢",7),("10♢",0.5),("11♢",0.5),("12♢",0.5),
        ("As♣",1),("2♣",2),("3♣",3),("4♣",4),("5♣",5),("6♣",6),("7♣",7),("10♣",0.5),("11♣",0.5),("12♣",0.5)]
jugador1 = []
jugador2 = []

while True:
    
    resp = input(f"Elige modo de juego:\n 1.- J vs J\n 2.- J vs COM\n 3.- COM vs COM\n 4.- Salir\n")
    match resp:
        case "1":
            print("Modo J vs J")
            carta = juego(cartas,jugador1,jugador2)
            len(cartas)
            print(carta)
            
            '''
            
            print("Carta al azar:", carta)
            
            insertar = agregarj1(carta,jugador1)
            print("Jugador 1:", jugador1)
            quitarCarta(carta)
            
            print("Cartas restantes:", cartas)'''
            len(cartas)
            time.sleep(5)
            
        case "2":
            os.system('clear')
            print("Modo J vs COM")
            time.sleep(3)
        case "3":
            os.system('clear')
            print("Modo COM vs COM")
            time.sleep(3)
        case "4":
            os.system('clear')
            print("Fin del juego")
            time.sleep(3)
            break
        case _:
            os.system('clear')
            print("Opcion invalida")
            time.sleep(3)

'''carta = cartaAzar()
print("Carta al azar:", carta)

agregarj1(carta)
print("Jugador 1:", jugador1)

quitarCarta(carta)
print("Cartas restantes:", cartas)
'''