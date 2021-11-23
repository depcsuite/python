class Usuario:
    __idU =  None
    __nombreU = None
    __passU = None
    __autorizados = [(1,"luka","pass"),(2,"cristian","mitas")]
    def __init__(self, id=None, nom=None, passw=None):
        self.__idU = id
        self.__nombreU = nom
        self.__passU = passw
    def getNombre(self):
        return self.__nombreU
    def setNombre(self, n):
        self.__nombreU = n
    @staticmethod
    def validar(usuario, passw):
        for tupla in Usuario.__autorizados:
            if(tupla[1]== usuario and tupla[2] == passw):
                return tupla
        return False
            
        