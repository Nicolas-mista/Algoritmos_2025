"""5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
se (MCU), desarrollar un algoritmo que contemple lo siguiente:

a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
leano que indica si es un héroe o un villano, True y False respectivamente;

b. listar los villanos ordenados alfabéticamente;
c. mostrar todos los superhéroes que empiezan con C;
d. determinar cuántos superhéroes hay el árbol;
e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
encontrarlo en el árbol y modificar su nombre;
f. listar los superhéroes ordenados de manera descendente;
g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
los villanos, luego resolver las siguiente tareas:
I. determinar cuántos nodos tiene cada árbol;
II. realizar un barrido ordenado alfabéticamente de cada árbol."""

from tree import BinaryTree


# a. Crear el arbol con heroes y villanos

arbol = BinaryTree()

# Ejemplo de insercion de heroes y villanos
personajes = [
    ("Iron Man", False),
    ("Captain America", False),
    ("Thor", False),
    ("Doctor Strange", False),
    ("Thanos", True),
    ("Loki", True),
    ("Captain Marvel", False),
    ("Crimson Dynamo", True),
]

for nombre, es_villano in personajes:
    arbol.insert(nombre, {"is_villain": es_villano})

# -------------------------------
# b. Listar villanos ordenados alfabeticamente

print("Villanos ordenados alfabeticamente:")
arbol.villain_in_order()

# -------------------------------
# c. Mostrar todos los superheroes que empiezan con 'C'

print("Superheroes que empiezan con 'C':")
def superheroes_starting_with_c(root):
    if root is not None:
        superheroes_starting_with_c(root.left)
        if not root.other_values["is_villain"] and root.value.startswith("C"):
            print(root.value)
        superheroes_starting_with_c(root.right)

superheroes_starting_with_c(arbol.root)

# -------------------------------
# d. Determinar cuentos superheroes hay en el arbol

total_heroes = arbol.count_heroes()
print(f"Cantidad de superheroes: {total_heroes}")

# -------------------------------
# e. Corregir Doctor Strange usando busqueda por proximidad

def correct_doctor_strange(root, correct_name):
    if root is not None:
        correct_doctor_strange(root.left, correct_name)
        if root.value.startswith("Doctor Strange"):
            root.value = correct_name
        correct_doctor_strange(root.right, correct_name)

correct_doctor_strange(arbol.root, "Doctor Strange (MCU)")

# Verificar corrección
print("Arbol despues de corregir Doctor Strange:")
arbol.in_order()

# -------------------------------
# f. Listar superheroes ordenados de manera descendente

print("Superheroes ordenados de manera descendente:")
def superheroes_descending(root):
    if root is not None:
        superheroes_descending(root.right)
        if not root.other_values["is_villain"]:
            print(root.value)
        superheroes_descending(root.left)

superheroes_descending(arbol.root)

# -------------------------------
# g. Generar un bosque: un arbol de heroes y otro de villanos

arbol_heroes = BinaryTree()
arbol_villanos = BinaryTree()
arbol.divide_tree(arbol_heroes, arbol_villanos)

# g-I. Determinar cuantos nodos tiene cada arbol
total_heroes_tree = arbol_heroes.count_heroes()
def count_villains(root):
    if root is None:
        return 0
    count = 1 if root.other_values["is_villain"] else 0
    count += count_villains(root.left)
    count += count_villains(root.right)
    return count

total_villains_tree = count_villains(arbol_villanos.root)

print(f"Cantidad de nodos en arbol de heroes: {total_heroes_tree}")
print(f"Cantidad de nodos en arbol de villanos: {total_villains_tree}")

# g-II. Barrido ordenado alfabeticamente de cada arbol
print("Heroes ordenados alfabeticamente:")
arbol_heroes.in_order()

print("Villanos ordenados alfabeticamente:")
arbol_villanos.in_order()
