from Clases.Conexion import Conexion
class Producto:
    __id= None
    __nombre= None
    __desc= None
    __precio= None
    __marca = None
    __listaProductos = []
    def __init__(self, cod, nom, desc, prec, sto):
        self.__id = cod
        self.__nombre = nom
        self.__desc = desc
        self.__precio = prec
        self.__stock = sto
    def getStock(self):
        return self.__stock
    def setStock(self, sto):
        self.__stock = sto
    def getId(self):
        return self.__id
    def setId(self, cod):
        self.__id = cod
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
        Producto.cargarLista()
        return Producto.__listaProductos
    @staticmethod
    def agregarProducto(prod):
        con = Conexion()
        con.conectar()
        cur = con.c()
        sentencia = "INSERT INTO producto(nombre, descripcion, precio, stock) VALUES (%s,%s,%s,%s)"
        recs = [prod]
        cur.executemany(sentencia, recs)
        con.grabar()
        con.desconectar()
    @staticmethod
    def cargarLista():
        con = Conexion()
        con.conectar()
        cur = con.c()
        q = "SELECT * FROM producto"
        cur.execute(q)
        resultado = cur.fetchall()
        for i, res in enumerate(resultado):
            temp = Producto(res[0], res[1], res[2], res[3], res[4]) #Esto NO es un producto, es una tuplap
            if len(Producto.__listaProductos) > 0 and i < len(Producto.__listaProductos):
                if temp.getId() != Producto.__listaProductos[i].getId():
                    Producto.__listaProductos.append(temp)
            else:
                Producto.__listaProductos.append(temp)
                
        con.desconectar()