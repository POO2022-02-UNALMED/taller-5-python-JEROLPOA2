class Animal:

    _totalAnimales = 0
    _zona = None

    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero

    def movimiento():
        return "desplazarse"
    
    def totalPorTipo():
        return "Mamiferos: " + Mamifero.cantidadMamiferos() + "\n" + "Aves: " + Ave.cantidadAves() + "\n" + "Reptiles: " + Reptil.cantidadReptiles() + "\n" + "Peces: " + Pez.cantidadPeces() + "\n" + "Anfibios: " + Anfibio.cantidadAnfibios()

    def toString(self):
        
        if(self._zona != None):
            return "Mi nombre es " + self._nombre + ", tengo una edad de " + self._edad +", habito en " + self._habitat + " y mi genero es " + self._genero + ", la zona en la que me ubico es " + self._zona + ", en el " + self._zona.getZoo()
        
        
        else:
            return "Mi nombre es " + self._nombre + ", tengo una edad de " + self._edad +", habito en " + self._habitat + " y mi genero es " + self._genero
    
    
    def getNombre(self):
        return self._nombre
    
    def getEdad(self):
        return self._edad
    
    def getHabitat(self):
        return self._habitat
    
    def getGenero(self):
        return self._genero
    
    def getZona(self):
        return self._zona
    
    def setNombre(self,nombre):
        self._nombre = nombre
    
    def setEdad(self,edad):
        self._edad = edad
    
    def setHabitat(self,habitat):
        self._habitat = habitat
    
    def setGenero(self,genero):
        self._genero = genero
    
    def setZona(self,zona):
        self._zona = zona
    