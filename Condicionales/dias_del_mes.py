mes = int(input("Digita el número del mes: "))

if mes in {1, 3, 5, 7, 8, 10, 12}:
    print("El mes tiene 31 días.")
elif mes in {4, 6, 9, 11}:
    print("El mes tiene 30 días.")
else:
    print("El mes tiene 28 o 29 días.")