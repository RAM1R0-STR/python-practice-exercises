# Ejercicio 1: (3 puntos)
# Hacer una función que dado un entero n indique cuantos primos hacen falta sumar para superar dicho n. Por ejemplo: si n=15 hacen falta 4 primos (2,3,5,7) 

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

def faltanPrimos(n):
    suma = 0
    i = 0
    while suma <= n:
        tof = Primos(i)
        if tof == True:
            suma = suma + i
            print (i)
        i = i +1
    print("suma:", suma)

faltanPrimos(500)