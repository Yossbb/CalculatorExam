import numpy as np

def calculator():
    print("Menu de operaciones:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Raiz Cuadrada")
    print("6. Exponente")
    print("0. Salir")

    opcion = int(input("Seleccione una operación a usar: "))

    if opcion == 1:#Suma
        print("\nEl resultado de la suma es: ", resultado, "\n")
    elif opcion == 2:#Resta
        print("\nEl resultado de la resta es: ", resultado, "\n")
    elif opcion == 3:#Multiplicación
        print("\nEl resultado de la multiplicación es: ", resultado, "\n")
    elif opcion == 4:#División
        print("\nEl resultado de la división es: ", resultado, "\n")
    elif opcion == 5:#Raiz Cuadrada
        print("\nLa raiz cuadrada de "+str(num1)+" es: ", resultado, "\n")
    elif opcion == 6:#Exponente
        print("\nEl resultado de la pontencia es: ", resultado, "\n")
    elif opcion == 0:#Salir
        print("\nSaliendo de la calculadora...")
        break
    else:
        print("\nOpción inválida. Intente otra opción.,\n")

calculator()
