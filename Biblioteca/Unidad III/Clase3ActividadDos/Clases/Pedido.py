from Clases.Conexion import Conexion
from Clases.Producto import Producto
class Pedido:
    __id=None
    __listaProds=None
    __fecPedido= None
    __autPedido= None
    __total= None
    __entregado= None
    __listaPedidos = []
    def __init__(self, codP, fecha, autor):
        self.__fecPedido = fecha
        self.__autPedido = autor
        self.__id = codP
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
    def getId(self):
        return self.__id
    
    def agregarProducto(self, prodPedido):
        self.__listaProds.append(prodPedido)
    def calcularTotal(self):
        for prod in self.__listaProds:
            self.__total = self.__total+prod.getPrecio()
            return self.__total
    def imprimirPedido(self):
        print("Código: ", self.__id)
        print("Fecha: ", self.__fecPedido)
        for producto in self.__listaProds:
            print("Cód:" , producto.getId(), " | Nombre: ", producto.getNombre(), " | Precio: ", producto.getPrecio())
        print(" --- TOTAL --- : ", self.calcularTotal())
    @staticmethod
    def verTodos():
        return Pedido.__listaPedidos
    @staticmethod
    def agregarPedido(pedido, listaProductos):
        con = Conexion()
        con.conectar()
        cur = con.c()
        recs = [pedido]
        sentencia = "INSERT INTO pedido (fecha, fk_id_autor, entregado) VALUES (%s,%s,%s)"
        cur.executemany(sentencia, recs)
        con.grabar()
        ultimoId = "SELECT id FROM pedido ORDER BY id DESC LIMIT 1"
        cur.execute(ultimoId)
        resultado = cur.fetchall()
        for dato in resultado:
            ultimoId = dato
        for producto in listaProductos:
            datos = [(producto, ultimoId,1)]
            sentencia = "INSERT INTO productopedido (fk_id_producto, fk_id_pedido, cantidad) VALUES (%s,%s,%s)"
            cur.executemany(sentencia, datos)
            con.grabar()
        con.desconectar()
    @staticmethod
    def cargarLista():
        con = Conexion()
        con.conectar()
        cur = con.c()
        q = "SELECT pedido.id, fecha, entregado, fk_id_autor FROM pedido INNER JOIN usuario ON pedido.fk_id_autor = usuario.id"
        cur.execute(q)
        resultado = cur.fetchall()
        for pedido in resultado:
            p = Pedido(pedido[0], pedido[1], pedido[2])
            qDos = "SELECT producto.id, producto.nombre, producto.descripcion, producto.precio, producto.stock from productopedido inner join producto on productopedido.fk_id_producto = producto.id " \
            "inner join pedido on pedido.id = productopedido.fk_id_pedido where pedido.id = "+str(p.getId()) 
            cur.execute(qDos)
            productos = cur.fetchall()
            for producto in productos:
                prod = Producto(producto[0], producto[1], producto[2], producto[3], producto[4])
                p.agregarProducto(prod)
            Pedido.__listaPedidos.append(p)
        con.desconectar()
    ###Setters y getters
