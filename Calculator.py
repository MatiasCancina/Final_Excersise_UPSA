# Función para realizar la suma
def suma(a, b):
    return a + b

# Función para realizar la resta
def resta(a, b):
    return a - b

# Función para realizar la multiplicación
def multiplicacion(a, b):
    return a * b

# Función para realizar la división
def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    else:
        return a / b

while True:
    # Solicitar dos números al usuario
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Por favor, ingrese números válidos.")
        continue

    # Mostrar el menú de opciones
    print("Menú de opciones:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    # Solicitar la elección al usuario
    opcion = input("Seleccione una opción (1/2/3/4/5): ")

    if opcion == '1':
        resultado = suma(num1, num2)
        print("El resultado de la suma es:", resultado)
    elif opcion == '2':
        resultado = resta(num1, num2)
        print("El resultado de la resta es:", resultado)
    elif opcion == '3':
        resultado = multiplicacion(num1, num2)
        print("El resultado de la multiplicación es:", resultado)
    elif opcion == '4':
        resultado = division(num1, num2)
        print("El resultado de la división es:", resultado)
    elif opcion == '5':
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida (1/2/3/4/5).")
