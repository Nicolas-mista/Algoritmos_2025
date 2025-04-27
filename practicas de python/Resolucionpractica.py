#Trabajo de recursividad fecha 28/04/25
#Actividad numero 5 
def romano_a_decimal(romano):
    
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 
               'C': 100, 'D': 500, 'M': 1000}
    
    
    if len(romano) == 1:
        return valores[romano]
    
   
    if valores[romano[0]] >= valores[romano[1]]:
        return valores[romano[0]] + romano_a_decimal(romano[1:])
    else:
       
        return -valores[romano[0]] + romano_a_decimal(romano[1:])


romano = input("Ingrese un número romano: ").upper()
decimal = romano_a_decimal(romano)
print(f"El número decimal equivalente a {romano} es: {decimal}")




#Actividad numero 22

def Usofuerza(mochila, objetos_sacados=0):
   
    if len(mochila) == 0:
        print("No se encontró el sable de luz.")
        return False, objetos_sacados

    
    objeto = mochila.pop(0)
    objetos_sacados += 1

    
    if objeto == "sable de luz":
        print(f"Sable de luz encontrado después de sacar {objetos_sacados} objetos.")
        return True, objetos_sacados
    else:
        
        return Usofuerza(mochila, objetos_sacados)
