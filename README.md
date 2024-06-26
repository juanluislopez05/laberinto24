<body>
    <h1><strong>MAZE GAME 2024</strong></h1>
    <p>Proyecto del laberinto del curso 23-24</p>

El código (maze.py) de este repositorio ha sido desarrollado mediante el uso de SourceGraph Cody

Initial prompt

Describir en Python los objetos Maze, Wall, Door y Room:

- El objeto Laberinto tiene una colección de objetos Room.
- Cada Room tiene cuatro lados (norte, este, oeste, sur), inicialmente cada lado es nulo.
- El objeto Door tiene dos lados que pueden ser objetos Room.
- El objeto Maze tiene una operación `addRoom` que recibe un objeto Room como parámetro.

---

Decorator prompt

- Añadir clase Decorator que es sublclase de MapElement

---

Strategy prompt

- Añadir clase Bicho, con atributos modo, vidas, poder y posicion, la clase Bicho que cuenta con las subclases Agresivo y Perezoso.
---

Composite prompt

- Aplicar los siguientes cambios: añadir clase Contenedor, subclase de MapElement and Room ahora es subclase de Contenedor. 
Añadir clase Hoja is subclass of MapElement.
Decorator es ahora subclase de Hoja
---

Iterator prompt

- Añadir el metodo recorrer en MapElement y sus subclases 
- Este metodo en Contenedor consiste en recorrer todos sus hijos.
- En el resto consiste en pasarle a unBloque, self.

---

TemplateMethod prompt

- Este método consiste en delegar la función `actua`de Bicho en Modo.
- El método `actua`de Bicho consiste en llamar a otros metodos como `caminar`y `dormir`.
- El método `caminar` consiste en llamar al método `caminarAleatorio` de Bicho.
- El método `dormir`consiste en dormir el bicho durante 2 segundos.
---

Singleton prompt

- Este método se implementa mediante la inclusión de la clase Orientación y sus subclases Norte, Sur, Este y Oeste, de manera que se garantice que solo hay una única instancia de éstas.
---

Builder prompt

- Este método va aparte, con un import de las clases de Maze de laberinto.py
- Tiene métodos como `leer_archivo` que nos permite leer los json que le vamos a pasar.
- También métodos como `procesar`que se le pasa `leer_archivo`y `fabricar_laberinto`.
- Otros métodos consiste en sobrescribir los de laberinto.py

---
Proxy prompt 
- En el caso de Proxy, lo hemos implementado a través de ElementoMapa (Subject), Tunel (Proxy) y Laberinto (RealSubject). 
- En este caso, hemos usado el atributo laberinto para refererirnos a la clase homónima.

---

Adapter prompt
- Este patrón no lo hemos incluido de momento en el laberinto
---
Bridge prompt
- Este patrón lo hemos incluido mediante la inclusión de la clase Forma y su subclase Cuadrado
- Forma cuenta con el atributo orientaciones y los metodos recorrer, agregarOrientacion y ponerEn que ya hemos tratado en otras clasles
- Cuadrado cuenta con los atributos norte sur este y oeste y los respetivos metodos irAlNorte, irAlSur, irAlEste y irAlOeste
---
Mediator prompt
- Este patrón lo hemos implementado mediante la clase Ente que es superclase de Bicho y la nueva clase Personaje.
- Hay que tener en cuenta que Juego cuenta con bichos y personajes como variables.
- Ente cuenta con los atributos poder posicion vidas juego.
- Personaje cuenta con el atributo nombre e inicializa vidas a 10 y poder a 1. Cuenta tambien con el metodo esAtacadoPor.
- Ente tiene el metodo estaVivo que devuelve true si vidas>0 y irAlEste, irAlNorte, irAlSsur e irAlOeste.
</body>
</html>
