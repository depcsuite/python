def parImpar(numero):
    if(numero%2==0):
        return "Es par"
    else:
        return "Es impar"
def paresMenores(n):
    resultado = []
    i = 0
    while(i<=n):
        if(i%2 == 0):
            resultado.append(i)
        i = i+1
    return resultado
def mitad(palabra):
    corte = len(palabra)//2
    mitadUno = palabra[:corte]
    mitadDos = palabra[corte:]
    return mitadUno, mitadDos
print(mitad("lucas"))