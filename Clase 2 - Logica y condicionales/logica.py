numA = 10
numB = 12
numC = 12
numD = 12
prop = (numA != numB) and (numC != numD) #prop es la conjunción (and) de las proposiciones numA != numB y numC!=numD
propD = (numA != numB) or (numC != numD) #propD es la disyuncion (or) de las proposiciones componentes
propT = (numA != numB and (numA<=10 or numB <11)) or (numC != numD)
#Interpretación:
#propT = (numA != numB and (True)) or (numC != numD)
#propT = ((True) and (True)) or (numC != numD)
#propT = (True) or (numC != numD)
#propT = (True) or (False)
#propT = (True) or (False) = True
#print(propD)
#nom = input("Bienvenido, ingresá tu nombre...")
#nomD = input("Bienvenido, ingresá tu segundo nombre...")
#ordenAlf = (nom > nomD) #Nos fijamos si el primer nombre es alfabéticamente mayor al segundo
print("Bienvenido, por favor ingrese dos números...")
nA = int(input("Ingrese primer número"))
nB = int(input("Ingrese segundo número"))
condicion = nA > nB
if(condicion):
    #Acá escribimos
    #otra linea
    print("El primer número es mayor que el segundo")
elif(nA<nB):
    print("El segundo número es mayor que el primero")
else:
    print("Los números son iguales")
#else:
#    if(nA < nB):
#        print("El segundo número es mayor que el primero")
#    else:
#        print("Los números son iguales")
#    #Código que se ejecuta si la condición NO se cumple

