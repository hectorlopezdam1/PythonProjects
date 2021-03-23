from figuras import Triagulo, Rectangulo, Cuadrado, Petagono


def escribir_menu():
    print("\nFIGURAS GEOMÉTRICAS\n 1. Triángulo\n 2. Rectángulo\n 3. Cuadrado\n 4. Pentágono\n 0. Salir")


def pedir_opcion(mensaje):
    try:
        op = int(input(mensaje))
    except ValueError:
        op = None
    finally:
        return op


if __name__ == '__main__':
    while True:
        escribir_menu()
        opcion = pedir_opcion("Escoja una opción: ")
        if opcion == 0:
            break
            exit(0)
        elif opcion == 1:
            lado1 = input("Introduce lado 1 (base): ")
            lado2 = input("Introduce lado 2: ")
            lado3 = input("Introduce lado 3: ")
            altura = input("Introduce altura: ")
            area = Triagulo.calcular_area(lado1, altura)
            perimetro = Triagulo.calcular_perimetro(lado1, lado2, lado3)
            print("El área es: " + str(area) + " y el perímetro es: " + str(perimetro))
        elif opcion == 2:
            base = input("Introduzca base: ")
            altura = input("Introduzca altura: ")
            area = Rectangulo.calcular_area(base, altura)
            perimetro = Rectangulo.calcular_perimetro(base, altura)
            print("El área es: " + str(area) + " y el perímetro es: " + str(perimetro))
        elif opcion == 3:
            lado = input("Introduce lado: ")
            area = Cuadrado.calcular_area(lado)
            perimetro = Cuadrado.calcular_perimetro(lado)
            print("El área es: " + str(area) + " y el perímetro es: " + str(perimetro))
        elif opcion == 4:
            lado = input("Introduce lado: ")
            apotema = input("Introduce apotema: ")
            area = Petagono.calcular_area(float(lado) * 5, apotema)
            perimetro = Petagono.calcular_perimetro(lado)
            print("El área es: " + str(area) + " y el perímetro es: " + str(perimetro))
        else:
            print("ERROR, OPCIÓN NO VÁLIDA")











