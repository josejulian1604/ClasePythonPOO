from Ficha import *

class Tablero:

    #Defina aquí los atributos de Tablero
    casillas = 0
    jugadores = 0


    #también va a necesitar una lista de Fichas (puede asumir un número de Fichas fijo si le parece más fácil), 
    #y un mecanismo para saber quién sigue en el turno
    fichas = [Ficha("verde"), Ficha("rojo"), Ficha("azul"), Ficha("amarillo"), Ficha("negro")]
    jugadorMoviendo = 0  #indice para el array



    #agregue parámetros necesarios después de self
    #para iniciar los valores de sus atributos

    def __init__(self, casillas, jugadores, jugadorMoviendo):
        #inicialice aquí todos los atributos
        #no olvide usar self.atributo para acceder el atributo de la clase
        self.casillas = casillas
        self.jugadores = jugadores
        self.jugadorMoviendo = jugadorMoviendo

#defina aquí los métodos de Tablero
#recuerde que el primer parámetro de cada método es siempre self
    def moverJugador(self):
        if(jugadorMoviendo <= 4):
            fichas[jugadorMoviendo].avanzar()
            jugadorMoviendo += 1
    
        else:
            jugadorMoviendo = 0
    
    def getPlayerPosition(self):
        return self.fichas[self.jugadorMoviendo].posicion
