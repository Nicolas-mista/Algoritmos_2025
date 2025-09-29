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

Ej:22 from list_ import List

jedi = List([
    {"nombre": "Yoda", "maestros": [], "sables": ["verde"], "especie": "desconocida"},
    {"nombre": "Luke Skywalker", "maestros": ["Obi-Wan Kenobi", "Yoda"], "sables": ["azul", "verde"], "especie": "humano"},
    {"nombre": "Anakin Skywalker", "maestros": ["Obi-Wan Kenobi"], "sables": ["azul"], "especie": "humano"},
    {"nombre": "Obi-Wan Kenobi", "maestros": ["Qui-Gon Jinn"], "sables": ["azul"], "especie": "humano"},
    {"nombre": "Qui-Gon Jinn", "maestros": ["Conde Dooku"], "sables": ["verde"], "especie": "humano"},
    {"nombre": "Mace Windu", "maestros": ["Cyslin Myr"], "sables": ["violeta"], "especie": "humano"},
    {"nombre": "Ahsoka Tano", "maestros": ["Anakin Skywalker"], "sables": ["verde", "azul", "blanco"], "especie": "togruta"},
    {"nombre": "Kit Fisto", "maestros": [], "sables": ["verde"], "especie": "nautolano"},
    {"nombre": "Plo Koon", "maestros": [], "sables": ["naranja"], "especie": "kel dor"},
    {"nombre": "Aayla Secura", "maestros": ["Quinlan Vos"], "sables": ["azul"], "especie": "twi'lek"},
])


jedi.add_criterion("nombre", lambda j: j["nombre"])
jedi.add_criterion("especie", lambda j: j["especie"])


# a) Listado por nombre y especie
print("a) Jedi ordenados por nombre:")
jedi.sort_by_criterion("nombre")
for j in jedi:
    print(j["nombre"])

print("Jedi ordenados por especie:")
jedi.sort_by_criterion("especie")
for j in jedi:
    print("-" ,j["nombre"], "(", j["especie"], ")")


# b) Info de Ahsoka Tano y Kit Fisto
print("b) Info de Ahsoka Tano y Kit Fisto:")
for name in ["Ahsoka Tano", "Kit Fisto"]:
    idx = jedi.search(name, "nombre")
    if idx is not None:
        print("-", jedi[idx])


# c) Padawan de Yoda y Luke Skywalker
print("c) Padawans de Yoda y Luke Skywalker:")
for maestro in ["Yoda", "Luke Skywalker"]:
    print(f"{maestro}:")
    for j in jedi:
        if maestro in j["maestros"]:
            print("  -", j["nombre"])


# d) Jedi humanos y twi'lek
print("d) Jedi humanos y twi'lek:")
for j in jedi:
    if j["especie"].lower() in ["humano", "twi'lek"]:
        print("-", j["nombre"], "(", j["especie"], ")")


# e) Jedi que comienzan con A
print("e) Jedi que comienzan con A:")
for j in jedi:
    if j["nombre"].startswith("A"):
        print("-", j["nombre"])


# f) Jedi con más de un color de sable
print("f) Jedi con más de un color de sable:")
for j in jedi:
    if len(j["sables"]) > 1:
        print("-", j["nombre"], "->", j["sables"])


# g) Jedi que usaron sable amarillo o violeta
print("g) Jedi con sable amarillo o violeta:")
for j in jedi:
    if "amarillo" in j["sables"] or "violeta" in j["sables"]:
        print("-", j["nombre"], "->", j["sables"])
        

# h) Padawans de Qui-Gon Jinn y Mace Windu
print("h) Padawans de Qui-Gon Jinn y Mace Windu:")
for maestro in ["Qui-Gon Jinn", "Mace Windu"]:
    print(f"{maestro}:")
    encontrados = False
    for j in jedi:
        if maestro in j["maestros"]:
            print("  -", j["nombre"])
            encontrados = True
    if not encontrados:
        print("  (sin padawans)")

