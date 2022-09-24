class Zoologico:

    def __init__(self, nombre, ubicacion):
        
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []
    
    def agregarZonas(self,zona):

        self._zonas.append(zona)
    
    def cantidadTotalAnimales(self):

        ca = 0

        for i in self._zonas:

            ca += i.cantidadAimales()
        
        return ca
    
    
    def getNombre(self):
        return self._nombre
    
    def getUbicacion(self):
        return self._ubicacion
    
    def getZonas(self):
        return self._zonas

    def setNombre(self, nombre):
        self._nombre = nombre
    
    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion
    
    def setZonas(self, zonas):
        self._zonas = zonas


