class Mamifero(Animal):

    _listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):

        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)
    
    def cantidadMamiferos():

        return len(Mamifero._listado)

    def crearCaballo(nombre, edad, genero):
        
        Mamifero.caballos += 1
        caballo = Mamifero(nombre,edad,"pradera", genero, True, 4)
    
    def crearLeon(nombre, edad, genero):
        
        Mamifero.leones += 1
        leon = Mamifero(nombre,edad,"selva", genero, True, 4)

    
    def getPelaje(self):
        return self._pelaje
    
    def getPatas(self):
        return self._patas
    
    def getListado(self):
        return self._listado
    
    def setPelaje(self,pelaje):
        self._pelaje = pelaje
    
    def setPatas(self,patas):
        self._patas = patas
    
    def setListado(self,listado):
        self._listado = listado