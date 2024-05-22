
horarios_disponibles = [
    {"fecha": "LUNES", "hora_inicio": "10:00", "hora_fin": "12:00"},
    {"fecha": "LUNES", "hora_inicio": "02:00", "hora_fin": "04:00"},
    {"fecha": "LUNES", "hora_inicio": "09:00", "hora_fin": "11:00"},
    
]


reserva = {}


def mostrar_horarios_disponibles():
    print("Horarios disponibles:")
    for i, horario in enumerate(horarios_disponibles, start=1):
        print(f"{i}. Fecha: {horario['fecha']}, Hora de inicio: {horario['hora_inicio']}, Hora de fin: {horario['hora_fin']}")

def reservar_horario():
    mostrar_horarios_disponibles()
    opcion = int(input("Selecciona el número de horario que deseas reservar: "))
    if opcion >= 1 and opcion <= len(horarios_disponibles):
        horario_seleccionado = horarios_disponibles[opcion - 1]
        reserva["fecha"] = horario_seleccionado["fecha"]
        reserva["hora_inicio"] = horario_seleccionado["hora_inicio"]
        reserva["hora_fin"] = horario_seleccionado["hora_fin"]
        print("Has realizado la reserva exitosamente.")
    else:
        print("Opción inválida.")

def realizar_pago():

    monto = float(input("Ingresa el monto a pagar: "))
    reserva["monto"] = monto
    print(f"Se ha realizado el pago exitosamente por un monto de {monto}.")

def verificar_alquiler():
    if reserva:
        print("Detalles de la reserva:")
        print(f"Fecha: {reserva['fecha']}")
        print(f"Hora de inicio: {reserva['hora_inicio']}")
        print(f"Hora de fin: {reserva['hora_fin']}")
        print(f"Monto pagado: {reserva['monto']}")
    else:
        print("No tienes ninguna reserva realizada.")

mostrar_horarios_disponibles()
reservar_horario()
realizar_pago()
verificar_alquiler()