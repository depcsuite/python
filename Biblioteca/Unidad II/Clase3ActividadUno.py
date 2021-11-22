lU = [2,2]
lD = [1,3]
lT = [4,5]
tuplaDos = (lU,lD,lT)

lC = [6,6]
lCi = [9,9]
lS = [0,12]
tuplaTres = (lC,lCi,lS)

lSi = [3,3]
lO = [12,8]
lN = [1,7]
tuplaCuatro = (lSi,lO,lN)

tuplaPrincipal = (tuplaDos, tuplaTres, tuplaCuatro)

#Revisemos los repetidos que pueda haber en la "tuplaDos"
sinRepetidos = set(tuplaDos[0]) #Primera lista de "tuplaDos"
sinRepetidosU = list(sinRepetidos) #Convierto nuevamente a lista, pero ya sin los repetidos
sinRepetidos = set(tuplaDos[1]) #Segunda lista de "tuplaDos"
sinRepetidosD = list(sinRepetidos) #Convierto nuevamente a lista, pero ya sin los repetidos
sinRepetidos = set(tuplaDos[2]) #Tercera lista de "tuplaDos"
sinRepetidosT = list(sinRepetidos) #Convierto nuevamente a lista, pero ya sin los repetidos
tuplaSinRepetidos = (sinRepetidosU, sinRepetidosD, sinRepetidosT)

tuplaDos = tuplaSinRepetidos #TuplaDos sin repetidos

#Revisemos los repetidos que pueda haber en la "tuplaTres"
sinRepetidos = set(tuplaTres[0]) #Primera lista de "tuplaDos"
sinRepetidosU = list(sinRepetidos) #Convierto nuevamente a lista, pero ya sin los repetidos
sinRepetidos = set(tuplaTres[1]) #Segunda lista de "tuplaDos"
sinRepetidosD = list(sinRepetidos) #Convierto nuevamente a lista, pero ya sin los repetidos
sinRepetidos = set(tuplaTres[2]) #Tercera lista de "tuplaDos"
sinRepetidosT = list(sinRepetidos) #Convierto nuevamente a lista, pero ya sin los repetidos
tuplaSinRepetidos = (sinRepetidosU, sinRepetidosD, sinRepetidosT)

tuplaTres = tuplaSinRepetidos #TuplaTres sin repetidos

#Revisemos los repetidos que pueda haber en la "tuplaCuatro"
sinRepetidos = set(tuplaCuatro[0]) #Primera lista de "tuplaDos"
sinRepetidosU = list(sinRepetidos) #Convierto nuevamente a lista, pero ya sin los repetidos
sinRepetidos = set(tuplaCuatro[1]) #Segunda lista de "tuplaDos"
sinRepetidosD = list(sinRepetidos) #Convierto nuevamente a lista, pero ya sin los repetidos
sinRepetidos = set(tuplaCuatro[2]) #Tercera lista de "tuplaDos"
sinRepetidosT = list(sinRepetidos) #Convierto nuevamente a lista, pero ya sin los repetidos
tuplaSinRepetidos = (sinRepetidosU, sinRepetidosD, sinRepetidosT)

tuplaCuatro = tuplaSinRepetidos #TuplaCuatro sin repetidos

print("Tupla principal original: ", tuplaPrincipal)
tuplaPrincipal = (tuplaDos, tuplaTres, tuplaCuatro)
print("Nueva tupla principal: ", tuplaPrincipal)