from Clases.Usuario import Usuario
from Clases.Producto import Producto
from Clases.Pedido import Pedido
from datetime import datetime
print("Bienvenido, por favor ingrese su nombre y su contraseña...")
nom = input("Usuario...")
pas = input("Password...")
validado = Usuario.validar(nom, pas) 
while(validado == False):
    print("El usuario NO existe, ingrese nuevamente...")
    nom = input("Usuario...")
    pas = input("Password...")
    validado = Usuario.validar(nom, pas)

idUs = validado[0] #Tiene idUsuario y nombreUsuario
nombreUs = validado[1]
print("Bienvenido, ", nombreUs, " identificado correctamente...")
print("1 - Ver lista de productos\n2 - Crear nuevo producto\n3 - Registrar nuevo pedido\n4 - Ver pedidos")
opc = int(input("Ingrese su selección ó -1 para salir"))
while(opc != -1):
    if opc == 1:
        for prod in Producto.verTodos() :
            print(prod.getId(), " ", prod.getNombre()," ",prod.getPrecio(),"\n")
    elif opc == 2:
        n = input("Nombre del nuevo producto: ")
        d = input("Descripción del nuevo producto: ")
        p = float(input("Precio del nuevo producto: "))
        m = int(input("Stock del nuevo producto: "))
        tupla = (n,d,p,m)
        Producto.agregarProducto(tupla)
    elif opc == 3:
        listaIds = []
        f = input("Ingrese fecha del pedido (dd/mm/yy)")
        f = datetime.strptime(f, '%d/%m/%y')
        print(" ---- Ingrese los productos que estarán en el pedido (-1 para dejar de cargar) ----")
        for prod in Producto.verTodos() :
            print(prod.getId(), " ", prod.getNombre()," ",prod.getPrecio(),"\n")
        idACargar = int(input("Ingrese el ID que desea cargar (-1 para cerrar)"))
        listaIds.append(idACargar)
        total = 0
        entregado = 'false'
        tupla = (f, idUs, entregado)
        print(" ---- Ingrese los productos que estarán en el pedido (-1 para dejar de cargar) ----")
        for prod in Producto.verTodos() :
            print(prod.getId(), " ", prod.getNombre()," ",prod.getPrecio(),"\n")
        idACargar = int(input("Ingrese el ID que desea cargar (-1 para cerrar)"))
        while(idACargar != -1):
            listaIds.append(idACargar)
            idACargar = int(input("Ingrese el ID que desea cargar (-1 para cerrar)"))
        Pedido.agregarPedido(tupla,listaIds)
    elif opc == 4:
        Pedido.cargarLista()
        for res in Pedido.verTodos():
            print("----------------------")
            res.imprimirPedido()
            print("-----------------------")     

    else:
        print("Opción inválida")
    print("1 - Ver lista de productos\n2 - Crear nuevo producto\n3 - Registrar nuevo pedido\n4 - Ver pedidos")
    opc = int(input("Ingrese su selección ó -1 para salir"))
