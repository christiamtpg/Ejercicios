def dimension_matriz(matriz):
    if not matriz or len(matriz[0]) == 0:
        return 0, 0 
    num_filas = len(matriz)
    num_columnas = len(matriz[0])

    return num_filas, num_columnas

matriz1= [[2,5,6],[2,6,8]]


filas, columnas = dimension_matriz(matriz1)
print(f"La matriz tiene {filas} filas y {columnas} columnas.")