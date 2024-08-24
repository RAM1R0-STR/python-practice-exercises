def moda(l):
    cmax = 0
    c = 0
    repe = []
    for i in range(0,len(l)):
        actual = l[i]
        if actual in repe:
            b = 2 +2 
        else:
            repe.append(l[i])
            for a in l:
                if actual == a:
                    c = c + 1
        if cmax >=c:
            mayor = actual
            c = 0
        else:
            cmax = c
            c = 0
    pos = posicion(mayor,l)
    print("El valor",mayor,"aparece",cmax,"veces","\nEn las posiciones:",pos)

def posicion(n,l):
    lpos = []
    for i in range(0,len(l)):
        if n == l[i]:
            lpos.append(i)
    return lpos

lista = (2,4,5,8,2,8,2,2,8,7,4,2,8,2,7,8,1,2,1,2)
moda (lista)
