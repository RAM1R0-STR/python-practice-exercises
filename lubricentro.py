##Un lubricentro desea automatizar su software de gestión para controlar los cambios de aceite de sus clientes.
##Actualmente, el local cuenta con el siguiente listado de clientes recurrentes:
##Se solicita:
##a) Hacer una función que reciba un ID de cliente y muestre su historial de asistencia: vehículo,
##último y próximo service (valores expresados en KMs).
##b) Realizar un programa principal que permita al usuario tomar un service para su vehículo.
##En dicho caso, el operador deberá contar con el kilometraje actual y se deberán
##actualizar los listados correspondientes.
##Considerar que los cambios de aceite se realizan cada 10.000 KM.

ids_clientes_recurrentes = [144, 133, 122, 148, 999]
vehiculos = ["Volkswagen Up! 1.0 Take 2021", "Ford Focus 2.0 Se Plus At 2019", "Toyota Etios 1.5 Xls At 2020", "Kia Sportage Lx 2.0 At 2020", "Chevrolet Onix Joy 1.4 Af 2021"]
ultimo_service = [10000, 56875, 35000, 49587, 12500]
proximo_service = [20000, 66875, 45000, 59587, 22500]

def lubricentro(ids_clientes_recurrentes,vehiculos,ultimo_service,proximo_service):
    opcion = input("Opcion A: Historial de Asistencia \nOpcion B:Registrar nuevo Service\n ")
    if opcion.lower() == "a":
        idCliente = int(input("ID del Cliente: "))
        for i in range(0,len(ids_clientes_recurrentes)):
            if idCliente == ids_clientes_recurrentes[i]:
                print("CLIENTE:",idCliente,"\nVEHICULO:",vehiculos[i])
                print("Realizo el ultimo service a los",ultimo_service[i],"kMs","y el proximo service es a los",proximo_service[i],"kMs")
    elif opcion.lower() =="b":
        opcion2 = input("Cliente NUEVO?: Escriba SI o NO")
        if opcion2.lower() == "si":
            idClienteNuevo = int(input("ID del Cliente Nuevo: "))
            vehiculoNuevo = input("Vehiculo del cliente: ")
            ultimoServiceNuevo = int(input("Ingresar ultimo service del vehiculo: "))
            ids_clientes_recurrentes.append(idClienteNuevo)
            vehiculos.append(vehiculoNuevo)
            ultimo_service.append(ultimoServiceNuevo)
            proximo_service.append(ultimoServiceNuevo+10000)
        elif opcion2.lower() == "no":
            idCliente = int(input("ID del Cliente: "))
            for i in range(0,len(ids_clientes_recurrentes)):
                if idCliente == ids_clientes_recurrentes[i]:
                    print("El ultimo Service del Cliente",idCliente,"fue a los",ultimo_service[i],"kMs","y el proximo deberia ser a los",proximo_service[i],"kMs")
                    kMsActual = int(input("Ingresar el Kilometraje Actual del Vehiculo: "))
                    ultimo_service[i] = kMsActual
                    proximo_service[i] = ultimo_service[i] + 10000
        return ids_clientes_recurrentes, vehiculos,ultimo_service, proximo_service


print(lubricentro(ids_clientes_recurrentes,vehiculos,ultimo_service,proximo_service))