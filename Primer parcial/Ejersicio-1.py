#empiezo definiendo y busco al capitan america(consigna a)
def buscar_capitan(superheroes: list, indice: int = 0) -> bool:
    if indice >= len(superheroes):
        return False
    if superheroes[indice].lower() == "capitan america":
        return True
    return buscar_capitan(superheroes, indice + 1)

#estructura lista recursiva de los personajes(consignab)
def listar_superheroes(superheroes: list, indice: int = 0) -> None:
    if indice >= len(superheroes):
        return
    print(superheroes[indice])
    listar_superheroes(superheroes, indice + 1)
superheroes = ["hulk", "thor", "black widow", "deadpool","vision",
    "hombre araña", "doctor strange", "falcon","pantera negra",
    "ant-Man", "capitan america", "scarlet witch", 
    "wolverine","falcon", "doctor doom", "iron man",]

encontrado = buscar_capitan(superheroes)
print("Esta capitan america?", "si" if encontrado else "no")

print("Lista de superheroes:")
listar_superheroes(superheroes)