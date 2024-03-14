import json
from laberinto import Maze, Room, Door, Wall, Bomba, Norte, Este, Sur, Oeste

class Director:
    def __init__(self):
        self.diccionario=None
        self.builder=LaberintoBuilder()

    def procesar(self,filename):
        self.leer_archivo(filename)
        self.fabricar_laberinto()

    def leer_archivo(self, filename):
        try:
            with open(filename) as f:
                data = json.load(f)
                self.diccionario= data
        except FileNotFoundError:
            print(f"File {filename} does not exist")
            return None
    
    def fabricar_laberinto(self):
        self.builder()
        
        for each in self.diccionario['laberinto']:
            self.crear_laberinto_recursivo(each, 'root')
            
        for each in self.diccionario['puertas']:
            n1 = each[0]
            or1 = each[1]
            n2 = each[2]
            or2 = each[3]
            self.builder.create_door(n1, or1, n2, or2)
    
    def crear_laberinto_recursivo(self, un_dic, padre):
    
        if un_dic['tipo'] == 'habitacion':
            con = self.builder.fabricarHabitacion(un_dic['num'])
            
        if un_dic['tipo'] == 'bomba':
            self.builder.create_bomb(padre)
            
        if 'hijos' in un_dic:
            for each in un_dic['hijos']:
                self.crear_laberinto_recursivo(each, con)

class LaberintoBuilder:
    def __init__(self):
        self.game = None
        self.maze = None
    
    def create_maze(self):
        self.maze= Maze()
    
    def create_wall(self):
        return Wall()
    
    def create_door(self,room1, room2):
        door=Door(room1, room2)
        return door

    def create_bomb(self, room):
        bomba=Bomba()
        room.agregarHijo(bomba)
        return bomba

    def fabricarHabitacion(self, unNum):
        hab = Room(unNum)
        hab.agregarOrientacion(self.fabricarNorte())
        hab.agregarOrientacion(self.fabricarEste())
        hab.agregarOrientacion(self.fabricarSur())
        hab.agregarOrientacion(self.fabricarOeste())

        for each in hab.orientaciones:
            each.poner_elemento(self.create_wall, self)
        self.maze.addRoom(hab)
        return hab

    def fabricarNorte(self):
        return Norte().get_instance()

    def fabricarEste(self):
        return Este.get_instance()
    
    def fabricarSur(self):
        return Sur().get_instance()
    
    def fabricarOeste(self):
        return Oeste().get_instance()
    
    def fabricarPuerta(self, un_num, una_or, otro_num, otra_or):

        lado1 = self.maze.obtenerHabitacion(un_num)
        lado2 = self.maze.obtenerHabitacion(otro_num)
        
        or1 = getattr(self, 'make'+una_or)()
        or2 = getattr(self, 'make'+otra_or)()
        
        pt = Door(lado1, lado2)
        
        lado1.poner_elemento(pt,or1) 
        lado2.poner_elemento(pt,or2)



director=Director()
director.procesar('C:\Users\juanl\Desktop\3INFORMATICA\Diseño\laberintos\laberinto2hab2arm.json')

director.dict