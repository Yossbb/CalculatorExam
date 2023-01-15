import numpy as np

def calculator():
    while True:
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
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            resultado = num1 + num2
            print("\nEl resultado de la suma es: ", resultado, "\n")
        elif opcion == 2:#Resta
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            resultado = num1 - num2
            print("\nEl resultado de la resta es: ", resultado, "\n")
        elif opcion == 3:#Multiplicación
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            resultado = num1 * num2
            print("\nEl resultado de la multiplicación es: ", resultado, "\n")
        elif opcion == 4:#División
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            resultado = num1 / num2
            print("\nEl resultado de la división es: ", resultado, "\n")
        elif opcion == 5:#Raiz Cuadrada
            num1 = float(input("Introduce el número a sacar su raiz cuadrada: "))
            resultado = np.sqrt(num1)
            print("\nLa raiz cuadrada de "+str(num1)+" es: ", resultado, "\n")
        elif opcion == 6:#Exponente
            num1 = float(input("Introduce el número a exponenciar: "))
            num2 = float(input("Introduce la potencia: "))
            resultado = num1**num2
            print("\nEl resultado de la pontencia es: ", resultado, "\n")
        elif opcion == 0:#Salir
            print("\nSaliendo de la calculadora...")
            break
        else:
            print("\nOpción inválida. Intente otra opción.,\n")

calculator()
