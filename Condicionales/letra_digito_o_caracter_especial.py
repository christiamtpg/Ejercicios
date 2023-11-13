caracter1 = input("Ingrese un caracter: ")
cod_ascii = ord(caracter1)

if 65 <= cod_ascii <= 90 or 97 <= cod_ascii <= 122:
    print("Es una letra.")
elif 48 <= cod_ascii <= 57:
    print("Es un digito.")
else:
    print("Es un carácter especial.")