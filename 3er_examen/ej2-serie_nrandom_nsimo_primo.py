# EXAMEN FINAL - EJERCICIO 2
# Hacer una función que reciba un entero n n y devuelva la suma de los primeros y devuelva la suma de los primeros n n términos de esta serie, también términos de esta serie, también
# debe realizar el programa principal que llama a esta función. debe realizar el programa principal que llama a esta función.
# La serie se caracteriza porque cada término es una fracción que alterna el signo donde el numerador La serie se caracteriza porque cada término es una fracción que alterna el signo donde el numerador a a es un es un
# número al azar entre 1 y 99 y el denominador es el número al azar entre 1 y 99 y el denominador es el a a-ésimo número primo, es decir -ésimo número primo, es decir, el denominador es un , el denominador es un
# número primo pero no cualquiera sino el que está en ese lugar si tuviéramos a los primos ordenados de menor a número primo pero no cualquiera sino el que está en ese lugar si tuviéramos a los primos ordenados de menor a
# mayor mayor.
#Los primos ordenados: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ...

import random

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

def serie(n):
    suma = 0
    for i in range(1,n):
        num = random.randrange(1,10)
        a= 0
        c = 0
        b = 1
        while a == 0:
            tof = Primos(b)
            if tof == True:
                c = c +1
                if c == num:
                    den = b
                    a=1
            b=b+1
        t = ((-1)**(i))*(num/den)
        #print((-1)**(i),"(",num,"/",den,")", end="  ")
        suma = suma + t
    return suma

def main():
    n = int(input("Ingresar cantidad de terminos: "))
    print("\nLa suma es: ",serie(n))

main()

