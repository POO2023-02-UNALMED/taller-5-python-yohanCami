from gestion.zona import Zona

class Zoologico:

    def __init__(self, nombre = "", ubicacion = "", zonas = None):

        self._nombre = nombre
        self._ubicacion = ubicacion
        if zonas == None:
            self._zonas = []
        else:
            self._zonas = zonas

    def agregarZonas(self, zona):
        self._zonas.append(zona) 

    def cantudadTotalAnimales(self):

        contador = 0
        for i in range(len(self._zonas)):

            zona = self.zonas[i]
            contador += zona.cantidadAnimales()
        
        return contador
    
    def getNombre(self):
        return self._nombre
    
    def getUbicacion(self):
        return self._ubicacion
    
    def getZona(self):
        return self._zonas