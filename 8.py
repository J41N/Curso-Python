
Nombre = input("¿Cuál es tu nombre? ")
print("Tu nombre es:", Nombre)

Edad = input("¿Cuál es tu edad en código binario? ")
print("Tu edad es:", Edad)

Impares = [num for num in range(1, 101) if num % 2 != 0]
print("Lista de números impares del 1 al 100:")
print(Impares)

Num1 = int(input("Escoge tu primer número impar: "))
Num2 = int(input("Escoge tu segundo número impar: "))


if Num1 in Impares and Num2 in Impares:
    print("Has escogido los siguientes números impares:", Num1, "y", Num2)
else:
    print("Uno o ambos números no son impares o no están en la lista.")

def Elige_Numeros_Impares(maximo):
    return [num for num in range(1, maximo + 1) if num % 2 != 0]


Num1 = int(input("Escoge tu primer número impar: "))
Num2 = int(input("Escoge tu segundo número impar: "))

suma = Num1 + Num2
resta = Num1 - Num2
multiplicacion = Num1 * Num2

if Num2 != 0:
        division = Num1 / Num2
else:
        division = "No se puede dividir entre 0"

print(f"\nResultados:")
print(f"Suma +: {suma}")
print(f"Resta -: {resta}")
print(f"Multiplicación x: {multiplicacion}")
print(f"División / : {division}")
