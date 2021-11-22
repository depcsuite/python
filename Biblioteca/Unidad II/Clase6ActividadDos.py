class Auto:
    __color = None
    __cantidadPilas = None
    __tamanio = None
    def __init__(self, color, cPilas):
        self.__color = color
        self.__cantidadPilas = cPilas
    def getColor(self):
        return self.__color
    def setColor(self,c):
        self.__color = c
    #Otros getters y setters
class BochaPlastica:
    __color = None
    __tamanio = None
    #Getters y setters
class Trompo:
    __color = None
    __material = None
    #Constructor, getter y setter
class BanditaElasticas:
    __color = None
    __grosor = None
    __forma = None
    #Constructor, getters y setters
