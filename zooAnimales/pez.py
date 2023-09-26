from zooAnimales.animal import Animal

class Pez(Animal):

    _listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre = "", edad = 0, habitat = "", genero = "", colorEscamas = "", cantidadAletas = 0):

        super().__init__(nombre, edad, habitat, genero)

        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas

        self._listado.append(self)

    
    @classmethod

    def cantidadPeces(cls):
        return len(cls._listado)
    
    def movimiento():
        return "nadar"
    
    @classmethod

    def crearSalmon(cls, nombre, edad, genero):
        salmon = Pez(nombre, edad, "oceano", genero, "rojo", 6)
        cls.salmones += 1
        return salmon
    
    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        bacalao = Pez(nombre, edad, "oceano", genero, "gris", 6)
        cls.bacalaos += 1
        return bacalao
    
    def getColorEscamas(self):
        return self._colorEscamas
    
    def getCantidadAletas(self):
        return self._cantidadAletas
    
    