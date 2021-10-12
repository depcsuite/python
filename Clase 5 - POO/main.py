from Auto import Auto
from Motor import Motor
from Tractor import Tractor
motorDeAuto = Motor(200,8,2000,"Nafta")
bmw = Auto("Negro",2,"Chico",250, motorDeAuto, "BMW","Serie 3")
unTractor = Tractor()
print("Creado un auto de color: ", bmw.getColor())
print("El motor de este auto tiene un motor a: ", bmw.getMotor().getTipoCombustible())
print(bmw.arrancar())
print(bmw)
#print("Tractor arrancando..." , unTractor.arrancar())
