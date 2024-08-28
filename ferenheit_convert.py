#Crear una funcion que transforme grados Celsius en Fahrenheit y viceversa.
import pprint

def convert(T):
    num = ""
    res = 0
    for i in range(len(T)):
        if T[i] == "°":
            val = float(num)
            if T[i+1] == "C":
                print("val",val)
                res = val*1.8+32
                print("res",res)
            elif T[i+1] == "F":
                res = (val-32)/1.8
        num = num+T[i]
    if res == 0:
        print("Dato invalido")
        pass    
    else:
        return res


print(convert("75.2°F"))
        
#pprint.pprint(dir(""))
