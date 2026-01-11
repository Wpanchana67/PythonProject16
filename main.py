"""
Programa: Conversor y Calculador
Autor: William Javier Panchana Reyes

Descripción:
Este programa permite calcular el área de un rectángulo y convertir metros a centímetros.
Utiliza diferentes tipos de datos como int, float, string y boolean.
"""

# Función que calcula el área de un rectángulo
def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area


# Función que convierte metros a centímetros
def convertir_metros_a_centimetros(metros):
    centimetros = metros * 100
    return centimetros


# Función principal del programa
def ejecutar_programa():
    print("Bienvenido al programa de cálculo y conversión")

    nombre_usuario = input("Ingrese su nombre: ")  # string
    print("Hola", nombre_usuario)

    continuar = True  # boolean

    while continuar:
        print("\nSeleccione una opción:")
        print("1. Calcular área de un rectángulo")
        print("2. Convertir metros a centímetros")
        print("3. Salir")

        opcion = int(input("Ingrese una opción: "))  # integer

        if opcion == 1:
            base = float(input("Ingrese la base del rectángulo: "))  # float
            altura = float(input("Ingrese la altura del rectángulo: "))  # float
            area = calcular_area_rectangulo(base, altura)
            print("El área del rectángulo es:", area)

        elif opcion == 2:
            metros = float(input("Ingrese los metros: "))
            centimetros = convertir_metros_a_centimetros(metros)
            print("Equivale a", centimetros, "centímetros")

        elif opcion == 3:
            print("Gracias por usar el programa")
            continuar = False

        else:
            print("Opción inválida, intente nuevamente")


# Ejecutar el programa
ejecutar_programa()
