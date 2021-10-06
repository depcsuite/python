#Bucle 
condicion = (2!=3)
#Bucle "while()"
i = 0
while(i>100):
    print(i)
    i = i+1

#for i in range(100):
#    print(i)

lista = [98,7,12,5,"r",9]
lPalabras = ["murcielago", "oficial", "luca", "hoy", "te"]
lconA = []
i = 0
#while(i<len(lPalabras)):
#    if("a" in lPalabras[i]):
#        lconA.append(lPalabras[i])
#    i = i+1

palBuscada = input("Ingrese una palabra para ver si está presente en la lista o escriba FIN para cerrar el programas")

while(palBuscada != "FIN"):
    if palBuscada not in lPalabras:
        print("La palabra que querés buscar no está en la lista...")
    else:
        for i in range(len(lPalabras)):
            if(lPalabras[i] == palBuscada):
                lconA.append(lPalabras[i])
        print("Palabra encontrada: ", lconA)
    palBuscada = input("Ingrese una palabra para ver si está presente en la lista o escriba FIN para cerrar el programas")














#i = 0
#palabraSecreta = "wendy"
#acertijo = input("Ingresá una palabra a ver si adivinás la clave...")
#while(acertijo!=palabraSecreta):
#    print("Erorr, ésa es no es la clave...")
#    acertijo = input("Ingresá una palabra a ver si adivinás la clave...")
#print("Perfecto, adivinaste.")
###################################

###################################
