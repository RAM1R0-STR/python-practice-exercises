##Ejercicio 4: (3 puntos)
##Hacer un programa que dado un número entero n indique la cantidad mínima de términos necesarios para que la serie supere el número n. En esta serie cada término es la división entre un entero al azar (1,9) y los primeros impares, ver ejemplo:
##Ejemplo n=6
##La suma fue 6.303, hicieron falta 7 términos de la serie.

from random import*
def serie (n):
    suma = 0
    i = 1
    while suma <= n:
        numerador = randint (1,9)
        denominador = i*2-1
        term = numerador/denominador
        print (numerador,"/",denominador, end =" + ")

        i = i + 1
        suma = suma + term

    print("...\n")
    print("suma:", suma,"\ncantidad de terminos:", i)



serie(18)

