# Se tienen tres listas para representar productos de almacÃ©n:
# Nombres, Precios, Cantidad
# Las tres listas se corresponden, en el sentido en que la misma posiciÃ³n en las tres listas hablan del nombre, precio y 
# cantidad del mismo producto. La lista de precios estÃ¡ ordenada de menor a mayor, por ejemplo:
# precios=[30, 50, 65, 70, 99]
# productos=["Harina", "arroz", "fideos", "manteca", "leche"]
# cantidad = [4, 5, 12, 7, 8]
# Hacer un programa que, dado un producto ingresado por el usuario, imprima todos 
# los productos con sus cantidades que valgan menos que el producto ingresado. Por ejemplo, si el usuario ingresa "manteca" el programa debe mostrar:
# Harina : 4
# arroz: 5
# fideos : 12
# Y si ingresa "Harina" no muestra nada, porque no hay nada mÃ¡s barato. 
# Si el producto ingresado no existe tiene que imprimir "El producto ingresado no existe", 
# pueden asumir que las listas tienen al menos un elemento.


precios =[30,50,65,70,99]
productos = ["harina","arroz","fideos","manteca","leche"]
cantidad = [4,5,12,7,8]

def compra(precios,productos,cantidad):
    prod_us = input("Ingresar el Producto a comprar: ")
    c = 0
    for i in range(0,len(productos)):
            if productos[i] == prod_us:
                n=0
                while n < len(precios):
                    if i != n:
                        if precios[n] <= precios[i]:
                            print (productos[n],":",cantidad[n])
                    n = n+1

compra(precios,productos,cantidad)