class Anfibio(Animal):

    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):

        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)
    
    def cantidadAnfibios():

        return len(Anfibio._listado)

    def movimiento():
        return "saltar"

    def crearRana(nombre, edad, genero):
        
        Anfibio.ranas += 1
        rana = Anfibio(nombre,edad,"selva", genero,"rojo", True)
    
    def crearSalamandra(nombre, edad, genero):
        
        Anfibio.salamandras += 1
        salamandra = Anfibio(nombre,edad,"selva", genero,"negro y amarillo", False)

    
    def getColorPiel(self):
        return self._colorPiel
    
    def getVenenoso(self):
        return self._venenoso
    
    def getListado(self):
        return self._listado
    
    def setColorPiel(self,colorPiel):
        self._colorPiel = colorPiel
    
    def setVenenoso(self,venenoso):
        self._venenoso= venenoso
    
    def setListado(self,listado):
        self._listado = listado
    