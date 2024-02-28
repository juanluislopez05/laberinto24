class Game:
    def __init__(self):
        self.maze = None

    def create_wall(self):
        return Wall()
    
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
    def activarBombas(self):
        def activar_si_bomba(elemento):
            if elemento.esBomba():
                elemento.activar()

        self.laberinto.recorrer(activar_si_bomba)

class BombedGame(Game):
    def create_wall(self):
        return BombedWall()

class MapElement:
    def __init__(self):
        pass
    def entrar(self):
        pass
    def recorrer (self):
        pass 


class Hoja(MapElement):
    def accept(self, visitor):
        visitor.visit_hoja(self)
    def recorrer(self, unBloque):
        unBloque.value = self

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


class Decorator(Hoja):
    def __init__(self, component):
        self.component = component

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



class Room(Contenedor):
    def __init__(self,id):
        self.north = None
        self.east = None
        self.west = None
        self.south = None
        self.id = id
    
    def entrar(self):
        print("You enter room", self.id)

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
        
class Bicho:

    def __init__(self, modo, vidas, poder, posicion):
        self.modo = modo 
        self.vidas = vidas
        self.poder = poder 
        self.posicion = posicion
class Modo:

  def caminar(self, bicho):
    
    
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

game= Game()
game.make2RoomsMaze()
game.maze.entrar()

game=Game()
game.make2RoomsMazeFM() 
    
game=BombedGame()
game.make2RoomsMazeFM()
game.maze.entrar() 