class Vehiculo:
    _color = None #protected
    _puertas = None
    _tamanio = None
    _velMaxima = None
    _motor = None

    def __init__(self, col, puer, tamanio, velMax, motor):
        self._color = col
        self._puertas = puer
        self._tamanio = tamanio
        self._velMaxima = velMax
        self._motor = motor


    def getColor(self):
        return self._color

    def setColor(self,color):
        self._color = color
        
    def getPuertas(self):
        return self._puertas

    def setPuertas(self,puertas):
        self._puertas = puertas

    def getTamanio(self):
        return self._tamanio

    def setTamanio(self, tamanio):
        self._tamanio = tamanio

    def getVelMax(self):
        return self._velMaxima

    def setVelMax(self,velMax):
        self._velMaxima = velMax
    def getMotor(self):
        return self._motor
    def arrancar(self):
        return "Vehículo arrancando..."
    def __str__(self):
        return "Color: " + self._color + " | Tamaño: " + self._tamanio + " | V max:  " + str(self._velMaxima)
    

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


