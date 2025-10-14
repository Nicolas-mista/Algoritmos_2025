# main.py
from tree import BinaryTree
from queue_ import Queue

def crear_dataset():
    # Datos basados en la tabla que enviaste (nombre: derrotado_por)
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

# a: listado inorden
def listado_inorden(arbol):
    def __rec(root):
        if root is not None:
            __rec(root.left)
            dp = root.other_values.get("derrotado_por")
            print(f"{root.value}  —  Derrotado por: {dp}")
            __rec(root.right)
    if arbol.root is not None:
        __rec(arbol.root)

# b: agregar descripcion (ejemplo automático)
def agregar_descripcion(arbol, descripciones):
    def __rec(root):
        if root is not None:
            __rec(root.left)
            name = root.value
            if name in descripciones:
                root.other_values["descripcion"] = descripciones[name]
            __rec(root.right)
    if arbol.root is not None:
        __rec(arbol.root)

# c: mostrar toda la info de Talos
def mostrar_info_talos(arbol):
    pos = arbol.search("Talos")
    if pos is not None:
        print("Talos ->", pos.value, pos.other_values)
    else:
        print("Talos no encontrado")

# d: 3 héroes o dioses que derrotaron mayor cantidad de criaturas
def tres_mayores_derrotadores(arbol):
    ranking = {}
    arbol.ranking(ranking)  # utiliza la función que ya está en tree.py
    # filtrar None
    ranking = {k: v for k, v in ranking.items() if k is not None}
    # ordenar por cantidad descendente
    top = sorted(ranking.items(), key=lambda x: x[1], reverse=True)[:3]
    print("Top 3 derrotadores:")
    for name, count in top:
        print(f"{name}: {count} criaturas")

# e: listar criaturas derrotadas por un héroe
def criaturas_derrotadas_por(arbol, nombre_heroe):
    resultados = []
    def __rec(root):
        if root is not None:
            __rec(root.left)
            if root.other_values.get("derrotado_por") == nombre_heroe:
                resultados.append(root.value)
            __rec(root.right)
    if arbol.root is not None:
        __rec(arbol.root)
    return resultados

# f: criaturas que no han sido derrotadas
def no_derrotadas(arbol):
    resultados = []
    def __rec(root):
        if root is not None:
            __rec(root.left)
            if not root.other_values.get("derrotado_por"):
                resultados.append(root.value)
            __rec(root.right)
    if arbol.root is not None:
        __rec(arbol.root)
    return resultados

# g: (ya tenemos el campo 'capturada' en other_values); función para mostrar capturas
def mostrar_capturadas(arbol):
    def __rec(root):
        if root is not None:
            __rec(root.left)
            print(f"{root.value} -> capturada por: {root.other_values.get('capturada')}")
            __rec(root.right)
    if arbol.root is not None:
        __rec(arbol.root)

# h: marcar capturadas por Heracles para nodos específicos
def marcar_capturadas_por_heracles(arbol):
    nombres = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]
    for n in nombres:
        nodo = arbol.search(n)
        if nodo is not None:
            nodo.other_values["capturada"] = "Heracles"
            print(f"Marcado {n} como capturada por Heracles")
        else:
            print(f"{n} no encontrado para marcar captura")

# i: búsquedas por coincidencia (subcadena, case-insensitive)
def busqueda_por_coincidencia(arbol, texto):
    texto = texto.lower()
    matches = []
    def __rec(root):
        if root is not None:
            __rec(root.left)
            if texto in root.value.lower():
                matches.append((root.value, root.other_values))
            __rec(root.right)
    if arbol.root is not None:
        __rec(arbol.root)
    return matches

# j: eliminar Basilisco y Sirenas
def eliminar_criaturas(arbol, nombres):
    for n in nombres:
        deleted_value, other = arbol.delete(n)
        if deleted_value is not None:
            print(f"Eliminado: {deleted_value}")
        else:
            print(f"No se encontró para eliminar: {n}")

# k: modificar Aves del Estínfalo
def modificar_aves_estinfalo(arbol):
    nodo = arbol.search("Aves del Estínfalo")
    if nodo is not None:
        # añadimos texto descriptivo y actualizamos derrotado_por
        nodo.other_values["derrotado_por"] = "Heracles (varias)"
        nodo.other_values["descripcion"] = nodo.other_values.get("descripcion", "") + " — Heracles derrotó a varias de estas aves."
        print("Aves del Estínfalo modificadas.")
    else:
        print("Aves del Estínfalo no encontradas")

# l: renombrar Ladón por Dragón Ladón
def renombrar_ladon(arbol):
    deleted, other = arbol.delete("Ladón")
    if deleted is not None:
        other["name"] = "Dragón Ladón"
        arbol.insert("Dragón Ladón", other)
        print("Ladón renombrado a Dragón Ladón")
    else:
        print("Ladón no encontrado para renombrar")

