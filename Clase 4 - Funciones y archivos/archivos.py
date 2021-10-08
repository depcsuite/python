file = open("datos.csv","r")
#file.next() # Esto no va a trabajar si está por fuera
next(file) #Esto SÍ va a trabajar
for linea in file:
    formateado = linea.split(",")
    print("Nombre: ", formateado[0], " | Apellido: ", formateado[1], " | DNI: ", formateado[2])
file.close()
#Observar que se utiliza for
