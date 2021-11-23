class Producto:
    __codigo= None
    __nombre= None
    __desc= None
    __precio= None
    __marca = None
    __listaProductos = []
    def __init__(self, cod, nom, desc, prec, marc):
        self.__codigo = cod
        self.__nombre = nom
        self.__desc = desc
        self.__precio = prec
        self.__marca = marc
    def getMarca(self):
        return self.__marc
    def setMarca(self, marc):
        self.__marca = marc
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
    @staticmethod
    def verPorID(id):
        for prod in Producto.__listaProductos:
            if(prod.getCodigo() == id):
                return prod
        return None
    @staticmethod
    def verTodos():
        return Producto.__listaProductos
    @staticmethod
    def agregarProducto(prod):
        p = Producto(prod[0], prod[1], prod[2], prod[3], prod[4])
        Producto.__listaProductos.append(p)