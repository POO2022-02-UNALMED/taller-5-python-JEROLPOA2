from zooAnimales.animal import Animal

class Pez(Animal):

    _listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):

        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)

    def movimiento():
        return "nadar"
    
    def cantidadPeces():

        return len(Pez._listado)

    def crearSalmon(nombre, edad, genero):
        
        Pez.salmones += 1
        salmon = Pez(nombre,edad,"oceano", genero,"rojo",6)
    
    def crearBacalao(nombre, edad, genero):
        
        Pez.bacalaos += 1
        bacalao = Pez(nombre,edad,"oceano", genero,"blanco",6)

    
    def getcolorEscamas(self):
        return self._colorEscamas
    
    def getcantidadAletas(self):
        return self._cantidadAletas
    
    def getListado(self):
        return self._listado
    
    def setcolorEscamas(self,colorEscamas):
        self._colorEscamas = colorEscamas
    
    def setcantidadAletas(self,cantidadAletas):
        self._cantidadAletas = cantidadAletas
    
    def setListado(self,listado):
        self._listado = listado