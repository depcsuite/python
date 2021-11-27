from Clases.Conexion import Conexion
#### DEBE ACLARARSE A LOS ALUMNOS QUE LOS SISTEMAS REALES UTILIZAN CONTRASEÑAS
# ENCRIPTADAS
# PUEDE PRESENTÁRSELE A ELLOS EL PAQUETE FERNET PARA REALIZARLO
#
class Usuario:
    __id =  None
    __nombreU = None
    __passU = None
    __autorizados = [(1,"luka","pass"),(2,"cristian","mitas")]
    def __init__(self, id=None, nom=None, passw=None):

        self.__id = id
        self.__nombreU = nom
        self.__passU = passw
    def getNombre(self):
        return self.__nombreU
    def setNombre(self, n):
        self.__nombreU = n
    @staticmethod
    def validar(usuario, passw):
        con = Conexion()
        con.conectar()
        query = "SELECT * FROM usuario WHERE nombre = '"+usuario+"' AND passw = '"+passw+"'"
        cur = con.c()
        cur.execute(query)
        r = cur.fetchall()
        con.desconectar()
        if(len(r) == 0):
            return False
        else:
            for resultado in r:
                idUs = resultado[0]
                nombreUs = resultado[1]
            return idUs, nombreUs
        
        