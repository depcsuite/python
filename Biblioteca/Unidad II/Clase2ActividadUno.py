tupla = (1,2,2,4,1)
listaTemporal = list(tupla)
listaResultado = []
for elemento in tupla:
    if listaTemporal.count(elemento) == 1:
        listaResultado.append(elemento)
nueva = tuple(listaResultado)
print(nueva)