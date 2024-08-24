##Hacer una función que reciba 2 números enteros a y b que definen el intervalo (a,b)
##y devuelva el producto de los primos del intervalo.
##
##Por ejemplo, si recibe 6 y 15 debe devolver 1001 (7*11*13)

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

def Multip_Primos (a,b):
    multip = 1
    for i in range(a,b+1,1):
        tof = Primos(i)
        if tof == True:
            multip = multip*i
    return multip

print(Multip_Primos(6,15))
