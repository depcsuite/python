def verRegistros(archivo):
    arc = open(archivo, "r")
    next(arc)
    for linea in arc:
        print(linea)
    arc.close()
def agregarRegistro(archivo):
    nombre = input("Nombre a agregar")
    apellido = input("Apellido a agregar")
    cargo = input("Cargo")
    sueldo = input("Sueldo")
    linea = nombre+","+apellido+","+cargo+","+sueldo+"\n"
    arc = open(archivo,"a")
    arc.write(linea)
    arc.close()
def sueldoPorCargo(archivo, cargo):
    arc = open(archivo, "r")
    total = 0
    next(arc)
    for linea in arc:
        linea = linea.split(",")
        if(linea[2] == cargo):
            total = total+float(linea[3])
    arc.close()
    return total
verRegistros("datos.csv")
agregarRegistro("datos.csv")
verRegistros("datos.csv")
print(sueldoPorCargo("datos.csv", "Profesor"))