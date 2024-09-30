#crear una clase banco
#sus atributos seran nombre, apellido, dni, numero de cuenta y saldo inicial

# como metodos podremos hacer deposito retirar dinero y ver estado de cuenta

class Banco:
    def __init__(self, nombre, apellido, dni, numero_cuenta, saldo_inicial):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo_inicial

    def depositar(self, monto):
        ssself.saldo += monto
        print(f"Se ha depositado ${monto}. Saldo actual: ${self.saldo}")

    def retirar(self, monto):
        if monto > self.saldo:
            print("Fondos insuficientes.")
        else:
            self.saldo -= monto
            print(f"Se ha retirado ${monto}. Saldo actual: ${self.saldo}")

    def ver_estado_cuenta(self):
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"DNI: {self.dni}")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Saldo: ${self.saldo}")




