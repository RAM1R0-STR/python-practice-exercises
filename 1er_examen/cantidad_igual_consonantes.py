##Igual cant consonantes
##Hacer un programa que solicite el ingreso de 2 palabras distintas y determine
##si ambas tienen igual cantidad de consonantes.
##Ejemplo:
##“murcielago” y “elefante”, NO tienen igual cantidad de consonantes.
##“pato” y “rana”, SI tienen igual cantidad de consonantes.

pb1 = input("palabra 1")
pb2 = input("palabra 2")

cont1 = 0
cont2 = 0

for char1 in pb1 :
    if char1 !="a" and char1 !="e" and char1 !="i" and char1 !="o" and char1 !="u":
        cont1 = cont1 + 1

for char2 in pb2:
    if char2 !="a" and char2 !="e" and char2 !="i" and char2 !="o" and char2 !="u":
        cont2 = cont2 + 1

if cont1 == cont2 :
    print ("Tienen igual cantidad de consonantes")
else:
    print("No tienen igual cantidad de consonantes")

##print (pb1,"tiene",cont1 ,"\n",pb2,"tiene", cont2)