class MapElement:
    def __init__(self, padre):
        self.padre=padre
    def entrar(self):
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
        self.hijos = []
        
    def agregarHijo(self, hijo):
        self.hijos.append(hijo)
        
    def eliminarHijo(self, hijo):
        self.hijos.remove(hijo)
        
    def recorrer(self, unBloque):
        unBloque.value = self 
        for each in self.hijos:
            each.recorrer(unBloque)
class Room(Contenedor):
    def __init__(self, id):
        self.north = None
        self.east = None
        self.west = None
        self.south = None
        self.id = id
        self.hijos = []


    
    def entrar(self):
        print("You enter room", self.id)
    def esHabitacion(self):
        return True
        
    def ponerEn(self, unaOrientacion, unEM):
        if unaOrientacion == Norte():
            self.north = unEM
        elif unaOrientacion == Este():
            self.east = unEM
        elif unaOrientacion == Oeste():
            self.west = unEM
        elif unaOrientacion == Sur():
            self.south = unEM
        else:
            print("Orientación inválida")

class Maze(Contenedor):
    def __init__(self):
        self.rooms = []
    
    def addRoom(self, room):
        self.rooms.append(room)

  #  def agregarHijo(self, hijo):
  #      self.hijos.append(hijo)

 #   def eliminarHijo(self, hijo):
  #      self.hijos.remove(hijo)
    
    def entrar(self):
        self.rooms[0].entrar()
        
    def numeroHabitaciones(self):
        return len(self.rooms)
        
    def obtenerHabitacion(self, unNum):
    	return self.rooms[unNum]
    
class Hoja(MapElement):
    def accept(self, visitor):
        visitor.visit_hoja(self)
    def recorrer(self, unBloque):
        unBloque.value = self
class Decorator(Hoja):
    def __init__(self, component):
        self.component = component

class Bomba(Decorator):

  def __init__(self, component):
    super().__init__(component)
    self.activa = False

  def activar(self):
    self.activa = True

  def desactivar(self):
    self.activa = False

  def esBomba(self):
    return True

  def entrar(self):
    if self.activa:
      print("La bomba ha explotado!")
    else:
      # em puede ser None
      if self.component:
        self.component.entrar()

  
class Wall(MapElement):
    def __init__(self):
        pass # Walls don't need additional attributes
    def entrar(self):
        print("You can't go through walls")

class BombedWall(Wall):
    def __init__(self):
        self.active = False   
    def entrar(self):
        if self.active:
            print("the bomb has detonated")
        else:
            return super().entrar()
class Door(MapElement):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
        self.opened = False
        
    def esPuerta(self):
        return True
    
    def entrar(self):
        if self.opened:
            self.side2.entrar()
        else:
            print("The door is locked")
class Bicho:

    def __init__(self):
        self.modo = None
        self.vidas = None
        self.poder = None
        self.posicion = None
        
    def actua(self):
        self.modo.actua(self)
class Modo:

  def caminar(self, bicho):

    # definir un comportamiento por defecto
    pass

    # dada la posicion del bicho, obtener las orientaciones, 
    # eligir una, caminar en esa direccion
    posicion_actual = bicho.posicion
    
    # Obtener orientaciones posibles
    orientaciones = [norte, sur, este, oeste]
    
    # Elegir orientación al azar 
    import random
    orientacion = random.choice(orientaciones)
    
    # Caminar en esa orientación
    if orientacion == norte:
      bicho.posicion[1] += 1 
    elif orientacion == sur:
      bicho.posicion[1] -= 1
    # y así con este y oeste
      
    print(f"El bicho camina hacia {orientacion}")

  def actua(self, bicho):
    self.caminar(bicho)

class Agresivo(Modo):
  pass

class Perezoso(Modo):
  pass

class Orientacion:

    def poner_elemento(self, un_em, un_contenedor):
        pass

class Este(Orientacion):

    def poner_elemento(self, un_em, un_contenedor):
        un_contenedor.este = un_em

class Norte(Orientacion):
    
    def poner_elemento(self, un_em, un_contenedor):
        un_contenedor.norte = un_em

class Oeste(Orientacion):

    def poner_elemento(self, un_em, un_contenedor):
        un_contenedor.oeste = un_em

class Sur(Orientacion):

    def poner_elemento(self, un_em, un_contenedor):
        un_contenedor.sur = un_em
