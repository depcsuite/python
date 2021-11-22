print("Bienvenido. Ingrese su nombre...")
nom = input()
nom = nom.upper()
print("Bienvenido ", nom)

print("Ingrese 5 palabras cualesquiera...")
pUno = input("Palabra uno")
pDos = input("Palabra dos")
pTres = input("Palabra tres")
pCuatro = input("Palabra cuatro")
pCinco = input("Palabra cinco")

pUno = pUno.upper() #Primera a mayúsculas
pDos = pDos.lower() #Segunda a minúsculas
nueva = pUno+pDos
primeraLetra = pCinco[0]
ultimaLetra = pCinco[len(pCinco)-1]
pUno = pUno.replace("a"," ")
pUno = pUno.replace("e", " ")
pUno.replace("i", " ")
pUno.replace("o", " ")
pUno.replace("u", " ")

pDos = pDos.replace("a"," ")
pDos = pDos.replace("e", " ")
pDos.replace("i", " ")
pDos.replace("o", " ")
pDos.replace("u", " ")

pTres = pTres.replace("a"," ")
pTres = pTres.replace("e", " ")
pTres.replace("i", " ")
pTres.replace("o", " ")
pTres.replace("u", " ")

pCuatro = pCuatro.replace("a"," ")
pCuatro = pCuatro.replace("e", " ")
pCuatro.replace("i", " ")
pCuatro.replace("o", " ")
pCuatro.replace("u", " ")

pCinco = pCinco.replace("a"," ")
pCinco = pCinco.replace("e", " ")
pCinco.replace("i", " ")
pCinco.replace("o", " ")
pCinco.replace("u", " ")

resultado = pUno+pDos+pTres+pCuatro+pCinco


print(resultado)