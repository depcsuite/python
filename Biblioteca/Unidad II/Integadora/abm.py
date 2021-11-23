from Clases.Usuario import Usuario
from Clases.Producto import Producto
from Clases.Pedido import Pedido
print("Bienvenido, por favor ingrese su nombre y su contraseña...")
nom = input("Usuario...")
pas = input("Password...")
while(Usuario.validar(nom, pas) == False):
    print("El usuario NO existe, ingrese nuevamente...")
    nom = input("Usuario...")
    pas = input("Password...")
datosUs = Usuario.validar(nom, pas)
idUs = datosUs[0]
nombreU = datosUs[1]
print("Bienvenido, identificado correctamente...")
print("1 - Ver lista de productos\n2 - Crear nuevo producto\n3 - Registrar nuevo pedido\n4 - Ver pedidos")
opc = int(input("Ingrese su selección ó -1 para salir"))
while(opc != -1):
    if opc == 1:

        for prod in Producto.verTodos() :
            print(prod.getCodigo(), " ", prod.getNombre()," ",prod.getPrecio(),"\n")
    elif opc == 2:
        i = int(input("ID del nuevo producto"))
        n = input("Nombre del nuevo producto")
        d = input("Descripción del nuevo producto")
        p = int(input("Precio del nuevo producto"))
        m = (input("Marca del nuevo producto"))
        tupla = (i,n,d,p,m)
        Producto.agregarProducto(tupla)
    elif opc == 3:
        f = input("Ingrese fecha del pedido (dd/mm/yyyy)")
        idP = int(input("Ingrese ID del pedido"))
        total = 0
        entregado = 'false'
        tupla = (f, idUs, total, entregado)
        pedido = Pedido(f, idUs, idP)

        print(" ---- Ingrese los productos que estarán en el pedido (-1 para dejar de cargar) ----")
        for prod in Producto.verTodos() :
            print(prod.getCodigo(), " ", prod.getNombre()," ",prod.getPrecio(),"\n")
        idACargar = int(input("Ingrese el ID que desea cargar (-1 para cerrar)"))
        while(idACargar != -1):
            prodCargar = Producto.verPorID(idACargar)
            pedido.agregarProducto(prodCargar)

            idACargar = int(input("Ingrese el ID que desea cargar (-1 para cerrar)"))
        Pedido.agregarPedido(pedido)
    elif opc == 4:

        for res in Pedido.verTodos():
            print("----------------------")
            res.imprimirPedido()
            print("-----------------------")     

    else:
        print("Opción inválida")
    print("1 - Ver lista de productos\n2 - Crear nuevo producto\n3 - Registrar nuevo pedido\n4 - Ver pedidos")
    opc = int(input("Ingrese su selección ó -1 para salir"))
