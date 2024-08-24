##Escribir una función esPuntoValido(coeficienteLineal, ordenadaAlOrigen, coordX, coordY).
##La función lineal sería f(x) = a x + b que recibe el coeficiente del término lineal (a)
##y la ordenada al origen (b), y las coordenadas (x, y) de un punto, y devuelve True si dicho
##punto pertenece a la función; False, en caso contrario. Un punto pertenece si a x + b = y
##Además, se debe elaborar un programa principal que indique un mensaje de pertenencia (o no)
##del punto recibido al usuario.

def esPuntoValido(coeficienteLineal, ordenadaAlOrigen, coordX, coordY):
    if coeficienteLineal*coordX + ordenadaAlOrigen == coordY:
        return True
    else:
        return False

def analisisLineal(coeficienteLineal, ordenadaAlOrigen, coordX, coordY):
    tof = esPuntoValido(coeficienteLineal, ordenadaAlOrigen, coordX, coordY)
    if tof == True:
        print("El punto PERTENECE a la funcion")
    else:
        print("El punto NO PERTENECE a la funcion")

analisisLineal(2,3,1,5)

