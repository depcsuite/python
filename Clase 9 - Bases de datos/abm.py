from Conexion import Conexion
con = Conexion()
con.conectar()
cur = con.c()
print("Bienvenido, por favor ingrese su nombre y su contraseña...")
nom = input("Usuario...")
pas = input("Password...")
query = "SELECT * FROM usuario WHERE nombreusuario = '"+nom+"' AND passusuario = '"+pas+"'"
cur.execute(query)
r = cur.fetchall() #Lista de resultados
while(len(r) == 0):
    print("El usuario NO existe, ingrese nuevamente...")
    nom = input("Usuario...")
    pas = input("Password...")
    query = "SELECT * FROM usuario WHERE nombreusuario = '"+nom+"' AND passusuario = '"+pas+"'"
    cur.execute(query)
    r = cur.fetchall()

print("Bienvenido, identificado correctamente...")
print("1 - Ver lista de productos\n2 - Crear nuevo producto")
opc = int(input("Ingrese su selección ó -1 para salir"))
while(opc != -1):
    if opc == 1:
        q = "SELECT * FROM producto"
        cur.execute(q)
        resultado = cur.fetchall()
        for res in resultado:
            print(res)
    elif opc == 2:
        n = input("Nombre del nuevo producto")
        d = input("Descripción del nuevo producto")
        p = int(input("Precio del nuevo producto"))
        s = int(input("Stock del nuevo producto"))
        tupla = (n,d,p,s)
        sentencia = "INSERT INTO producto (nombre, descripcion, precio, stock) VALUES (%s,%s,%s,%s)"
        recs = [tupla]
        cur.executemany(sentencia, recs)
        con.grabar()
    else:
        print("Opción inválida")
    print("1 - Ver lista de productos\n 2 - Crear nuevo producto")
    opc = int(input("Ingrese su selección ó -1 para salir"))


con.desconectar()
