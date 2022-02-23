from Tablero import *

class Main:

    casillas = 15
    jugadores = 5
    tablero = Tablero(casillas, jugadores, 0)

    while(tablero.getPlayerPosition() <= casillas):
        tablero.moverJugador()