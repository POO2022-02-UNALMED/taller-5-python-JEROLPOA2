class Zona():
    
    def __init__(self, nombre, *args):
        self._nombre = nombre
        
        if args != None:
            for i in args:
                self._zoo = i 
        else:
            self._zoo = None
        self._animales = []
        pass

    def agregarAnimales(self,animal):
        self._animales.append(animal)

    def cantidadAnimales(self):

        return len(self._animales)

    
    def getNombre(self):
        return self._nombre
    
    def getZoo(self):
        return self._zoo
    
    def getAnimales(self):
        return self._animales

    def setNombre(self, nombre):
        self._nombre = nombre
    
    def setZoo(self, zoo):
        self._zoo = zoo
    
    def setAnimales(self, animales):
        self._animales = animales