class Game:
    def __init__(self):
        self.maze = None
        self.bichos = []
        
    def activarBombas(self):
        def activar_si_bomba(elemento):
            if elemento.esBomba():
                elemento.activar()

        self.laberinto.recorrer(activar_si_bomba)

    def create_wall(self):
        return Wall()
    
    def agregarBicho(self, unBicho):
        self.bichos.append(unBicho)

    def eliminarBicho(self, unBicho):
        if unBicho in self.bichos:
            self.bichos.remove(unBicho)
        else:
            print('No existe ese bicho')
            
    def desactivarBombas(self):
        self.laberinto.recorrer(lambda elemento: elemento.desactivar() if elemento.esBomba() else None)

    def fabricarBichoAgresivo(self, unaHab):
        bicho = Bicho()
        bicho.modo = Agresivo()
        bicho.vidas = 5
        bicho.poder = 2
        bicho.posicion = unaHab
        return bicho
    def fabricarBichoPerezoso(self, unaHab):
        bicho = Bicho()
        bicho.modo = Perezoso()
        bicho.vidas = 2
        bicho.poder = 0
        bicho.posicion = unaHab
        return bicho


    def fabricarHabitacion(self, unNum):
        hab = Room()
        hab.num = unNum
        hab.ponerEn(Norte(), self.create_wall())
        hab.ponerEn(Este(), self.create_door())
        hab.ponerEn(Sur(), self.create_door())
        hab.ponerEn(Oeste(), self.create_wall())
        return hab
    
    def create_door(self,side1,side2):
        door=Door(side1,side2)
        return door  
    
    def create_room(self, id):
        room=Room(id)
        room.north=self.create_wall()
        room.south=self.create_wall()
        room.east=self.create_wall()
        room.west=self.create_wall()
        return room

    def create_maze(self):
        return Maze()
    def create_bomb(self):
        return Bomba(None)
        
    def obtenerHabitacion(self, unNum):
        return self.laberinto.obtenerHabitacion(unNum)
        
    def fabricarPuertaLado1(unaHab1, unaHab2):
        puerta = Door(unaHab1, unaHab2)
        puerta.side1=unaHab1
        puerta.side2=unaHab2
        return puerta


    def make2RoomsMazeFM(self):
        self.maze = self.create_maze()
        room1 = self.create_room(1)
        room2 = self.create_room(2)
        door = self.create_door(room1,room2)
        room1.south=door
        room2.north=door
        self.maze.addRoom(room1)
        self.maze.addRoom(room2)
        return self.maze
    
    def make2RoomsMaze(self):
        self.maze = Maze()
        room1 = Room(1)
        room2 = Room(2)
        self.maze.addRoom(room1)
        self.maze.addRoom(room2)

        door=Door(room1,room2)
        room1.south = door
        room2.north = door
        return self.maze
        
    def fabricarLaberinto2Habitaciones2BombasFM(self):
    #fabrica un laberinto con 2 habitaciones. La hab1 tiene al sur la hab 2 unidas por una puerta"
        self.maze = self.create_maze()
        hab1 = self.create_room(1) # Habitacion new num:1  
        hab2 = self.create_room(2)
        puerta = self.create_door(hab1,hab2) # self fabricarPuertaLado1:hab1 lado2:hab2  
        hab1.south = puerta
        hab2.north = puerta

        puerta.side1=hab1
        puerta.side2=hab2

        bm1 = self.create_bomb()
        bm2 = self.create_bomb()

        hab1.agregarHijo(bm1)
        hab2.agregarHijo(bm2)
        self.laberinto = self.create_maze()
        self.laberinto.addRoom(hab1)
        self.laberinto.addRoom(hab2)
    def fabricarLaberinto4Habitaciones4BichosFM(self):
        hab1 = self.create_room(1)
        hab2 = self.create_room(2) 
        hab3 = self.create_room(3)
        hab4 = self.create_room(4)
        
        p12 = self.create_door(hab1,hab2)
        p13 = self.create_door(hab1,hab3)
        p34 = self.create_door(hab3, hab4) 
        p24 = self.create_door(hab2, hab4)

        p12.side1 = hab1
        p12.side2 = hab2
        
        p13.side1 = hab1 
        p13.side2 = hab3
        
        p24.side1 = hab2
        p24.side2 = hab4
        
        p34.side1 = hab3
        p34.side2 = hab4

        hab1.south = p12
        hab2.north = p12
            
        hab1.east = p13
        hab3.west = p13
        
        hab2.west = p24
        hab4.east = p24
        
        hab3.south = p34 
        hab4.north = p34
        
        self.laberinto = self.create_maze()
        self.laberinto.addRoom(hab1)
        self.laberinto.addRoom(hab2)
        self.laberinto.addRoom(hab3)
        self.laberinto.addRoom(hab4)

        self.agregarBicho(self.fabricarBichoAgresivo(hab1))
        self.agregarBicho(self.fabricarBichoAgresivo(hab3))

        self.agregarBicho(self.fabricarBichoPerezoso(hab2))
        self.agregarBicho(self.fabricarBichoPerezoso(hab4))



class BombedGame(Game):
    def create_wall(self):
        return BombedWall()





game= Game()
game.make2RoomsMaze()
game.maze.entrar()

game=Game()
game.make2RoomsMazeFM() 
    
game=BombedGame()
game.make2RoomsMazeFM()
game.maze.entrar() 

game=BombedGame()
game.fabricarLaberinto2Habitaciones2BombasFM()

game= Game()
game.fabricarLaberinto4Habitaciones4BichosFM()