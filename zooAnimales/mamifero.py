from zooAnimales.animal import Animal

class Mamifero(Animal):

    _listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre = "", edad = 0, habitat = "", genero = "", zona = None, pelaje = False, patas = 0):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._pelaje = pelaje
        self._patas = patas

        self._listado.append(self)

    @staticmethod

    def cantidadMamiferos(cls):
        return len(cls._listado)
    
    @staticmethod

    def crearCaballo(cls, nombre, edad, genero):

        caballo = Mamifero(nombre, edad, "pradera", genero, True, 4)
        cls.caballos += 1
        return caballo
    
    @staticmethod

    def crearLeon(cls, nombre, edad, genero):

        leon = Mamifero(nombre, edad, "selva", genero, True, 4)
        cls.leones += 1
        return leon
    
    def getPelaje(self):
        return self._pelaje
    
    def isPelaje(self):
        return self._pelaje
    
    def getPatas(self):
        return self._patas
    
