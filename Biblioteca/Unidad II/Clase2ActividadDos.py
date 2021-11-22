nombre = input("Bienvenido al programa, ingresá tu nombre...")
print("Hola, ", nombre, ". Por favor, elegí una de las siguientes opciones...")
print("1-Detectar mayor de 3 números\n2-Identificar un horario\n3-Decidir si suma de cifras deun número de 3 digitos es par o impar\n4-Descomponer un número de cinco dígitos y mostrar las cifras invertidas")
opc = int(input("Ingresá tu selección..."))
if (opc == 1):
    print("Ingresá 3 números enteros. Vamos a detectar cuál es el mayor.")
    numA = int(input("Primer número...")) # 12
    numB = int(input("Segundo número...")) #12
    numC = int(input("Tercer número")) #2
    
    if(numA >= numB and numA >= numC):
        print("El mayor es el ", numA)
    elif(numB >= numA and numB >= numC):
        print("El mayor es el ", numB)
    else:
        print("El mayor es el ", numC)

elif (opc == 2):
    print("Elegida opción 2...")
    horas = int(input("Ingrese horas"))
    minutos = int(input("Ingrese minutos"))
    if(horas >= 12 and horas <= 18 and minutos <= 30):
        print("Es de tarde")
    elif((horas >= 18 and horas <= 23) or (horas == 18 and minutos > 30)):
        print("Es de noche")
    else:
        print("Es la mañana")
elif opc == 3:
    print("Elegida opción 3...")
    numero = input("Ingrese un número de tres cifras")
    num = str(numero)
    suma = int(num[0])+int(num[1])+int(num[2])
    if(suma%2 == 0):
        print("Es par")
    else:
        print("Es impar")
else:
    numero = int(input("Ingrese un número de cinco cifras..."))
    #numero = 10324
    #numero%10 = 4
    #numero = numero//10 queda 1032
    #numero%10 = 2
    #numero = numero//10 queda
    ## juego
    numero = str(numero) #10324
    numero = list(numero) #['1','0','3','2','4']

    numero[0] = int(numero[0])#int('1')
    numero[1] = int(numero[1])#int('0')
    numero[2] = int(numero[2])#int('3')
    numero[3] = int(numero[3])#int('2')
    numero[4] = int(numero[4])#int('4')
    #[1,0,3,2,4]
    lNueva = []
    if(numero[0] % 2 == 0): #Si el resto de dividir numero[0] entre 2 es 
        #Se lee numero[0] módulo 2
        lNueva.append(numero[0])
    if(numero[1] %2 == 0):
        lNueva.append(numero[1])
    if(numero[2] %2 == 0):
        lNueva.append(numero[2])
    if(numero[3] %2 == 0):
        lNueva.append(numero[3])
    if(numero[4] %2 == 0):
        lNueva.append(numero[4])
    print(lNueva[::-1])



