def Primos(n):
    cont = 0
    for i in range(1,n+1,1):
        div = n%i
        if div == 0:
            cont = cont + 1
    if cont == 2:
        return True
    else:
        return False

def extraerPrimosPorCantidad(numero,n):
    primos = ""
    numeroStr = str(numero)
    for numStr in numeroStr:
        numInt = int(numStr)
        tof = Primos(numInt)
        if tof == True:
            if len(primos) < n:
                primos = primos + numStr
    return primos

def extraerPrimosPorIntervalo(a,b):
    for i in range(a,b):
        primos = extraerPrimosPorCantidad(i,2)
        strPrimos = str(primos)
        if len(primos) == 2 and strPrimos[0] != strPrimos[1]:
            print(primos)

##print(extraerPrimosPorCantidad(12345,2))
extraerPrimosPorIntervalo(1,100)
