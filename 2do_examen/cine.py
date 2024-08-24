Salas=[1,2,3,4,5,6]
Peliculas = [ "Xmen" ,"Titanic","Saw","Rio","Taxi Driver","Avatar"]
Capacidad=[80,70,60,75,40,90]

def cine (Capacidad):
    peliVer = input("Ingresar Pelicula a Ver: ")
    if peliVer in Peliculas:
        cantVer = int(input("Ingresar la cantidad de Personas: "))
    else:
        print("No se encuentra la Pelicula")
        cine(Capacidad)
    for i in range(0,len(Peliculas)):
        if peliVer == Peliculas[i]:
            eleccion = i
    if Capacidad[eleccion] >= cantVer:
        Capacidad[eleccion] = Capacidad[eleccion] - cantVer
        print("Debe dirigirse a la sala", Salas[eleccion],"para la pelicula",Peliculas[eleccion])
        return Capacidad
    else:
        print("No hay Capacidad Suficiente en la Sala")

print(cine(Capacidad))

