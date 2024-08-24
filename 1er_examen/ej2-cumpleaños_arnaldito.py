##Ejercicio 2: (3 puntos)
##Arnaldito quiere festejar su cumpleaños cenando con sus amigos, democráticamente la cena será elegida por
##los amigos entre pizzas o empanadas, de pizzas “Al Toke”. Tanto si la mayoría desea pizzas o empanadas
##siempre que alcance prefieren las más caras. Se estima que cada hombre come 4 porciones de pizzas y cada
##mujer 2 y en caso de empanadas los hombres 6 y las mujeres 4. Se debe indicar en cada caso cual fue el costo
##de la comida y cuanto dinero sobró, solo en el caso de que no les alcance el dinero Arnaldito pedirá a sus
##padres el resto. Nota: Cuando piden pizzas, serán todas del mismo estilo (todas especial o todas seleccionada
##o todas muzzarella)
##Los precios de los estilos que maneja la pizzería “Al Toke” son:
##especial= 170 #8 porciones
##seleccionada= 140 #8 porciones
##muzzarella= 100 #8 porciones
##empandas= 90 #la docena
##Continuar el programa:
precio_esp = 170
precio_selec = 140
precio_muzza = 100

cantHombres = int(input("Indique la cantidad de hombres de la fiesta: "))
cantMujeres=int(input("Indique la cantidad de mujeres de la fiesta: "))
dineroDisponible= int(input("Indique el dinero recaudado: "))
eleccion=int(input("Indique 0 si la mayoria selecciono pizzas o 1 si la mayoria eligio empanadas: "))

def empanadas (h,m,d):
  emp = h*6 + m*4
  docena = emp//12
  empanadas= 90
  if docena*empanadas <=d :
   precio = docena*empanadas
   print("Pago", precio, "por decenas", docena)

  else:
    precio = docena*empanadas
    faltante = precio - d
    print("Se pide", faltante, "...")

  print("Debe abonar: ", precio)


def pizzas (h,m,d):
    porciones = h*4 + m*2
    cantpiz = porciones//8
    if cantpiz*precio_esp <= d:
        pagar = cantpiz*precio_esp
    elif cantpiz*precio_selec <= d:
        pagar = cantpiz*precio_selec
    elif cantpiz*precio_muzza <= d:
        pagar = cantpiz*precio_muzza
    else:
        faltante = cantpiz*precio_muzza - d
        print ("Se piden", faltante,"a los padres de Arnaldito")
        pagar = cantpiz*precio_muzza
    print("El monto a pagar es",pagar,"para", cantpiz,"de pizzas.")

if eleccion == 0:
    pizzas (cantHombres,cantMujeres,dineroDisponible)
elif eleccion == 1:
    empanadas (cantHombres,cantMujeres,dineroDisponible)