# m: listado por nivel (mostrando nombre y derrotado_por)
def listado_por_nivel(arbol):
    # usamos la clase Queue para recorrer por nivel (por claridad implementamos aquí)
    q = Queue()
    if arbol.root is None:
        return
    q.arrive(arbol.root)
    level = 0
    print("Listado por nivel:")
    while q.size() > 0:
        level_size = q.size()
        print(f"Nivel {level}:")
        for _ in range(level_size):
            node = q.attention()
            dp = node.other_values.get("derrotado_por")
            print(f"  {node.value}  — derrotado por: {dp}")
            if node.left is not None:
                q.arrive(node.left)
            if node.right is not None:
                q.arrive(node.right)
        level += 1
        
# n) mostrar criaturas capturadas por Heracles
def criaturas_capturadas_por_heracles(arbol):
    print("n) Criaturas capturadas por Heracles:")
    capturadas = []
    def __rec(root):
        if root is not None:
            __rec(root.left)
            if root.other_values.get("capturada") == "Heracles":
                capturadas.append(root.value)
            __rec(root.right)
    if arbol.root is not None:
        __rec(arbol.root)
    if capturadas:
        for c in capturadas:
            print(f"  - {c}")
    else:
        print("No hay criaturas capturadas por Heracles.")

# ---------------------------
# Programa principal de prueba
# ---------------------------
if __name__ == "__main__":
    arbol = BinaryTree()
    rows = crear_dataset()
    insertar_dataset(arbol, rows)

    print("a) Listado inorden (criaturas y quien las derrotó):")
    listado_inorden(arbol)
    print("\n" + "-"*50)

    # b) agregar descripciones de ejemplo
    descripciones_ej = {
        "Medusa": "Mujer con serpientes por cabello cuya mirada petrifica.",
        "Hidra de Lerna": "Serpiente con múltiples cabezas que se regeneran.",
        "Talos": "Autómata de bronce que protegía la isla de Creta."
    }
    agregar_descripcion(arbol, descripciones_ej)
    print(f"b) Descripciones agregadas:{descripciones_ej}")

    # c) mostrar Talos
    print("\nc) Mostrar info Talos:")
    mostrar_info_talos(arbol)
    print("\n" + "-"*50)

    # d) top 3 derrotadores
    print("d) Top 3 derrotadores:")
    tres_mayores_derrotadores(arbol)
    print("\n" + "-"*50)

    # e) criaturas derrotadas por Heracles
    print("e) Criaturas derrotadas por Heracles:")
    heracles_list = criaturas_derrotadas_por(arbol, "Heracles")
    for c in heracles_list:
        print("  -", c)
    print("\n" + "-"*50)

    # f) criaturas no derrotadas
    print("f) Criaturas no derrotadas:")
    for c in no_derrotadas(arbol):
        print("  -", c)
    print("\n" + "-"*50)

    # g) mostrar campo capturada (todavía None)
    print("g) Campo 'capturada' (antes de marcar):")
    mostrar_capturadas(arbol)
    print("\n" + "-"*50)

    # h) marcar capturadas por Heracles
    print("h) Marcar algunas criaturas como capturadas por Heracles:")
    marcar_capturadas_por_heracles(arbol)
    print("\nCampo 'capturada' luego de marcar:")
    mostrar_capturadas(arbol)
    print("\n" + "-"*50)

    # i) busqueda por coincidencia
    print("i) Búsqueda por coincidencia 'ja' (ejemplo):")
    matches = busqueda_por_coincidencia(arbol, "ja")
    for name, other in matches:
        print(f"  {name} -> {other}")
    print("\n" + "-"*50)

    # j) eliminar Basilisco y Sirenas
    print("j) Eliminando Basilisco y Sirenas:")
    eliminar_criaturas(arbol, ["Basilisco", "Sirenas"])
    print("\nListado inorden tras eliminaciones:")
    listado_inorden(arbol)
    print("\n" + "-"*50)

    # k) modificar Aves del Estínfalo
    print("k) Modificar Aves del Estínfalo:")
    modificar_aves_estinfalo(arbol)
    pos = arbol.search("Aves del Estínfalo")
    if pos: print("  ->", pos.value, pos.other_values)
    print("\n" + "-"*50)

    # l) renombrar Ladón
    print("l) Renombrar Ladón por Dragón Ladón:")
    renombrar_ladon(arbol)
    print("Buscar Dragón Ladón:")
    pos = arbol.search("Dragón Ladón")
    if pos: print("  ->", pos.value, pos.other_values)
    print("\n" + "-"*50)

    # m) listado por nivel
    print("m) Listado por nivel:")
    listado_por_nivel(arbol)
# n)
    criaturas_capturadas_por_heracles(arbol)