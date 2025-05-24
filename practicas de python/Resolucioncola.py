#ejersicio 10 
from collections import namedtuple, deque

#cuerpo de las notis
Notificacion = namedtuple('Notificacion', ['hora', 'aplicacion', 'mensaje'])

# a. Eliminacion noti facebook
def eliminar_facebook(cola):
    nueva_cola = deque()
    while cola:
        noti = cola.popleft()
        if noti.aplicacion.lower() != 'facebook':
            nueva_cola.append(noti)
    return nueva_cola

# b. notis de twitter
def mostrar_twitter_python(cola):
    aux = deque()
    print("Notificaciones de Twitter con 'Python':")
    while cola:
        noti = cola.popleft()
        if noti.aplicacion.lower() == 'twitter' and 'python' in noti.mensaje.lower():
            print(noti)
        aux.append(noti)
    while aux:
        cola.append(aux.popleft())


def en_rango(hora, inicio, fin):
    return inicio <= hora <= fin

# c. pila para las horas
def contar_notificaciones_rango(cola):
    pila = []
    aux = deque()
    inicio = "11:43"
    fin = "15:57"
    while cola:
        noti = cola.popleft()
        if en_rango(noti.hora, inicio, fin):
            pila.append(noti)
        aux.append(noti)
    while aux:
        cola.append(aux.popleft())
    return len(pila)
#ejemplo
cola = deque([
    Notificacion("11:45", "Twitter", "Aprendiendo Python"),
    Notificacion("12:30", "Facebook", "Nueva publicación"),
    Notificacion("14:00", "Instagram", "Historia nueva"),
    Notificacion("13:20", "Twitter", "Python es genial"),
    Notificacion("16:10", "Facebook", "Mensaje nuevo"),
])

# a. Eliminar notificaciones de Facebook
cola = eliminar_facebook(cola)

# b. Mostrar notificaciones de Twitter que contienen "Python"
mostrar_twitter_python(cola)

# c. Contar notificaciones entre 11:43 y 15:57
cantidad = contar_notificaciones_rango(cola)
print(f"\nCantidad de notificaciones entre 11:43 y 15:57: {cantidad}")
