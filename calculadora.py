from calculos_dev1 import add, subtract, multiply, divide
#import power, square_root, modulo from calculos-dev2

def addAndPower(a, b, exponent):
    return

def subtractAndRoot(a, b):
    return

def multiplyAndModulo(a, b, mod):
    return

a = float(input("Escribe el primer número: "))
b = float(input("Escribe el segundo número: "))

# Menú de operaciones escogidos con un número
print("¿Qué operación quieres hacer?")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Escribe el número de la operación: ")

 #Operación que el usuario quiere realizar
if opcion == "1":
    print("Resultado:", add(a, b))
elif opcion == "2":
    print("Resultado:", subtract(a, b))
elif opcion == "3":
    print("Resultado:", multiply(a, b))
elif opcion == "4":
    print("Resultado:", divide(a, b))
else:
    print("Opción no válida")

continuar = input("\n¿Quieres hacer otra operación? (sí/no): ").lower()
    if continuar != "sí":
        print("¡Hasta luego!")
        break