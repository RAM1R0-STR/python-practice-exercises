#Este programa hace que el usuario mueva un dron con las teclas 8 (arriba), 4 (izquierda), 2 (abajo) y 6 (derecha).
#Calculando la distancia a la antena y terminando el programa cuando el dron se va de rango.

import math
import numpy

ant1 = [1,7,5]
ant2 = [5,5,5]
ant3 = [30,18,5]
ant4 = [40,15,5]
ant0 = [12,50,5]

def señalSOS(posicion):
    print("SE PERDIO LA SEÑAL, LA ULTIMA POSICION FUE (X,Y,Z):",posicion)
    return

def desactivarTransmision():
    print("Desactivar Transmision")
    return

def activarTransmision(posicion, AntenaCerca):
    print("TRANSMITIENDO DATOS DE LA POSICION:",posicion,"A LAS ANTENAS",AntenaCerca)
    return

def corrigeElevacion(posicion):
    if posicion[2] > 75:
        print("Se supero la altura limite:",posicion[2]-75,"\nRecupera la posicion 75")
        posicion[2] = 75
    elif posicion [2]<50:
        print("Se corrige la altura minima:",50 - posicion[2],"\nRecupera la posicion 50")
        posicion[2] = 50
    return posicion

def manejo(posicion):
    a = True
    opcion = ""
    while a == True:
        opcion = input("Eje X:4 6 / Eje Y:8 2 / Eje Z:+ -")
        for op in opcion:
            if op == "8":
                posicion[1] = posicion[1] + 1
            if op== "2":
                posicion[1] = posicion[1] -1
            if op == "4":
                posicion[0] = posicion[0] -1
            if op =="6":
                posicion[0] = posicion[0] +1
            if op == "-":
                posicion[2] = posicion[2] -1
            if op == "+":
                posicion[2] = posicion[2] +1
        a = False
    return posicion

def antenasCercanas(posicion):
    distEje1 = [0,0,0]
    distEje2 = [0,0,0]
    distEje3 = [0,0,0]
    distEje4 = [0,0,0]
    distEje0 = [0,0,0]
    for i in range (0,len(ant1)):
        distEje1[i] = abs(ant1[i]-posicion[i])
    dist1 = math.sqrt((ant1[0]-posicion[0])**2+(ant1[1]-posicion[1])**2+(ant1[2]-posicion[2])**2)
    for i in range (0,len(ant2)):
        distEje2[i] = abs(ant2[i]-posicion[i])
    dist2 = math.sqrt((ant2[0]-posicion[0])**2+(ant2[1]-posicion[1])**2+(ant2[2]-posicion[2])**2)
    for i in range (0,len(ant3)):
        distEje3[i] = abs(ant3[i]-posicion[i])
    dist3 = math.sqrt((ant3[0]-posicion[0])**2+(ant3[1]-posicion[1])**2+(ant3[2]-posicion[2])**2)
    for i in range (0,len(ant4)):
        distEje4[i] = abs(ant4[i]-posicion[i])
    dist4 = math.sqrt((ant4[0]-posicion[0])**2+(ant4[1]-posicion[1])**2+(ant4[2]-posicion[2])**2)
    for i in range (0,len(ant0)):
        distEje0[i] = abs(ant0[i]-posicion[i])
    dist0 = math.sqrt((ant0[0]-posicion[0])**2+(ant0[1]-posicion[1])**2+(ant0[2]-posicion[2])**2)
    distAntenas = [dist0, dist1, dist2, dist3, dist4]
    distAntenas2 = [dist0, dist1, dist2, dist3, dist4]
    DistAntenaCerca = []
    AntenaCerca = []
    for i in range(0,3):
        temp = min(distAntenas2)
        temp1 = numpy.argmin(distAntenas2)
        DistAntenaCerca.append(temp)
        for i in range (0,len(distAntenas)):
            if temp == distAntenas[i]:
                AntenaCerca.append(i)
        distAntenas2.pop(temp1)
    print("POSICION DRON = ", posicion,"\nANTENAS CERCA = ",AntenaCerca,"DISTANCIA = ",DistAntenaCerca)
    return AntenaCerca, DistAntenaCerca

def controlDeVuelo(posicion):
    a = True
    while a == True:
        posicion = manejo(posicion)
        (AntenaCerca,DistAntenaCerca) = antenasCercanas(posicion)
        if posicion[2] > 75 or posicion[2] <50:
            posicion = corrigeElevacion(posicion)
        for distancia in DistAntenaCerca:
            if distancia > 70:
                desactivarTransmision()
                señalSOS(posicion)
                break
                a = False
        activarTransmision(posicion, AntenaCerca)

controlDeVuelo([4,5,60])


