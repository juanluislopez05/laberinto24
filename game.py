from laberinto import Maze, Room, Door, Wall, BombedWall, Bomba, Norte, Este, Sur, Oeste
from DirectorHilos import DirectorHilos
from bicho import Bicho, Modo, Agresivo, Perezoso

class Game:
    def __init__(self):
        self.maze = None
        self.bichos = []
        self.directorHilos = DirectorHilos()
    
    def lanzarHilos(self):
        for bicho in self.bichos:
            self.directorHilos.añadirHilo(bicho)
        self.directorHilos.start()
    
    def pararHilos(self):
        self.directorHilos.stop()
        self.directorHilos.join()
        
    def activarBombas(self):
        def activar_si_bomba(elemento):
            if elemento.esBomba():
                elemento.activar()

        self.laberinto.recorrer(activar_si_bomba)

    def create_wall(self):
        return Wall()
    
    def agregarBicho(self, unBicho):
        self.bichos.append(unBicho)
       # unBicho.num=len(self.bichos)+1

    def eliminarBicho(self, unBicho):
        if unBicho in self.bichos:
            self.bichos.remove(unBicho)
        else:
            print('No existe ese bicho')
            
    def desactivarBombas(self):
        self.laberinto.recorrer(lambda elemento: elemento.desactivar() if elemento.esBomba() else None)

    def fabricarBichoAgresivo(self, unaHab):
        bicho = Bicho(Agresivo())
        bicho.poder = 6
        bicho.posicion = unaHab
        return bicho
    def fabricarBichoPerezoso(self, unaHab):
        bicho = Bicho(Perezoso())
        bicho.poder = 2
        bicho.posicion = unaHab
        return bicho
    def print(self):
        print("Game")


    def fabricarHabitacion(self, unNum):
        hab = Room(unNum)
        hab.agregarOrientacion(self.fabricarNorte())
        hab.agregarOrientacion(self.fabricarEste())
        hab.agregarOrientacion(self.fabricarSur())
        hab.agregarOrientacion(self.fabricarOeste())
        hab.norte=self.create_door()
        hab.este=self.create_door()
        hab.sur=self.create_door()
        hab.oeste=self.create_door()
        return hab
    
    def fabricarNorte(self):
        return Norte().get_instance()

    def fabricarEste(self):
        return Este.get_instance()
    
    def fabricarSur(self):
        return Sur().get_instance()
    
    def fabricarOeste(self):
        return Oeste().get_instance()

    
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
        maze = Maze()
        self.maze = maze
        room1 = Room(1)
        room2 = Room(2)
        self.maze.addRoom(room1)
        self.maze.addRoom(room2)

        door=Door(room1,room2)
        room1.south = door
        room2.north = door
        
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
        
        maze = Maze()
        
        self.laberinto = self.create_maze()
        self.laberinto.addRoom(hab1)
        self.laberinto.addRoom(hab2)
        self.laberinto.addRoom(hab3)
        self.laberinto.addRoom(hab4)

        self.maze = maze
        
        bicho1=self.fabricarBichoAgresivo(hab1)
        bicho2=self.fabricarBichoAgresivo(hab3)

        bicho3=self.fabricarBichoPerezoso(hab2)
        bicho4=self.fabricarBichoPerezoso(hab4)

        self.agregarBicho(bicho1)
        self.agregarBicho(bicho2)
        self.agregarBicho(bicho3)
        self.agregarBicho(bicho4)

        return maze



class BombedGame(Game):
    def create_wall(self):
        return BombedWall()
    def print(self):
        print("JuegoBomba")





# game= Game()
# game.make2RoomsMaze()
# game.maze.entrar()

# game=Game()
# game.make2RoomsMazeFM() 
    
# game=BombedGame()
# game.make2RoomsMazeFM()
# game.maze.entrar() 

# game=BombedGame()
# game.fabricarLaberinto2Habitaciones2BombasFM()

# game= Game()
# game.fabricarLaberinto4Habitaciones4BichosFM()