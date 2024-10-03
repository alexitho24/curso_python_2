# ejercicio 01
#crear una clase banco
#sus atributos seran nombre, apellido, dni, numero de cuenta y saldo inicial

# como metodos podremos hacer deposito retirar dinero y ver estado de cuenta

# class Banco:
#     def __init__(self, nombre, apellido, dni, numero_cuenta, saldo_inicial):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.dni = dni
#         self.numero_cuenta = numero_cuenta
#         self.saldo = saldo_inicial

#     def depositar(self, monto):
#         self.saldo += monto
#         print(f"Se ha depositado {monto}. Saldo actual: {self.saldo}")

#     def retirar(self, monto):
#         if monto > self.saldo:
#             print("Fondos insuficientes.")
#         else:
#             self.saldo -= monto
#             print(f"Se ha retirado {monto}. Saldo actual: {self.saldo}")

#     def mostrar_estado_cuenta(self):
#         print(f"Nombre: {self.nombre} {self.apellido}")
#         print(f"DNI: {self.dni}")
#         print(f"Número de cuenta: {self.numero_cuenta}")
#         print(f"Saldo: {self.saldo}")



#ejercicio 02
#crear una clase agencia 
# con sus atributos nombre y apellidos del pasajero, dni, numero de asiento
# sus metodos seran origen , ingresar, destino, cancelar viaje , ver estado de pasaje



class Agencia:
    def init(self,nombre,apellido,dni,numero_asiento,fecha_viaje):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.numero_asiento=numero_asiento
        self.fecha_viaje=fecha_viaje
    
    def origen(self,lugar):
        print("ingresa origen: ", lugar)
    def destino(self,lugar):
        print("ingrese destino: ", lugar)
    def cancelar_viaje(self):
        print("viaje cancelado")
    def estado_viaje(self):
        print("ver su estado de viaje: ")

alex=Agencia()
alex.estado_viaje()
alex.origen("puquio")
alex.destino("lima")
alex.cancelar_viaje()

