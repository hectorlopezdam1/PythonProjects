from abc import ABC


class CuentaBancaria(ABC):

    saldo = 0

    def consultar_saldo(self):
        pass

    def ingresar_dinero(cantidad):
        pass

    def retirar_dinero(cantidad):
        pass

class CuentaNormal:

    def consultar_saldo(self):
        print(str(CuentaBancaria.saldo))

    def ingresar_dinero(cantidad):
        if cantidad < 0:
            print("La cantidad a ingresar debe ser positiva")
        else:
            CuentaBancaria.saldo += cantidad
            return CuentaBancaria.saldo

    def retirar_dinero(cantidad):
        if cantidad < 0:
            print("La cantidad a retirar debe ser positiva")
        else:
            if cantidad > CuentaBancaria.saldo:
                print("No puede quedarse con saldo negativo")
            else:
                CuentaBancaria.saldo -= cantidad
                return CuentaBancaria.saldo


class CuentaPremium:

    def consultar_saldo(self):
        print(str(CuentaBancaria.saldo))

    def ingresar_dinero(cantidad):
        if cantidad < 0:
            print("La cantidad a ingresar debe ser positiva")
        else:
            CuentaBancaria.saldo += cantidad
            return CuentaBancaria.saldo

    def retirar_dinero(cantidad):
        if cantidad < 0:
            print("La cantidad a retirar debe ser positiva")
        else:
            CuentaBancaria.saldo -= cantidad
            return CuentaBancaria.saldo
