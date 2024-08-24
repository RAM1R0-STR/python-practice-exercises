##Palabras esdrújulas: son las que están acentuadas en la antepenúltima sílaba y se escriben con tilde.
##Hacer una función llamada esEsdrujula(palabra), que reciba una palabra y retorne True si lo es, y False en caso contrario.
##Se dispone (no hay que programarla) de una función llamada enSilabas(palabra) que recibe una palabra y la devuelve
##separada en silabas por medio de guiones (-).
##Ejemplos:
##enSilabas("murciélago") ==>> devuelve "mur-cié-la-go"
##esEsdrujula("murciélago") ==>> devuelve True
##esEsdrujula("programación") ==>> devuelve False
##esEsdrujula("sol") ==>> devuelve False
##esEsdrujula("determinante") ==>> devuelve False
##esEsdrujula("atrápamelo") ==>> devuelve False

def Enlistar(word):
    lista = []
    for char in word:
        lista.append(char)
    return lista

def esEsdrujula (word):
    tildes = ["á","é","í","ó","ú"]
    silaba = ""
    word = "-" + word
    cont = 0
    #wordSep = esSilabas(word)
    wordSep_list = Enlistar(word)
    for i in range(len(wordSep_list)-1,0,-1):
        if wordSep_list[i] == "-":
            cont = cont + 1
        else:
            silaba = silaba + wordSep_list[i]
            if cont == 2:
                for char in silaba:
                    if char in tildes:
                        return True
            else:
                silaba = ""

print(esEsdrujula("mur-cié-la-go"))