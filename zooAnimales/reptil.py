from zooAnimales.animal import Animal

class Reptil(Animal):

    _listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):

        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)
    
    def cantidadReptiles():

        return len(Reptil._listado)

    def crearIguana(nombre, edad, genero):
        
        Reptil.iguanas += 1
        iguana = Reptil(nombre,edad,"pradera", genero, True, 4)
    
    def crearSerpiente(nombre, edad, genero):
        
        Reptil.serpientes += 1
        serpiente = Reptil(nombre,edad,"selva", genero, True, 4)

    
    def getColorEscamas(self):
        return self._colorEscamas
    
    def getLargoCola(self):
        return self._largoCola
    
    def getListado(self):
        return self._listado
    
    def setColorEscamas(self,colorEscamas):
        self._colorEscamas = colorEscamas
    
    def setLargoCola(self,largoCola):
        self._largoCola = largoCola
    
    def setListado(self,listado):
        self._listado = listado