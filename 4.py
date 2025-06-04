numero1 = float(input("Ingresa el primer número, hacker♳: "))
numero2 = float(input("Ingresa el segundo número, hacker♴: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

if numero2 != 0:
    division = numero1 / numero2
else:
    division = "No se puede dividir entre 0"

print(f"\nResultados:")
print(f"Suma +: {suma}")
print(f"Resta -: {resta}")
print(f"Multiplicación x: {multiplicacion}")
print(f"División / : {division}")