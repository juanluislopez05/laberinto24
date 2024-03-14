import time
class Bicho:

    def __init__(self, modo):
        self.modo = modo
        self.vidas = 10
        self.poder = 3
        self.posicion = None
        self.num=0
        
    def actua(self):
        self.modo.actua(self)

    def __str__(self):
        template='Bicho-{0.modo}{0.num}'
        return template.format(self)
        
    def caminarAleatorio(self):
        self.posicion.caminarAleatorio(self)
    
    def esAgresivo(self):
        return self.modo.esAgresivo()

    def esPerezoso(self):
        return self.modo.esPerezoso()
        
    def irAEste(self):
        self.posicion.irAEste(self)
        
    def irAOeste(self):
        self.posicion.irAOeste(self)
        
    def irASur(self):
        self.posicion.irASur(self)
        
    def irANorte(self):
        self.posicion.irANorte(self)

    def start(self):
        self.actua()

    def stop(self):
        print(self , " ha sido parado")
        exit(0)

class Modo:
  def __init__(self):
        pass
  def __str__(self):    
        pass
  def esAgresivo(self):
        return False
  def esPerezoso(self):
        return False

  def caminar(self, bicho):
    
    bicho.caminarAleatorio()

  def dormir(self, unBicho):
           print(unBicho.print())
           print(unBicho + ' duerme')
           time.sleep(2)  

  def actua(self, bicho):
    self.caminar(bicho)
    self.dormir(bicho)


class Agresivo(Modo):
  def __init__(self):
        super().__init__()
    
  def __str__(self):
        return "Agresivo"
    
  def esAgresivo(self):
        return True

  def print(self):
        print("Bicho Agresivo")

class Perezoso(Modo):
  def __init__(self):
        super().__init__()
    
  def __str__(self):
        return "Perezoso"
    
  def esPerezoso(self):
        return True
  
  def print(self):
        print("Bicho perezoso")