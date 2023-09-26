from zooAnimales.animal import Animal

class Anfibio(Animal):

    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre = "", edad = 0, habitat = "", genero = "", colorPiel = "", venenoso = False):

        super().__init__(nombre, edad, habitat, genero)

        self._colorPiel = colorPiel
        self._venenoso = venenoso

        self._listado.append(self)

    @classmethod

    def cantidadAnfibios(cls):
        return len(cls._listado)
    
    def movimiento():
        return "saltar"
    
    @staticmethod

    def crearRana(cls, nombre, edad, genero):
        rana = Anfibio(nombre, edad, "selva", genero, "rojo", False)
        cls.ranas += 1
        return rana
    
    @staticmethod
    
    def crearSalamandra(cls, nombre, edad, genero):
        salamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        cls.salamandras += 1
        return salamandra
    
    def getColorPiel(self):
        return self._colorPiel
    
    def getVenenoso(self):
        return self._venenoso
    
    def isVenenoso(self):
        return self._venenoso
    

    



