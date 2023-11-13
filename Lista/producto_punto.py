vector1 = [8,4]
vector2 = [6,7]

producto_punto = 0

for i in range(len(vector1)):
    producto_punto = producto_punto + (vector1[i] * vector2[i])

print(f"El producto punto de los dos vectores es: {producto_punto}")