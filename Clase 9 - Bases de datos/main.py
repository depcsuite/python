from Pedido import Pedido
from Producto import Producto
from Usuario import Usuario
print(" ---- Programa gestor de pedidos ---- ")
nombre = input("Por favor, ingrese su nombre...")
passw = input("Por favor, ingrese su passw...")
admin = Usuario(0,nombre,passw)
print(" ---- Bienvenido: ", admin.getNombre())
listaProductos = []
codigo = -2
while(codigo!=-1):
    codigo = int(input("Ingrese codigo del nuevo producto o -1 para salir..."))
    if(codigo!=-1):
        nomNuevo = input("Nombre del nuevo producto...")
        descNuevo = input("Descripcion del nuevo producto...")
        precNuevo = float(input("Precio del nuevo producto..."))
        productoNuevo = Producto(codigo, nomNuevo, descNuevo, precNuevo)
        listaProductos.append(productoNuevo)
print("Cargado de productos finalizado. Se ha cargado:")

print("--- Creación de pedido ---")
fecPedido = input("Ingrese fecha del pedido...")
autPedido = admin
codPed = int(input("Ingrese código de pedido..."))
pedido = Pedido(fecPedido, autPedido, codPed)
codigo = -2
while(codigo!=-1):
    print("Elija un producto por código para agregar al pedido o -1 para cerrar el pedido.")
    print("Lista:")
    for p in listaProductos:
        print("C: ", p.getCodigo(), " | N: ", p.getNombre(), " | D: ", p.getDesc(), " | P: ", p.getPrecio())
    codigo = int(input("Elija su código..."))
    if(codigo != -1):
        productoElegido = None
        for producto in listaProductos:
            if producto.getCodigo() == codigo:
                productoElegido = producto
        pedido.agregarProducto(productoElegido)
pedido.imprimirPedido()



