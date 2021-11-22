class Articulo:
    __id = None
    __nombre = None
    __precio = None
    __marca = None
    __modelo = None
    
class Sector:
    __id = None
    __nombre = None
    __listaArticulos = None #Aquí existe COMPOSICIÓN. 
    #Si se elimina un sector, se eliminan también los artículos que contiene
    
    
class Marca:
    __id = None
    __nombre = None
    __listaModelos = None
    
class Modelo:
    __id = None
    __nombre = None
    __especificaciones = None