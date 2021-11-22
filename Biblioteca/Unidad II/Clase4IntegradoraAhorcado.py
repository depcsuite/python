from random import randint
def generarPalabra():
    lPalabras = ["perro","murcielago","oficial","desgracia","vida"]
    aleatorio = randint(0,4)
    return lPalabras[aleatorio]
    
def ahorcado():
    intentosPermitidos = 10000
    realizados = 0
    acertadas = []
    print("Bienvenido al juego del ahorcado")
    palabra = generarPalabra()
    print("Se ha generado una palabra de ", len(palabra) ," letras")
    print(palabra)
    while(realizados < intentosPermitidos and len(acertadas) < len(palabra)):
       print("Ingrese un intento de letra...")
       letra = input("")
       if letra in palabra:
           print("Bien. Ha acertado una de las letras")
           acertadas.append(letra)
           faltan = len(palabra)-len(acertadas)
           print("Falta acertar ", faltan, " letras")
    if(realizados <= intentosPermitidos):
        print("Muy bien. Victoria.")
        print("Palabra: ", palabra)
    else:
        print("Se acabaron los intentos posibles")
        
ahorcado()