#punto 6
def invertir(palabra):
    
    if len(palabra) <= 1:
        return palabra
    
    return palabra[-1] + invertir(palabra[:-1])


secuencia = "Asado"
resultado = invertir(secuencia)
print (resultado)

