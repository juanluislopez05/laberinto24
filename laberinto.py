import random
import time 
class MapElement:
    def __init__(self):
        pass
    def abrirPuertas(self):
        pass
    def cerrarPuertas(self):
        pass
    def entrar(self, alguien):
        pass
    def recorrer (self):
        pass 
    def esBomba (self):
        return False
    def esHabitacion (self):
        return False
    def esPared (self):
        return True
    def esPuerta (self):
        return False
    
class Contenedor(MapElement):
    def __init__(self):
        super().__init__()
        self.hijos = []
        self.orientaciones=[]
    def print(self):
        print("Contenedor")

    def agregarHijo(self, hijo):
        self.hijos.append(hijo)
        
    def eliminarHijo(self, hijo):
        self.hijos.remove(hijo)

    def agregarOrientacion(self, orientacion):
        self.orientaciones.append(orientacion)
    
    def removeOrientation(self, orientation):
        self.orientaciones.remove(orientation)

    def obtenerOrientacionAleatoria(self):
        return random.choice(self.orientaciones)

    def caminarAleatorio(self,alguien):
        pass
        
    def recorrer(self, unBloque):
        unBloque.value = self 
        for each in self.hijos:
            each.recorrer(unBloque)
            
    def irANorte(self, alguien):
        self.norte.entrar(alguien)

    def irAEste(self, alguien):
        self.este.entrar(alguien)

    def irASur(self, alguien):
        self.sur.entrar(alguien)

    def irAOeste(self, alguien):
        self.oeste.entrar(alguien)
        
    def ponerEnOrientacionElemento(self, unaOrientacion, unEM):
        if unaOrientacion == Norte():
            self.norte = unEM
        elif unaOrientacion == Sur():
            self.sur = unEM
        elif unaOrientacion == Este():
            self.este = unEM
        elif unaOrientacion == Oeste():
            self.oeste = unEM
        else:
            print("Orientación desconocida")
class Armario(Contenedor):
    def __init__(self, id):
        super().__init__()


class Room(Contenedor):
    def __init__(self, id):
        super().__init__()
        self.north = None
        self.east = None
        self.west = None
        self.south = None
        self.id = id


    
    def entrar(self,alguien):
        print(alguien + " ha entrado en la hab ", self.id)
    
    def print(self):
        print("Room")

    def esHabitacion(self):
        return True
        


class Maze(Contenedor):
    def __init__(self):
        super().__init__()
    
    def addRoom(self, room):
        self.agregarHijo(room)

  #  def agregarHijo(self, hijo):
  #      self.hijos.append(hijo)

 #   def eliminarHijo(self, hijo):
  #      self.hijos.remove(hijo)
    
    def entrar(self,alguien):
        self.hijos[0].entrar(alguien)
    
    def print(self):
        print("Laberinto")   

    def numeroHabitaciones(self):
        return len(self.rooms)
        
    def obtenerHabitacion(self, id):
        for hab in self.hijos:
            if hab.id == id:
                return hab
        return None
    
class Hoja(MapElement):
    def __init__(self):
        super().__init__()

    def print(self):
        print("Hoja")

    def recorrer(self, unBloque):
        unBloque.value = self
class Decorator(Hoja):
    def __init__(self):
        super().__init__()
        self.component = None 
    def print(self):
        print("Decorador")

class Bomba(Decorator):

    def __init__(self):
        super().__init__()
        self.activa = False

    def activar(self):
        self.activa = True

    def print(self):
        print("Bomba")

    def desactivar(self):
        self.activa = False

    def esBomba(self):
        return True

    def entrar(self, alguien):
        
        print(alguien + " ha pisado una bomba")

  
class Wall(MapElement):
    def __init__(self):
        pass # Walls don't need additional attributes
    def entrar(self, alguien):
        print(alguien + " se ha chocado con una pared")
    def esPared(self):
        return True
    def recorrer(self, unBloque):
        unBloque.value = self

class BombedWall(Wall):
    def __init__(self):
        super().__init__()
        self.active = False   

    def print(self):
        print("BombedWall")

    def entrar(self, alguien):
        if self.active:
            print(alguien + " ha hecho que la bomba explote")
        else:
            return super().entrar()
class Door(MapElement):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
        self.opened = False
        
    def esPuerta(self):
        return True
    
    def print(self):
        print("Puerta")
    
    def entrar(self, alguien):
        if self.opened:
            self.side2.entrar()
        else:
            print("The door is locked")
            
    def abrirPuertas(self):
        self.opened = True
        print("La puerta " + str(self) + " está abierta")
            
    def cerrarPuertas(self):
        self.opened = False
        print("La puerta " + str(self) + " está cerrada")
            
    def recorrer(self, unBloque):
        unBloque.value = self



class Orientacion:
    def __init__(self):
        pass
    def poner_elemento(self, un_em, un_contenedor):
        pass
    def caminar(self, alguien):
        pass


class Este(Orientacion):

    _instance = None
    def __init__(self):
        if not Este._instance:
            super().__init__()
            Este._instance = self
    def get_instance(cls):
        if not cls._instance:
            cls._instance = Este()
        return cls._instance

    def print(self):
        print("Este")

    def caminar(self, alguien):
        alguien.irAEste(self)
    
    def poner_elemento(self, un_em, un_contenedor):
        un_contenedor.este = un_em
    
    def recorrer(self, unBloque, unContenedor):
        unContenedor.este.recorrer(unBloque)

class Norte(Orientacion):
    _instance = None
    def __init__(self):
        if not Norte._instance:
            super().__init__()
            Norte._instance = self
    
    def poner_elemento(self, un_em, un_contenedor):
        un_contenedor.norte = un_em
        
    def get_instance(cls):
        if not cls._instance:
            cls._instance = Norte()
        return cls._instance

    def print(self):
        print("Norte")
    
    def caminar(self, alguien):
        alguien.irANorte(self)
        
    def recorrer(self, unBloque, unContenedor):
        unContenedor.norte.recorrer(unBloque)
        
class Oeste(Orientacion):
    _instance = None
    def __init__(self):
        if not Oeste._instance:
            super().__init__()
            Oeste._instance = self
    def get_instance(cls):
        if not cls._instance:
            cls._instance = Oeste()
        return cls._instance

    def poner_elemento(self, un_em, un_contenedor):
        un_contenedor.oeste = un_em

    def print(self):
        print("Oeste")

    def caminar(self, alguien):
        alguien.irAOeste(self)

    def recorrer(self, unBloque, unContenedor):
        unContenedor.oeste.recorrer(unBloque)
        
class Sur(Orientacion):
    _instance = None
    def __init__(self):
        if not Sur._instance:
            super().__init__()
            Sur._instance = self
    def get_instance(cls):
        if not cls._instance:
            cls._instance = Sur()
        return cls._instance

    def poner_elemento(self, un_em, un_contenedor):
        un_contenedor.sur = un_em

    def print(self):
        print("Sur")

    def recorrer(self, unBloque, unContenedor):
        unContenedor.sur.recorrer(unBloque)
    def caminar(self, alguien):
        alguien.irASur(self)



