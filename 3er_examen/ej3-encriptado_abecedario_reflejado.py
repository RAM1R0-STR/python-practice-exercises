# EXAMEN FINAL - EJERCICIO 3
# Método de encriptado de abecedario reflejado. Método de encriptado de abecedario reflejado.
# Este método consiste en dividir el abecedario por la mitad y reemplazar cada letra de un mensaje 
# con la que Este método consiste en dividir el abecedario por la mitad y reemplazar cada letra de un mensaje con la que
# ocupa la misma posición en la otra mitad. ocupa la misma posición en la otra mitad.
# Define las siguientes Define las siguientes funciones funciones: :
# cadena_a_lista(cadena): para ingresar la cadena abc y obtener la lista abecedario. No se puede usar 
# LIST cadena_a_lista(cadena): para ingresar la cadena abc y obtener la lista abecedario. No se puede usar LIST ni ni
# ninguna otra función provista por Python. ninguna otra función provista por Python.
# indice(cadena, caracter): que retorne el índice que corresponde al caracter dentro de la cadena 
# (no importa si indice(cadena, caracter): que retorne el índice que corresponde al caracter dentro de la cadena (no importa si
# está repetido y devuelve la primera o la última posición: en "anana" se repite "a" y "n" para "a", que devuelva 0; 
# está repetido y devuelve la primera o la última posición: en "anana" se repite "a" y "n" para "a", que devuelva 0;
# 2 ó 4 es irrelevante porque se usará para buscarla en el abecedario). No se puede usar INDEX ni ninguna otra 2 ó 4 es irrelevante 
# porque se usará para buscarla en el abecedario). No se puede usar INDEX ni ninguna otra función provista por Python. 
# Se permite el uso de la función len(…) y los métodos upper() y lower() función provista por Python. Se permite el uso de la 
# función len(…) y los métodos upper() y lower().
# De la lista abecedario deberás generar las De la lista abecedario deberás generar las listas listas abcde_1 con los 13 primeros elementos 
# de abecedario, y abcde_1 con los 13 primeros elementos de abecedario, y abecde_2 con los restantes. Codifica el programa principal
# para que solicite un texto por teclado y muestre el abecde_2 con los restantes. Codifica el programa principal para que solicite un texto por teclado y muestre el 
# texto cifrado. texto cifrado.
# Reemplaza los " " (espacios) por ":" Reemplaza los " " (espacios) por ":"
# Ejemplo: abc = 'abcdefghijklmnopqrstuvwxyz' Ejemplo: abc = 'abcdefghijklmnopqrstuvwxyz'
# abcde_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'] abcde_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
# abcde_2 = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] abcde_2 = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# Mensaje -> ‘hola cristina’ Mensaje -> ‘hola cristina’ Cifrado -> ‘ubyn:pevfgvan’

abc = "abcdefghijklmnopqrstuvwxyz"

def cadena_a_lista(cadena):
    list = []
    for element in cadena:
        list.append(element)
    return list

def indice(cadena,caracter):
    cad_list = cadena_a_lista(cadena)
    for i in range(len(cad_list)):
        if cad_list[i] == caracter:
            return i

def cifrado():
    cadena = input("Ingresar Texto: ")
    abc_list = cadena_a_lista(abc)
    abcde_1 = abc_list[:(len(abc_list)//2)]
    abcde_2 = abc_list[(len(abc_list)//2):len(abc_list)]
    cod = ""
    for element in cadena:
        pos = indice(abc,element)
        if element == " ":
            cod = cod + ":"
        else:
            if pos < (len(abc_list))//2:
                cod = cod + abcde_2[pos]
            else:
                cod = cod + abcde_1[pos-(len(abc_list)//2)]
    return cod

print(cifrado())