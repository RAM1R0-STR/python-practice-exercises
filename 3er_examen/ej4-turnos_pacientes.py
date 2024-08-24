# EXAMEN FINAL - EJERCICIO 4
# Una empresa de salud regional debe asignar turnos a los pacientes, estos eligen un horario y el programa debe Una empresa de salud regional debe asignar turnos a los pacientes, estos eligen un horario y el programa debe
# buscar dentro de las clinicas de la region alguna que tenga disponibilidad, de todas las disponibles debe buscar dentro de las clinicas de la region alguna que tenga disponibilidad, de todas las disponibles debe
# seleccionar una al azar e informarle al paciente. Lo contratan a usted y para resolverlo cuenta con las seleccionar una al azar e informarle al paciente. Lo contratan a usted y para resolverlo cuenta con las
# siguientes siguientes funciones funciones: :
# pacientes(): devuelve una lista de pacientes pacientes(): devuelve una lista de pacientes
# clinicas(): devuelve una lista de clinicas de la region clinicas(): devuelve una lista de clinicas de la region
# horarioPaciente(paciente): devuelve el horario elegido por el paciente. horarioPaciente(paciente): devuelve el horario elegido por el paciente.
# disponibilidad(clinica, horario): devuelve disponibilidad(clinica, horario): devuelve T True si la clinica tiene en el horario disponibilidad rue si la clinica tiene en el horario disponibilidad
# unoAlazar(lista): devuelve un elemento al azar de una lista

def turnos():
    pacientes_activos = pacientes()
    clinicas_region = clinicas()
    clinicas_disponibles = []
    for i in range(len(pacientes_activos)):
        paciente = pacientes_activos[i]
        horario = horarioPaciente(paciente)
        for clinica in clinicas_region:
            tof = disponibilidad(clinica,horario)
            if tof == True:
                clinicas_disponibles.append(clinica)
        clinica_asignada = unoAlazar(clinicas_disponibles)
        return clinica_asignada, paciente
    
def turnos(paciente):
    pacientes_activos = pacientes()
    clinicas_region = clinicas()
    clinicas_disponibles = []
    if paciente in pacientes_activos:
        horario = horarioPaciente(paciente)
        for clinica in clinicas_region:
            tof = disponibilidad(clinica,horario)
            if tof == True:
                clinicas_disponibles.append(clinica)
    clinica_asignada = unoAlazar(clinicas_disponibles)
    return clinica_asignada

#----------------------------------------------------------------------------------------------------------------------------------------
# Aclaracion:
# no entendia bien la consigna, si el programa es usado por un usuario para encontrar turnos de un paciente dado
# o es una forma automatizada de buscarle turnos a todos los pacientes, por lo que lo hice de ambas formas