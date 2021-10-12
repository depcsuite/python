class Motor:
    __caballosFuerza = None
    __cantCilindros = None
    __cilindrada = None
    __tipoCombustible = None
    def __init__(self, cF, cC, cilindrada, tC):
        self.__caballosFuerza = cF
        self.__cantCilindros = cC
        self.__cilindrada = cilindrada
        self.__tipoCombustible = tC
    def getTipoCombustible(self):
        return self.__tipoCombustible
    def setTipoCombustible(self, tipo):
        self.__tipoCombustible = tipo