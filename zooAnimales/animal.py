class Animal:

    _totalAnimales = 0
    def __init__(self, nombre = "", edad = 0, habitat = "", genero = "", zona = None):

        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        
        self._totalAnimales += 1

    def movimiento():
        return "desplazarse"
    
    @staticmethod

    def totalPorTipo(cls):

        from zooAnimales.mamifero import Mamifero 
        from zooAnimales.ave import Ave
        from zooAnimales.reptil import Reptil
        from zooAnimales.pez import Pez
        from zooAnimales.anfibio import Anfibio

        return ("Mamiferos: " + Mamifero.cantidadMamiferos() + "\n"+
				"Aves: " + Ave.cantidadAves()+ "\n" +
				"Reptiles: " + Reptil.cantidadReptiles() + "\n" +
				"Peces: " + Pez.cantidadPeces() + "\n" +
				"Anfibios: " + Anfibio.cantidadAnfibios())
    
    def __str__(self):

        if (self._zona != None):

            return "Mi nombre es " + self._nombre + ", tengo una edad de " + self._edad + " habito en " + self._habitat + "y mi genero es " + self._genero + ", la zona en la que me ubico es" + self._zona.getNombre() + ", en el zoo" + self._zona.getZoo()
        
        else:
            return "Mi nombre es " + self._nombre + ", tengo una edad de " + self._edad + ", habito en " + self._habitat + " y mi genero es " + self._genero

    def getNombre(self):
        return self._nombre
    
    def getEdad(self):
        return self._edad
    
    def getHabitat(self):
        return self._habitat
    
    def getGenero(self):
        return self._genero
    