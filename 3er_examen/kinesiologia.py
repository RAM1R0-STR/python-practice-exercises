pacientes = [1,2,3,4,5,6]

def pacientesConTurno(fecha):
    if fecha == 211013:
        pacientescTurno = (4,6,3)
        return pacientescTurno

def tieneCobertura(nroPaciente):
    pacientePrepaga = (4,6)
    for e2 in pacientePrepaga:
        if nroPaciente == e2:
            return True
    return False


def costoSesion():
    c = 5000
    return c

def sesionesUsadas(nroPaciente):
    nroSesiones = (1,4,12,20,2,7)
    for i in range(len(nroSesiones)):
        if nroPaciente == pacientes[i]:
            return nroSesiones[i]

def kinesiologia():
    fecha = 211013
    pacientescTurno = pacientesConTurno(fecha)
    pagan = []
    for i in range(len(pacientescTurno)):
        print (pacientescTurno[i])
        tof = tieneCobertura(pacientescTurno[i])
        if tof == False:
            c = costoSesion()
            pagan.append(c)
        else:
            c = costoSesion()
            nroSesiones_paciente = sesionesUsadas(pacientescTurno[i])
            if nroSesiones_paciente <=10:
                pagan.append(0)
            else:
                pagan.append(c/2)

    for i in range(len(pagan)):
        print("El paciente",pacientescTurno[i],"paga",pagan[i])

kinesiologia()