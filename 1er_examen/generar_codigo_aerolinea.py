##Aerolínea, código
##En las pantallas de Partidasy Llegadas de vuelos de los aeropuertos, se asigna una abreviatura a cada
##vuelo compuesta por dos letras que identifican a cada aerolínea. Se le pide codificar la determinación de la
##abreviatura correspondiente a cada aerolínea respetando las siguientes pautas:
##Ambas letras se muestran en mayúsculas.
##Si el nombre de la aerolínea es una sola palabra la abreviatura se formará con la primera letra más la
##siguiente consonante.
##Si el nombre de la aerolínea consta de dos palabras, la abreviatura se formará con la primera letra de
##cada palabra.
##Ejemplos: Aerolíneas  AR
##Emirates  EM
##TAM  TM Gol GL
##IBERIA  IB
##Ejemplos: Air France  AF
##American Airlines  AA
##United Airlines  UA
##El programa deberá solicitar el ingreso del nombre de la aerolínea y mostrar la abreviatura generada.

nb = input("Nombre de la aerolinea: ")

clas = "1p"
codigo = ""

for le in nb:
    if le == chr(32):
        clas = "2p"
##print(clas)

if clas == "1p":
    for char2 in nb:
        if len(codigo) == 1:
            if char2 !="a" and char2 !="e" and char2 !="i" and char2 !="o" and char2 !="u":
                codigo = codigo + char2
##                print("2",codigo)

        while len(codigo) < 1:
            codigo = codigo + char2
##            print("1",codigo)

cont= 0
if clas == "2p":
    for char3 in nb:
        if cont == 1:
            codigo = codigo + char3
            cont = cont + 1
        while len(codigo) < 1:
            codigo = codigo + char3
        if char3 == chr(32):
            cont = cont + 1

print (codigo.upper())












