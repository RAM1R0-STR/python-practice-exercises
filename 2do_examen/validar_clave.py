# Ejercicio 3: (3 puntos)
# Las contraseñas son las herramientas más utilizadas para restringir el acceso a los sistemas informáticos. Sin embargo, sólo 
# son efectivas si se definen con criterios y se exige cambiarlas periódicamente. Se considera un buen 
#
#  criterio si se combinan letras, números y símbolos. 
# Se desea definir una función  validarClave  que recibe una cadena como contraseña/clave y 
# que retorne un valor True si cumple los criterios enunciados a continuación y que retorne un valor False en caso contrario.
# Considera que cuenta con las siguientes listas:
# Se deben tener en cuenta los siguientes criterios:
# Las contraseñas deben tener 8 caracteres o más.
# Las contraseñas deben contener números, letras, y caracteres especiales.


lisNum=["0","1","2","3","4","5","6","7","8","9"]
lisLetMin=["a","b","c","d","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 
lisLetMay=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lisCaract=["¡","!","-","_","¿","?"]

def ValidarClave(cv):
    contNum = 0
    contMin = 0
    contMay = 0
    contChar = 0
    if len(cv) >= 8:
        for elem in cv:
            if elem in lisNum:
                contNum = contNum + 1
            if elem in lisLetMin:
                contMin = contMin + 1
            if elem in lisLetMay:
                contMay = contMay +1
            if elem in lisCaract:
                contChar = contChar + 1
        if contNum !=0 and contMin != 0 and contMay !=0 and contChar !=0:
            return True
        else:
            return False
    else:
        return False

# Ejemplo de contraseñas invalidas:
# PapasFritas_
# ¿River-o-Boca?
# AAA1234

# Ejemplo de contraseñas validas:
# UnGs_2015
# Conocido?129

print(ValidarClave("Conocido?129"))


    


         