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

def llenarLista():#Esto funciona pero lo consideramos una mala práctica, porque modifica directamente
    #una variable creada en el exterior de la función.
    #Esto es posible porque la variable contiene una estructura (lista)
    for i in range(10):
        ejemplo.append(i)

def rellenarLista(lista):
    for i in range(10):
        lista.append(i)
    return lista
#def duplicarNumero(): #Esto directamente NO compila, porque aunque la variable "unNumero" SI existe
    # en el exterior de la función, es de tipo int (no es una estructura como lista o tupla) y por ende
    # no es visible en el interior de la función salvo que la pase como parámetro
    #unNumero = unNumero*2
def duplicarNumeroGlobal(): #Esto SI funciona.
    #Porque indicamos expresamente con la palabra clave "global" que la variable "unNumero" está creada
    # en el exterior de la función
    global unNumero #En esta variable global vive el número 10 (línea 59)
    unNumero = unNumero*2 #"Piso" el valor 10 y lo reemplazo por 10*2 = 20

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




#print(esPrimo(20000))

#palabras = ["luca","mitas","avion","murcielago"]

#masDeCinco = list(filter(lambda x: len(x)<5, palabras))
#Esto signific que vamos a conservar,a filtrar, aquellos elementos de la lista "palabras" cuya longitud sea mayor a cinco
#print(palabras)
#print(masDeCinco)
#Nos da los pares dede 0 hasta 99


#saludando = lambda nom,ap: ("Hola " + nom + " " + ap)
#elevarA = lambda a, b: a**b
#print("El número vale ", 5)
#print(saludando("Luca","Mitas"))
unNumero = 10



#print("Un número vale: ", unNumero)
#duplicarNumeroGlobal()

#print("Después de la llamada un número vale: ", unNumero)

ejemplo = []
#ejemplo = rellenarLista(ejemplo)
#print(ejemplo)

#print(operaciones(2000))
#print(operaciones(10))
#print(operaciones(5)) #Invocación. Al hacerlo, “x” se reemplaza por el numero
#que nosotros queramos.
#Este código declara una función, le da un breve cuerpo y finalmente la invoca por su nombre pasándole el número 5 como parámetro.
#Al hacerlo, el código de la función es ejecutado y se imprime “11” por pantalla.

#funcionEjemplo() #Invocación
#Este código declara una función, le da un breve cuerpo y finalmente la invoca por su nombre
#Al hacerlo, el código de la función es ejecutado y se imprime “Un ejemplo” por pantalla.
