from matplotlib import pyplot as plt
def fibonacci(n):
    listaNumeros = [0,1]
    primero = 0
    segundo = 1
    if n == 1:
        return listaNumeros[0]
    elif n == 2:
        return listaNumeros[1]
    else:
        for i in range(n):
            fibo = primero+segundo
            listaNumeros.append(fibo)
            primero = segundo
            segundo = fibo
    return listaNumeros

def graficar(lista):
    datosX = [i for i in range(0, len(lista))]
    plt.plot(datosX, lista, 'ro')
    plt.show()

#print(fibonacci(10))        
graficar(fibonacci(5))