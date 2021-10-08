file = open("arcTexto.txt","a")
datos = ["primera linea", "segunda linea","tercera"]
for linea in datos:
    file.write(linea+"\n")
file.close()
