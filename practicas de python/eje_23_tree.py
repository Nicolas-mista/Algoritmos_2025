
from tree import BinaryTree
from queue_ import Queue


#(tabla de criaturas)

def crear_dataset():
    rows = [
        ("Ceto", None),
        ("Tifón", "Zeus"),
        ("Equidna", "Argos Panoptes"),
        ("Dino", None),
        ("Pefredo", None),
        ("Enio", None),
        ("Escila", None),
        ("Caribdis", None),
        ("Euríale", None),
        ("Esteno", None),
        ("Medusa", "Perseo"),
        ("Ladón", "Heracles"),
        ("Águila del Cáucaso", None),
        ("Quimera", "Belerofonte"),
        ("Hidra de Lerna", "Heracles"),
        ("León de Nemea", "Heracles"),
        ("Esfinge", "Edipo"),
        ("Dragón de la Cólquida", None),
        ("Cerbero", None),
        ("Cerda de Cromión", "Teseo"),
        ("Ortro", "Heracles"),
        ("Toro de Creta", "Teseo"),
        ("Jabalí de Calidón", "Atalanta"),
        ("Carcinos", None),
        ("Gerión", "Heracles"),
        ("Cloto", None),
        ("Láquesis", None),
        ("Átropos", None),
        ("Minotauro de Creta", "Teseo"),
        ("Harpías", None),
        ("Argos Panoptes", "Hermes"),
        ("Aves del Estínfalo", None),
        ("Talos", "Medea"),
        ("Sirenas", None),
        ("Pitón", "Apolo"),
        ("Cierva de Cerinea", None),
        ("Basilisco", None),
        ("Jabalí de Erimanto", None),
    ]
    return rows


def insertar_dataset(arbol, rows):
    for name, derrotado_por in rows:
        arbol.insert(name, {
            "derrotado_por": derrotado_por,
            "descripcion": "",
            "capturada": None
        })



# a) listado inorden de las criaturas y quien las derrotó

def listado_inorden(arbol):
    def __rec(root):
        if root is not None:
            __rec(root.left)
            dp = root.other_values.get("derrotado_por")
            print(f"{root.value} — Derrotado por: {dp}")
            __rec(root.right)
    if arbol.root is not None:
        __rec(arbol.root)



# b) cargar y mostrar una breve descripción por criatura

def agregar_descripcion(arbol, descripciones):
    print("#b) Agregando descripciones a criaturas...\n")
    def __rec(root):
        if root is not None:
            __rec(root.left)
            nombre = root.value
            if nombre in descripciones:
                root.other_values["descripcion"] = descripciones[nombre]
                print(f"Descripción agregada a '{nombre}': {descripciones[nombre]}")
            __rec(root.right)
    if arbol.root is not None:
        __rec(arbol.root)
    print("\nDescripciones cargadas correctamente.\n")



# c) mostrar toda la información de la criatura talos

def mostrar_info_talos(arbol):
    pos = arbol.search("Talos")
    if pos:
        print(f"Talos -> {pos.other_values}")
    else:
        print("Talos no encontrado")



# d) determinar los 3 heroes o dioses con mas derrotas

def tres_mayores_derrotadores(arbol):
    ranking = {}
    arbol.ranking(ranking)
    ranking = {k: v for k, v in ranking.items() if k is not None}
    top = sorted(ranking.items(), key=lambda x: x[1], reverse=True)[:3]
    print("\n#d) Top 3 derrotadores:")
    for name, count in top:
        print(f"  {name}: {count} criaturas")



# e) listar las criaturas derrotadas por un heroe

def criaturas_derrotadas_por(arbol, nombre_heroe):
    resultados = []
    def __rec(root):
        if root is not None:
            __rec(root.left)
            if root.other_values.get("derrotado_por") == nombre_heroe:
                resultados.append(root.value)
            __rec(root.right)
    __rec(arbol.root)
    return resultados



# f) listar criaturas que no han sido derrotadas

def no_derrotadas(arbol):
    resultados = []
    def __rec(root):
        if root is not None:
            __rec(root.left)
            if not root.other_values.get("derrotado_por"):
                resultados.append(root.value)
            __rec(root.right)
    __rec(arbol.root)
    return resultados



# g) mostrar campo “capturada” en cada criatura

def mostrar_capturadas(arbol):
    def __rec(root):
        if root is not None:
            __rec(root.left)
            print(f"{root.value} -> capturada por: {root.other_values.get('capturada')}")
            __rec(root.right)
    __rec(arbol.root)



