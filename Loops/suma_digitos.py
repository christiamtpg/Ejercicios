numero = input("Ingrese un número: ")

suma_digitos = 0

for num in numero:
    suma_digitos = suma_digitos+int(num)

print("La suma es:", suma_digitos)