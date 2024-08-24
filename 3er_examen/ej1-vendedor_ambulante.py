# EXAMEN FINAL - EJERCICIO 1
# Buscamos implementar una aplicación que permita asignar a cada vendedor ambulante de una provincia los locales que deberá visitar. 
# Se puede conocer la dirección de cada vendedor y de cada local. El criterio para asignar los locales que debe visitar cada vendedor es que estén a una distancia 
# menor de 4 km del lugar de su residencia.

# Se dispone de las siguientes funciones:
    
# vendedores(provincia): devuelve la lista de vendedores de la provincia.
# obtenerUbicacion(local-Persona): devuelve la ubicación de la residencia del vendedor o del local.
# locales(provincia): devuelve la lista de locales que deben ser visitados.
# distancia(lugar1, lugar2): devuelve la distancia entre dos ubicaciones.
# envioLista(lista, persona): envía la lista de locales que le toca al vendedor.
# Hacer una función que reciba una provincia y envíe a cada vendedor la lista de locales que debe visitar.
# Observación: puede ocurrir que a un vendedor le toquen locales comunes a otro vendedor; no importa, igualmente deberá visitarlos.

#Asumo que la funcion distancia me devuelve el valor representado en kilometros
def ambulante_app(provincia):
    vendedores_provincia = vendedores(provincia)
    locales_provincia = locales(provincia)
    localesxVendedor = []
    for vendedor in vendedores_provincia:
        lugar_vendedor = obtenerUbicacion(vendedor)
        for local in locales_provincia:
            lugar_local = obtenerUbicacion(local)
            distancia = distancia(lugar_vendedor,lugar_local)
            if distancia <= 4:
                localesxVendedor.append(local)
        envioLista(localesxVendedor,vendedor)