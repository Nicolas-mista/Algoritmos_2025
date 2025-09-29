from list_ import List


superheroes = List([
    {"nombre": "Linterna Verde", "anio": 1940, "casa": "DC", "biografia": "Héroe con anillo de poder y traje especial"},
    {"nombre": "Wolverine", "anio": 1974, "casa": "Marvel", "biografia": "Mutante con garras de adamantium y factor curativo"},
    {"nombre": "Dr. Strange", "anio": 1963, "casa": "DC", "biografia": "Mago supremo con capa levitante"},
    {"nombre": "Capitana Marvel", "anio": 1968, "casa": "Marvel", "biografia": "Heroína con traje espacial y poderes cósmicos"},
    {"nombre": "Mujer Maravilla", "anio": 1941, "casa": "DC", "biografia": "Guerrera amazona con armadura y lazo de la verdad"},
    {"nombre": "Flash", "anio": 1940, "casa": "DC", "biografia": "El hombre más rápido con traje rojo"},
    {"nombre": "Star-Lord", "anio": 1976, "casa": "Marvel", "biografia": "Líder de los Guardianes de la Galaxia con casco y armas"},
    {"nombre": "Batman", "anio": 1939, "casa": "DC", "biografia": "Detective con traje de murciélago y gadgets"},
    {"nombre": "Spider-Man", "anio": 1962, "casa": "Marvel", "biografia": "Joven héroe con traje rojo y azul, poderes arácnidos"},
    {"nombre": "Superman", "anio": 1938, "casa": "DC", "biografia": "El hombre de acero con traje azul y capa roja"},
])


superheroes.add_criterion("nombre", lambda hero:hero["nombre"])
superheroes.add_criterion("anio", lambda hero: hero["anio"])
superheroes.add_criterion("casa", lambda hero: hero["casa"])

# a. 
superheroes.delete_value("Linterna Verde", "nombre")

# b. 
idx = superheroes.search("Wolverine", "nombre")
print("b) Wolverine apareció en:", superheroes[idx]["anio"])

# c. 
idx = superheroes.search("Dr. Strange", "nombre")
superheroes[idx]["casa"] = "Marvel"

# d. 
print("d) Héroes con 'traje' o 'armadura' en la biografía:")
for hero in superheroes:
    if "traje" in hero["biografia"].lower() or "armadura" in hero["biografia"].lower():
        print("-", hero["nombre"])

# e. 
print("e) Héroes anteriores a 1963:")
for hero in superheroes:
    if hero["anio"] < 1963:
        print("-", hero["nombre"], "(", hero["casa"], ")")

# f. 
print("f) Casas de Capitana Marvel y Mujer Maravilla:")
for name in ["Capitana Marvel", "Mujer Maravilla"]:
    idx = superheroes.search(name, "nombre")
    print("-", name, "->", superheroes[idx]["casa"])

# g.
print("g) Información de Flash y Star-Lord:")
for name in ["Flash", "Star-Lord"]:
    idx = superheroes.search(name, "nombre")
    print("-", superheroes[idx])

# h. 
print("h) Héroes que comienzan con B, M o S:")
for hero in superheroes:
    if hero["nombre"].startswith(("B", "M", "S")):
        print("-", hero["nombre"])

# i. 
conteo = {}
for hero in superheroes:
    conteo[hero["casa"]] = conteo.get(hero["casa"], 0) + 1
print("i) Cantidad de superhéroes por casa:", conteo)
