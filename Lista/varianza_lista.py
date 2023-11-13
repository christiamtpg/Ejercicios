lista1 = [41,47,40,39,45,55]

suma_media=0

for i in lista1:
    suma_media = suma_media+i
    
media = suma_media / len(lista1)


suma_diferencias = 0

for num in lista1:
    suma_diferencias = suma_diferencias+(num - media) ** 2

varianza = suma_diferencias / len(lista1)

print(f"La varianza es: {varianza}")