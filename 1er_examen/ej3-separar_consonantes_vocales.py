##Ejercicio 3: (3 puntos)
##Hacer un programa que solicite al usuario una frase y acumule las consonantes
##por la izquierda y las vocales por la derecha para cada palabra de la frase.
##Por ejemplo:
##Entrada: un lunes lluvioso Salidas posibles: nu lnsue llvsuioo
##nu snlue svlluioo

def ordenar_pal(pal):
    pal_der=""
    pal_izq=""
    vocales = "aeiou"
    for char in pal:
        if char in vocales:
            pal_der = pal_der + char
        else :
            pal_izq = pal_izq + char
    pal_ord =pal_izq+pal_der
    return pal_ord

word ="un lunes lluvioso"
pal_u =""
c = 0
frase =""
cont = 0

for char in word:
    cont = cont +1
    if char == chr(32):
        frase =frase + " " + ordenar_pal(pal_u)
        pal_u=""
    else:
        pal_u = pal_u +char
    if cont == len(word):
        frase =frase + " " + ordenar_pal(pal_u)

print(frase)