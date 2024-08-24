# Escribir un programa que calcule el valor de la siguiente suma de n términos, teniendo en cuenta que n
# es un número natural introducido por el usuario. (Controlar el valor de n que ingresa el usuario)
# 1/2**1 + 2/2**1 + 3/2**2 + 4/2**2 + 5/2**1 + 6/2**1 + 7/2**2 + 8/2**2+...


def serie (n):
    suma = 0
    cont = 0
    for i in range(1,n+1,1):
        if cont <2:
            cont = cont + 1
            term = i/((2)**1)
            print (term, end=" + ")
            suma = suma + term
        elif cont < 4:
            cont = cont + 1
            term = i/((2)**2)
            print (term, end=" + ")
            suma = suma + term
        else:
            cont = 0
    print("...")
    print ("suma:", suma)
serie(8)
