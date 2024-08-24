##Realizar un programa que dado un número, indique si este es un número Perfecto.
##Aclaración: Por definición, un número Perfecto es un entero positivo que es igual a la suma de todos sus divisores positivos (Excepto si mismo).
##
##Ejemplos:
##10 no es Perfecto, sus divisores (sin incluirlo) son 1 2 5 que suman 7 y no 10.
##6 es Perfecto, sus divisores (sin incluirlo) son 1 2 3 que suman 6.

numero = int(input("Ingresar numero: "))
suma = 0

for i in range(1,numero-1):
    if numero%i == 0:
        suma = suma + i

if suma == numero:
    print ("El numero", numero, "es perfecto")
else :
    print ("El numero", numero, "no es perfecto")
    
def num_perfectoEntntre(n_desde,n_hasta):
    suma = 0

    print ("Los Numeros Perfectos entre",n_desde,"y",n_hasta,"son:")
    for n in range(n_desde,n_hasta):
        for i in range(1,n-1):
            if n%i == 0:
                suma = suma + i
        if suma == n:
            print (n)
        n = n + 1
        suma = 0
        
num_perfectoEntntre(1, 100)