from modos_juego.JvsJ import *
from modos_juego.JvsCOM import *
from modos_juego.COMvsCOM import *
import os
import time

cartas = [
        ("As♠",1),("2♠",2),("3♠",3),("4♠",4),("5♠",5),("6♠",6),("7♠",7),("10♠",0.5),("11♠",0.5),("12♠",0.5),
        ("As♡ ",1),("2♡ ",2),("3♡ ",3),("4♡ ",4),("5♡ ",5),("6♡ ",6),("7♡ ",7),("10♡ ",0.5),("11♡ ",0.5),("12♡",0.5),
        ("As♢",1),("2♢",2),("3♢",3),("4♢",4),("5♢",5),("6♢",6),("7♢",7),("10♢",0.5),("11♢",0.5),("12♢",0.5),
        ("As♣",1),("2♣",2),("3♣",3),("4♣",4),("5♣",5),("6♣",6),("7♣",7),("10♣",0.5),("11♣",0.5),("12♣",0.5)]

while True:
    resp = input(f"Elige modo de juego:\n 1.- J vs J\n 2.- J vs COM\n 3.- COM vs COM\n 4.- Salir\n")
    match resp:
        case "1":
            print("\n","*"*19,"\n *   Modo J vs J   *\n","*"*19)
            carta = juego_jvsj(cartas)
        case "2":
            print("\n","*"*21,"\n *   Modo J vs COM   *\n","*"*21)
            carta = juego_jvscom(cartas)
        case "3":
            print("\n","*"*23,"\n *   Modo COM vs COM   *\n","*"*23)
            carta = juego_comvscom(cartas)
        case "4":
            print("Fin del juego")
            time.sleep(1)
            os.system("clear")
            break
        case _:
            os.system('clear')
            print("Opcion invalida")
