primeraLista = []
sLista = [30,"Luca",12.73,"Mitas", primeraLista]
#Longitud de una lista: len(lista)
#Las listas también soportan slicing
#print(sLista[::-1])
sLista[1] = "Cristian"
#Listas por comprensión: se expresa una REGLA de inclusión, que debe cumplir un determinado elemento
# para pertenecer a la lista.
#pares = [i*2 for i in range(1000)]
#print(pares)
#Agregar datos dinámicamente a una lista; es decir, crearla vacía e ir expandiéndola
# a medida que necesitamos
usuarios = []
usuarios.append("Luca")#0
usuarios.append("Cristian")#1
#print("Cristian está en posición : ", usuarios.index("Cristian"))
usuarios.append("Mitas")#2
usuarios.remove("Luca")
#print("Cristian está en posición : ", usuarios.index("Cristian"))
texto = "Esto es un texto bastante largo"
#Texto a lista, separado por un determinado caracter
texto = texto.split(" ")
print(texto)