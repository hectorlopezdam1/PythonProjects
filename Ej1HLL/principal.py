import random


def mostrar_menu():
    print("BLACKJACK \n1. Modo fácil \n2. Modo normal \n0. Salir")


def pedir_opcion(mensaje):
    try:
        op = int(input(mensaje))
    except ValueError:
        op = None
    finally:
        return op


def generar_aleatorio():
    aleatorio = random.randint(1, 11)
    return aleatorio


if __name__ == '__main__':
    while True:
        a = True
        while a:
            mostrar_menu()
            opcion = pedir_opcion("Escoja una opción:\n")
            if opcion == 1:
                print("modo facil")
                a = False
            elif opcion == 2:
                print("modo normal")
                a = False
            elif opcion == 0:
                exit(0)
            else:
                print("Selecciona una opción válida\n")
        puntuacion = 0
        numeros = 0
        while puntuacion <= 15:
            aleatorio = generar_aleatorio()
            puntuacion = puntuacion + aleatorio
            numeros = numeros + 1
        if opcion == 1:
            print("Puntuacion IA = " + str(puntuacion))
        print("Es tu turno:")
        respuesta = "1"
        puntuacion_jugador = 0
        while respuesta == "1":
            aleatorio_jugador = generar_aleatorio()
            print("Tu numero es: " + str(aleatorio_jugador))
            puntuacion_jugador = puntuacion_jugador + aleatorio_jugador
            print("Tu puntuación actual es: " + str(puntuacion_jugador))
            if puntuacion_jugador > 21:
                print("Has perdido :(")
                break
            elif puntuacion_jugador == 21 and puntuacion != 21:
                print("Has ganado!")
                break
            elif puntuacion_jugador == 21 and puntuacion == 21:
                print("Empate")
                break
            else:
                while True:
                    respuesta = input("¿Seguir jugando?\n1. Sí\n2. No\nEscoja una opción:\n")
                    if respuesta == "1":
                        print("Aquí tienes tu carta...")
                        break
                    elif respuesta == "2":
                        if puntuacion_jugador < puntuacion <= 21:
                            print("Has perdido :(")
                            break
                        elif puntuacion_jugador > puntuacion or puntuacion > 21:
                            print("Has ganado!")
                            break
                        elif puntuacion_jugador == puntuacion:
                            print("Empate")
                            break
                    else:
                        print("Por favor, selecciona una opción válida")
