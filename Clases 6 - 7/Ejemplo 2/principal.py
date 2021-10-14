class Animal:
	_peso = None
	_color = None
	def __init__(self, p,c):
		self._peso = p
		self._color = c
	
	def nacer(self):
		return "Animal naciendo.."

	#Aquí van setters y getters….

class Perro(Animal):
    __raza = None
    __nombre = None
    __duenio = None
    def __init__(self, n,d, r, p,c):
        self.__raza = r
        self._nombre = n
        self._duenio = d
        Animal.__init__(self, p, c) #Envía peso y color al constructor
		# de Animal
    def nacer(self):
        return ("Perronaciendo")

	#Aquí van setters y getters….
class Caracol(Animal):
    __tipoCaparazon = None
    def __init__(self,p,c, cap):
        self.__tipoCaparazon = cap
        Animal.__init__(self, p, c)

    def nacer(self):
        return Animal.nacer(self)
        #return ("caracol naciendo")
	#Aquí van setters y getters….
unPerro = Perro("Olaf", "Luca", "Pastor", 20, "Marrón")
print(unPerro.nacer())
#Imprime a través del método de la clase padre, “nacer()”

unCaracol = Caracol(100, "gris","Dura")
print(unCaracol.nacer())
