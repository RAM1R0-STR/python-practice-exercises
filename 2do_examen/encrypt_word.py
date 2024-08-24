 # Ejercicio 3: (2.5 puntos)
# Hacer una programa que dada una palabra encriptada y una clave encuentre el texto oculto.
# La palabra encriptada es creada (por el emisor) sumando las posiciones de cada 
# letra en el abecedario del texto oculto y la clave, es decir, 
# para encontrar el Texto Oculto (el receptor) debe restar la Palabra Encriptada con la Clave. 
# Las letras son 26, si la suma supera este valor se inicia nuevamente desde 1.

# Palabra Encript 	DIOSES	    4  9   15   19   5  19
# Clave: 			BTBQDZ	        2  20  2    17   4  26
# Texto Oculto:		BOMBAS	        2  15  13   2    1  19


abcd=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def Krypto(clave,palabra):
    loculto = []        
    lclave = []
    lpalabra = []
    lkrypt = []
    pkrypt = 0
    cod = ""     
    for pc in clave:
        pclave = posicion(pc)
        lclave.append(pclave)
    for pp in palabra:
        ppalabra = posicion(pp)
        lpalabra.append(ppalabra)
    for i in range(0,len(clave)):
        pkrypt = lpalabra[i] - lclave[i]
        h = absoluto(lclave[i]-26) + lpalabra[i]
        if h>=26:
            lkrypt.append(pkrypt)
        else:
            pkrypt = h
            lkrypt.append(pkrypt)
    for pk in lkrypt:
        poculto = letra(pk)
        loculto.append(poculto)
        cod = cod + poculto
    return cod

def letra(p):
    abcd=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    c = 1
    for u in abcd:
        if c == p:
            return u
            break
        c = c + 1

def posicion(l):
    abcd=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    l = l.upper()
    cont = 1
    for char in abcd:
        if char == l:
            return cont
            break
        else:
            cont = cont +1

def absoluto (n):
    if n <=0:
        n =(-1)*n
    return n

x = input("Ingresar Palabra Enscriptada: ")
print("El Texto Oculto es:", Krypto("BTBQDZ",x))