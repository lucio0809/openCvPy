def obtener_valor_característica(características, buscada):
    for c in características:
        característica, puntaje = c
        if característica == buscada:
            return puntaje
    return 0

def puntaje_amigo(amigo, características):
    contador = 0
    nombre, característica = amigo
    for c in característica:
        contador += obtener_valor_característica(características, c)
    return contador

características = [
('kawaii',10), ('leal',20), ('acusete',-10), ('avaro',-15), ('respetuoso',20),
('otaku',25),('lolero',25),('furro',-50),('vtuver',25),('mechero',-30)
]

amigos = [('Sneki',('leal','kawaii','vtuver')),
          ('Otaku-taku',('otaku','avaro','lolero','leal')),
          ('Maiga',('paciente','otaku','leal')),
          ('Mojojojo',('mechero','kawaii','Furro','lolero')),
          ('Seiya',('leal','acusete')),
          ('Vegeta',('otaku','avaro')),
          ('Kalila',('lolero','kawaii')),
          ('Grogu',('avaro','kawaii','lolero','otaku')),
          ('Freezer',('acusete','furro','otaku','lolero'))
]

candidatos = []
filtro = []
borrar = []
seleccionado_1 = ""
puntaje_1 = 0
seleccionado_2 = ""
puntaje_2 = 0

for c in amigos:
    nombre, característica = c
    for i in característica:
        if i == "lolero":
            valor = puntaje_amigo(c, características)
            candidatos.append(nombre)
            candidatos.append(valor)
            filtro.append(candidatos)
            candidatos = []

for x in filtro:
    if x[1] > puntaje_1:
        puntaje_1 = x[1]
        seleccionado_1 = x[0]
          
borrar.append(seleccionado_1)
borrar.append(puntaje_1)
filtro.remove(borrar)

for y in filtro:
    if y[1] > puntaje_2:
        puntaje_2 = y[1]
        seleccionado_2 = y[0]

print("Equipo seleccionado:")
print(seleccionado_1 + "," ,puntaje_1,"puntos")
print(seleccionado_2 + ",",puntaje_2,"puntos")