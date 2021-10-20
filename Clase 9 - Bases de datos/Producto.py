class Producto:
    __codigo= None
    __nombre= None
    __desc= None
    __precio= None
    def __init__(self, cod, nom, desc, prec):
        self.__codigo = cod
        self.__nombre = nom
        self.__desc = desc
        self.__precio = prec
    def getCodigo(self):
        return self.__codigo
    def setCodigo(self, cod):
        self.__codigo = cod
    def getNombre(self):
        return self.__nombre
    def getPrecio(self):
        return self.__precio
    def getDesc(self):
        return self.__desc