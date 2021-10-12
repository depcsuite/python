from Vehiculo import Vehiculo
class Auto(Vehiculo):
    __marca = None
    __modelo = None

    def __init__(self, col, puer, tamanio, velMax, motor, marca, modelo):
        Vehiculo.__init__(self,col,puer,tamanio,velMax,motor)
        self.__marca = marca
        self.__modelo = modelo
    def arrancar(self):
        return("Auto arrancando...")

#primerAuto = Auto("Rojo", 4, "Grande", 120, 80)
#segundoAuto = Auto("Azul",2,"Chico",240,200)
#print(primerAuto.getColor())

#primerAuto.setColor("Amarillo")

#print(primerAuto.getColor())

#print("El segundo auto tiene como velocidad máxima:" , segundoAuto.getVelMax())
#print("El segundo auto es de tamaño:" , segundoAuto.getTamanio())
#nuevoTam = input("Ingrese un nuevo tamanio...")
#segundoAuto.setTamanio(nuevoTam)
#print("El segundo auto es ahora de tamaño:" , segundoAuto.getTamanio())


