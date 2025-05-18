#Aca defino los trajes
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
