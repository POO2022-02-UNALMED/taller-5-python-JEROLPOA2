from zooAnimales.animal import Animal

class Ave(Animal):

    _listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):

        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)
    
    def cantidadAves():
        return len(Ave._listado)

    def movimiento():
        return "volar"

    def crearHalcon(nombre, edad, genero):
        
        Ave.halcones += 1
        halcon = Ave(nombre,edad,"montanas", genero,"cafe glorioso")
    
    def crearAguila(nombre, edad, genero):
        
        Ave.aguilas += 1
        aguila = Ave(nombre,edad,"montanas", genero,"blanco y amarillo")

    
    def getColorPlumas(self):
        return self._colorPlumas
    
    def getListado(self):
        return self._listado
    
    def setColorPlumas(self,colorPlumas):
        self._colorPlumas = colorPlumas
    
    def setListado(self,listado):
        self._listado = listado