from cuentas_bancarias import CuentaBancaria, CuentaNormal, CuentaPremium


def escribir_menu():
    print("\r\nBANCO\r\n" + "1. Crear cuenta\r\n" + "2. Ingresar dinero\r\n" + "3. Retirar dinero\r\n"
          + "4. Consultar saldo\r\n" + "0. Salir")


def escribir_submenu():
    print("\r\nTipo de cuenta\r\n" + "1. Cuenta normal\r\n" + "2. Cuenta Premium\r\n" + "0. Cancelar")


class Cajero:
    if __name__ == '__main__':
        cuenta_creada = False
        tipo_cuenta = 0
        while True:
            escribir_menu()
            opcion = int(input())
            if opcion == 1:
                if cuenta_creada:
                    print("Ya tienes una cuenta")
                else:
                    while True:
                        escribir_submenu()
                        tipo_cuenta = int(input())
                        if tipo_cuenta != 0:
                            break
                    saldo_inicial = int(input("Introduzca saldo inicial:\n"))
                    print("Tu saldo actual es: " + str(CuentaNormal.ingresar_dinero(saldo_inicial)))
                    cuenta_creada = True
            elif opcion == 2:
                cantidad = int(input("Introduzca cantidad a ingresar:\n"))
                print("Tu saldo actual es: " + str(CuentaNormal.ingresar_dinero(cantidad)))
            elif opcion == 3:
                cantidad = int(input("Introduzca cantidad a retirar:\n"))
                if tipo_cuenta == 1:
                    print("Tu saldo actual es: " + str(CuentaNormal.retirar_dinero(cantidad)))
                elif tipo_cuenta == 2:
                    print("Tu saldo actual es: " + str(CuentaPremium.retirar_dinero(cantidad)))
            elif opcion == 4:
                CuentaNormal.consultar_saldo(1)
            elif opcion == 0:
                exit(0)
                break