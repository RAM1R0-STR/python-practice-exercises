##Cadenas – Generar claves
##Hacer un programa que genere claves provisorias para cada usuario, siguiendo
##las siguientes reglas:
##Longitud 8 caracteres, formada por la primera letra del nombre + las 3 últimas
##cifras del año de nacimiento + las consonantes del apellido hasta completar la
##longitud de la clave; si no llega a la longitud, completar con “A” (letras A).
##Ejemplo: Juan Fernandez 2003 CLAVE: J003frnn

nombre = input ("nombre")
apellido = input("apellido")
nacimiento = input ("año de nacimiento")

clave = ""

while len(clave) <= 8:
    for char1 in nombre:
        if len(nombre) <= 1:
            clave = char1

nac2 = ""
for char2 in nacimiento:
    nac2 = nac2 + char2
    if len(nac2) > len(nacimiento)-3:
        clave = clave + char2

for char3 in apellido:
    if char3 != "a" and "e" and "i" and "o" and "u":
        clave = clave + char3

if len(clave) < 8:
    while len(clave) < 8:
        clave = clave + "A"
    print (clave)
else:
    print (clave)

