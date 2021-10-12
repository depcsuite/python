class Auto:
    __color = None
    __puertas = None
    __tamanio = None
    __velMaxima = None
    __CV = None

    def __init__(self, col, puer, tamanio, velMax, cv):
        self.__color = col
        self.__puetas = puer
        self.__tamanio = tamanio
        self.__velMaxima = velMax
        self.__CV = cv

    def getColor(self):
            return self.__color

    def setColor(self,color):
            self.__color = color
        
    def getPuertas(self):
            return self.__puertas

    def setPuertas(self,puertas):
            self.__puertas = puertas
    def getTamanio(self):
        return self.__tamanio

    def setTamanio(self, tamanio):
        self.__tamanio = tamanio

    def getVelMax(self):
        return self.__velMax

    def setVelMax(self,velMax):
        self.__velMax = velMax
