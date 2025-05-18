#Aca defino los trajes, ejersicio 13
class TrajeIronMan:
    def __init__(self, modelo, pelicula, estado):
        self.modelo = modelo
        self.pelicula = pelicula
        self.estado = estado

    def __str__(self):
        return f"{self.modelo} - {self.pelicula} - {self.estado}"


pila = []


pila.append(TrajeIronMan("Mark III", "Iron Man", "Dañado"))
pila.append(TrajeIronMan("Mark V", "Iron Man 2", "Impecable"))
pila.append(TrajeIronMan("Mark XLIV", "Avengers: Age of Ultron", "Dañado"))
pila.append(TrajeIronMan("Mark XLVII", "Spider-Man: Homecoming", "Destruido"))
pila.append(TrajeIronMan("Mark XLVI", "Capitan America: Civil War", "Dañado"))
pila.append(TrajeIronMan("Mark L", "Avengers: Infinity War", "Destruido"))


import copy
pila_original = copy.deepcopy(pila)

#punto a
print("a. Películas donde se usó el modelo Mark XLIV (Hulkbuster):")
encontrado = False
for traje in reversed(pila):
    if traje.modelo == "Mark XLIV":
        print(f"- {traje.pelicula}")
        encontrado = True
if not encontrado:
    print("No se usó el modelo Mark XLIV.")

#punto b
print("\nb. Modelos que quedaron dañados:")
for traje in reversed(pila):
    if traje.estado == "Dañado":
        print(f"- {traje.modelo} ({traje.pelicula})")

#punto c
print("\nc. Modelos destruidos eliminados:")
pila_aux = []
while pila:
    traje = pila.pop()
    if traje.estado == "Destruido":
        print(f"- {traje.modelo} ({traje.pelicula})")
    else:
        pila_aux.append(traje)

while pila_aux:
    pila.append(pila_aux.pop())



#punto e
print("\ne. Agregando modelo Mark LXXXV:")
pelicula_nueva = "Avengers: Endgame"
modelo_nuevo = "Mark LXXXV"
repetido = any(t.modelo == modelo_nuevo and t.pelicula == pelicula_nueva for t in pila)
if not repetido:
    pila.append(TrajeIronMan(modelo_nuevo, pelicula_nueva, "Impecable"))
    print("Modelo agregado correctamente.")
else:
    print("Ya existe ese modelo en esa película, no se agrega.")

#punto f
print("\nf. Trajes utilizados en:")
peliculas_consulta = ["Spider-Man: Homecoming", "Capitan America: Civil War"]
for pelicula in peliculas_consulta:
    print(f"- {pelicula}:")
    for traje in reversed(pila):
        if traje.pelicula == pelicula:
            print(f"  * {traje.modelo}")
            

# ejersico 24
class PersonajeMCU:
    def __init__(self, nombre, cantidad_peliculas):
        self.nombre = nombre
        self.cantidad_peliculas = cantidad_peliculas

    def __str__(self):
        return f"{self.nombre} - {self.cantidad_peliculas} películas"


pila = []

#ej de personajes
pila.append(PersonajeMCU("Iron Man", 10))
pila.append(PersonajeMCU("Captain America", 9))
pila.append(PersonajeMCU("Thor", 9))
pila.append(PersonajeMCU("Black Widow", 8))
pila.append(PersonajeMCU("Hawkeye", 6))
pila.append(PersonajeMCU("Hulk", 7))
pila.append(PersonajeMCU("Rocket Raccoon", 4))
pila.append(PersonajeMCU("Groot", 5))
pila.append(PersonajeMCU("Doctor Strange", 4))
pila.append(PersonajeMCU("Gamora", 5))
pila.append(PersonajeMCU("Star-Lord", 4))
pila.append(PersonajeMCU("Spider-Man", 3))
pila.append(PersonajeMCU("Captain Marvel", 3))

#punto a
print("a. Posición desde la cima:")
posicion = 1
for personaje in reversed(pila): 
    if personaje.nombre == "Rocket Raccoon":
        print(f"- Rocket Raccoon está en la posición {posicion}")
    if personaje.nombre == "Groot":
        print(f"- Groot está en la posición {posicion}")
    posicion += 1

#punto b
print("\nb. Personajes que participaron en más de 5 películas:")
for personaje in reversed(pila):
    if personaje.cantidad_peliculas > 5:
        print(f"- {personaje.nombre}: {personaje.cantidad_peliculas} películas")

#punto c
print("\nc. Cantidad de películas de Black Widow:")
encontrado = False
for personaje in reversed(pila):
    if personaje.nombre == "Black Widow":
        print(f"- Black Widow participó en {personaje.cantidad_peliculas} películas")
        encontrado = True
        break
if not encontrado:
    print("- Black Widow no se encuentra en la pila")

#punto d
print("\nd. Personajes cuyos nombres empiezan con C, D o G:")
for personaje in reversed(pila):
    if personaje.nombre.startswith(("C", "D", "G")):
        print(f"- {personaje.nombre}")