# h) modificar nodos capturados por heracles

def marcar_capturadas_por_heracles(arbol):
    print("#h) Marcando criaturas capturadas por heracles...\n")
    for n in ["cerbero", "toro de creta", "cierva de cerinea", "jabali de erimanto"]:
        nodo = arbol.search(n)
        if nodo:
            nodo.other_values["capturada"] = "heracles"
            print(f"marcada '{n}' como capturada por heracles.")
    print()



# i) busqueda por coincidencia

def busqueda_por_coincidencia(arbol, texto):
    texto = texto.lower()
    matches = []
    def __rec(root):
        if root:
            __rec(root.left)
            if texto in root.value.lower():
                matches.append(root.value)
            __rec(root.right)
    __rec(arbol.root)
    return matches


# j) eliminar al basilisco y a las Sirenas

def eliminar_criaturas(arbol, nombres):
    for n in nombres:
        eliminado, _ = arbol.delete(n)
        if eliminado:
            print(f"Eliminado: {eliminado}")



# k) modificar las aves del estinfalo (heracles derroto varias)

def modificar_aves_estinfalo(arbol):
    nodo = arbol.search("aves del estinfalo")
    if nodo:
        nodo.other_values["derrotado_por"] = "heracles (varias)"
        nodo.other_values["descripcion"] += " — Heracles derrotó a varias de estas aves."
        print("Aves del Estinfalo modificadas.")



# l) modificar el nombre de Ladon a dragon ladon

def renombrar_ladon(arbol):
    eliminado, other = arbol.delete("ladon")
    if eliminado:
        arbol.insert("dragon ladon", other)
        print("ladon renombrado a dragon ladon")



# m) listado por nivel del arbol

def listado_por_nivel(arbol):
    q = Queue()
    if not arbol.root:
        return
    q.arrive(arbol.root)
    nivel = 0
    print("\n#m) Listado por nivel:")
    while q.size() > 0:
        tam = q.size()
        print(f"Nivel {nivel}:")
        for _ in range(tam):
            node = q.attention()
            dp = node.other_values.get("derrotado_por")
            print(f"  {node.value} — derrotado por: {dp}")
            if node.left: q.arrive(node.left)
            if node.right: q.arrive(node.right)
        nivel += 1



# n) Mostrar las criaturas capturadas por Heracles

def criaturas_capturadas_por_heracles(arbol):
    print("\n#n) Criaturas capturadas por Heracles:")
    capturadas = []
    def __rec(root):
        if root:
            __rec(root.left)
            if root.other_values.get("capturada") == "Heracles":
                capturadas.append(root.value)
            __rec(root.right)
    __rec(arbol.root)
    if capturadas:
        for c in capturadas:
            print(f"  - {c}")
    else:
        print("No hay criaturas capturadas por Heracles.")




arbol = BinaryTree()
insertar_dataset(arbol, crear_dataset())

# a)
print("\n#a) Listado inorden:")
listado_inorden(arbol)

# b)
agregar_descripcion(arbol, {
    "Medusa": "Mujer con serpientes por cabello cuya mirada petrifica.",
    "Hidra de Lerna": "Serpiente con múltiples cabezas que se regeneran.",
    "Talos": "Autómata de bronce que protegía la isla de Creta."
})

# c)
print("#c) Información de Talos:")
mostrar_info_talos(arbol)

# d)
tres_mayores_derrotadores(arbol)

# e)
print("\n#e) Criaturas derrotadas por Heracles:")
for c in criaturas_derrotadas_por(arbol, "Heracles"):
    print("  -", c)

# f)
print("\n#f) Criaturas no derrotadas:")
for c in no_derrotadas(arbol):
    print("  -", c)

# g)
print("\n#g) Campo 'capturada' antes de marcar:")
mostrar_capturadas(arbol)

# h)
marcar_capturadas_por_heracles(arbol)

# i)
print("\n#i) Búsqueda por coincidencia 'ja':")
print(busqueda_por_coincidencia(arbol, "ja"))

# j)
print("\n#j) Eliminar Basilisco y Sirenas:")
eliminar_criaturas(arbol, ["Basilisco", "Sirenas"])

# k)
print("\n#k) Modificar Aves del Estínfalo:")
modificar_aves_estinfalo(arbol)

# l)
print("\n#l) Renombrar Ladón:")
renombrar_ladon(arbol)

# m)
listado_por_nivel(arbol)

# n)
criaturas_capturadas_por_heracles(arbol)
