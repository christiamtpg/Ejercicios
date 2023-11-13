lista = [8,56,27,12,9,15]
mayor = lista[0]
for num in lista:
    if num > mayor:
        mayor = num
        
print(f"El número mayor es: {mayor}")