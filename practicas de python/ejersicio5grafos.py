"""5. Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos nece-
sarios para resolver las tareas, listadas a continuación:

a. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servi-
dor, router, switch, impresora;
b. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook:
Red Hat, Debian, Arch;
c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro,
Red Hat, Fedora hasta la impresora;
d. encontrar el árbol de expansión mínima;
e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”;
f. indicar desde que computadora del switch 01 es el camino más corto
al servidor “MongoDB”;
g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b;
h. debe utilizar un grafo no dirigido."""

from graph import Graph

g = Graph(is_directed=False)

nodos = {
    # de las pcs
    'Manjaro': 'pc',
    'Parrot': 'pc',
    'Fedora': 'pc',
    'Mint': 'pc',
    'Ubuntu': 'pc',

    # de las notebooks
    'Red Hat': 'notebook',
    'Debian': 'notebook',
    'Arch': 'notebook',

    # servidores
    'Guaraní': 'servidor',
    'MongoDB': 'servidor',

    # switches
    'Switch1': 'switch',
    'Switch2': 'switch',

    # routers
    'Router1': 'router',
    'Router2': 'router',
    'Router3': 'router',

    # mpresora
    'Impresora': 'impresora'
}


for nombre, tipo in nodos.items():
    g.insert_vertex(nombre)
    pos = g.search(nombre, 'value')
    g[pos].other_values = tipo




# 1 conexiones switch1 
g.insert_edge('Switch1', 'Debian', 17)
g.insert_edge('Switch1', 'Ubuntu', 18)
g.insert_edge('Switch1', 'Mint', 80)
g.insert_edge('Switch1', 'Impresora', 22)

# Router1
g.insert_edge('Router1', 'Switch1', 29)
g.insert_edge('Router1', 'Router2', 37)
g.insert_edge('Router1', 'Router3', 43)

# Router2
g.insert_edge('Router2', 'Red Hat', 25)
g.insert_edge('Router2', 'Guaraní', 9)
g.insert_edge('Router2', 'Router3', 50)

# Router3
g.insert_edge('Router3', 'Switch2', 61)

# conexiones switch2
g.insert_edge('Switch2', 'Manjaro', 40)
g.insert_edge('Switch2', 'Parrot', 12)
g.insert_edge('Switch2', 'MongoDB', 5)
g.insert_edge('Switch2', 'Arch', 56)

# pc Fedora
g.insert_edge('Fedora', 'Switch2', 3)


def reconstruir_camino(stack, origen, destino):
    camino = []
    peso_total = None
    actual = destino
    while stack.size() > 0:
        nodo = stack.pop()   
        nombre, costo, predecesor = nodo
        if nombre == actual:
            if peso_total is None:
                peso_total = costo
            camino.append(nombre)
            actual = predecesor
    if len(camino) == 0:
        return None, None
    camino.reverse()
    return camino, peso_total



#b- barridos

def barridos():
    notebooks = ['Red Hat', 'Debian', 'Arch']
    for n in notebooks:
        print("\n DFS DESDE", n, "")
        g.deep_sweep(n)

        print(" BFS DESDE", n, "")
        g.amplitude_sweep(n)



#c- camino mas cortos a la impresora

def camino_impresora():
    pcs = ['Manjaro', 'Red Hat', 'Fedora']
    for pc in pcs:
        stack = g.dijkstra(pc)
        camino, peso = reconstruir_camino(stack, pc, 'Impresora')
        print(f"\nCamino desde {pc} a Impresora: {camino}, peso total = {peso}")



#d- mst kruskal

def mst():
    print("\nÁRBOL DE EXPANSIÓN MÍNIMA (Kruskal):")
    print(g.kruskal('Manjaro'))



#E- PC → Servidor Guaraní

def pc_mas_cerca_guarani():
    mejores_pc = None
    mejor_peso = None

    for v in g:
        if v.other_values == 'pc':
            stack = g.dijkstra(v.value)
            camino, peso = reconstruir_camino(stack, v.value, 'Guaraní')
            if peso is not None:
                if mejor_peso is None or peso < mejor_peso:
                    mejor_peso = peso
                    mejores_pc = v.value

    print(f"\nLa PC más cercana al servidor Guaraní es: {mejores_pc}, peso = {mejor_peso}")



# f

def switch1_a_mongodb():
    pos = g.search('Switch1', 'value')
    vecinos = [edge.value for edge in g[pos].edges]

    mejor = None
    mejor_peso = None

    for compu in vecinos:
        stack = g.dijkstra(compu)
        camino, peso = reconstruir_camino(stack, compu, 'MongoDB')
        if peso is not None:
            if mejor_peso is None or peso < mejor_peso:
                mejor_peso = peso
                mejor = compu

    print(f"\nLa computadora del Switch1 con menor camino a MongoDB es: {mejor}, peso = {mejor_peso}")



#g

def mover_impresora():
    print("\n MOVIENDO IMPRESORA A ROUTER2 ")
    g.delete_edge('Impresora', 'Switch1', 'value')
    g.insert_edge('Impresora', 'Router2', 22)
    print("\n>>> Nuevos barridos desde notebooks:")
    barridos()




print("\n\n INCISO B ")
barridos()

print("\n\n INCISO C ")
camino_impresora()

print("\n\nINCISO D ")
mst()

print("\n\nINCISO E ")
pc_mas_cerca_guarani()

print("\n\n INCISO F ")
switch1_a_mongodb()

print("\n\n INCISO G ")
mover_impresora()
