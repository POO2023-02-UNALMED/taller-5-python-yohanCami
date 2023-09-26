from zooAnimales.animal import Animal

class Reptil(Animal):

    _listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre = "", edad = 0, habitat = "", genero = "", zona = None,  colorEscamas = "", largoCola = 0):
        super().__init__(nombre, edad, habitat, genero, zona)

        self._colorEscamas = colorEscamas
        self._largoCola = largoCola

        self._listado.append(self)

    @staticmethod

    def cantidadReptiles(cls):
        return len(cls._listado)
    
    def movimiento():
        return "reptar"
    
    @staticmethod

    def crearIguana(cls, nombre, edad, genero):
        iguana = Reptil(nombre, edad, "humedal", genero, "verde", 3)
        cls.iguanas += 1
        return iguana
    
    @staticmethod

    def crearSerpiente(cls, nombre, edad, genero):
        serpiente = Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        cls.serpientes += 1
        return serpiente
    
    def getColorEscamas(self):
        return self._colorEscamas
    
    def getLargoCola(self):
        return self._largoCola
    