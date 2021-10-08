def funcionEjemplo(): #Declaración
	print("Un ejemplo...")
def operaciones(x): #Declaración. “x” representa el parámetro.
	resultado = 2*x+1
	return resultado
def aMinuscula(texto):
    return texto.lower()
def saludar(nom, apellido):
    return ("Bienvenido " + nom + " " + apellido)

def tieneVocales(texto):
    vocales=False
    if ("a" in texto) or ("e" in texto) or ("i" in texto) or ("o" in texto) or ("u" in texto):
        vocales = True
    return (texto, vocales)

def cuentaVocales(texto):
    #["a","e","i","o","u"]
    # [1,0,3,1,2]
    lVocales = ["a","e","i","o","u"]
    cVocales = [0,0,0,0,0]
    for letra in texto:
        if letra == "a":
            cVocales[0] = cVocales[0]+1
        elif letra == "e":
            cVocales[1] = cVocales[1]+1
        elif letra == "i":
            cVocales[2] = cVocales[2]+1
        elif letra == "o":
            cVocales[3] = cVocales[3]+1
        elif letra == "u":
            cVocales[4] = cVocales[4]+1
    return (lVocales, cVocales)

def rellenarLista(lista):
    for i in range(10):
        lista.append(i)
    return lista
#def duplicarNumero(): #Esto directamente NO compila, porque aunque la variable "unNumero" SI existe
    # en el exterior de la función, es de tipo int (no es una estructura como lista o tupla) y por ende
    # no es visible en el interior de la función salvo que la pase como parámetro
    #unNumero = unNumero*2

def saludoDos(nombre="Persona", apellido="Desconocida"):
    return ("Bienvenido " + nombre + " " + apellido)


def paresMenores(n):
    resultado = []
    i = 0
    while(i<=n):
        if(i%2 == 0):
            resultado.append(i)
        i = i+1
    return resultado


def esPrimo(n):
    primo = True
    i = 2
    while(i<n//2):
        #print("Dividiendo ", n , " por " , i)
        if(n%2 == 0):
            primo = False
        i = i+1
    return primo
