class Pedido:
    __codPedido=None
    __listaProds=None
    __fecPedido= None
    __autPedido= None
    __total= None
    __entregado= None
    __listaPedidos = []
    def __init__(self, fecha, autor, codP):
        self.__fecPedido = fecha
        self.__autPedido = autor
        self.__codPedido = codP
        self.__listaProds = []
        self.__total = 0
        self.__entregado = False
    def getFecPedido(self):
        return self.__fecPedido
    def getAutPedido(self):
        return self.__autPedido
    def getListaProds(self):
        return self.__listaProds
    def getTotal(self):
        return self.__total
    def getEntregado(self):
        return self.__entregado
    
    def agregarProducto(self, prodPedido):
        self.__listaProds.append(prodPedido)
    def calcularTotal(self):
        for prod in self.__listaProds:
            self.__total = self.__total+prod.getPrecio()
            return self.__total
    def imprimirPedido(self):
        print("Código: ", self.__codPedido)
        print("Fecha: ", self.__fecPedido)
        for producto in self.__listaProds:
            print("Cód:" , producto.getCodigo(), " | Nombre: ", producto.getNombre(), " | Precio: ", producto.getPrecio())
        print(" --- TOTAL --- : ", self.calcularTotal())
    @staticmethod
    def verTodos():
        return Pedido.__listaPedidos
    @staticmethod
    def agregarPedido(pedido):
        Pedido.__listaPedidos.append(pedido)
    ###Setters y getters
