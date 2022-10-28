def matriz():
    matriz = []
    for i in range(3):
        matriz.append([])
        for j in range(3):
            matriz[i].append(0)
    return matriz

def rellenar_matriz(matriz):
    for i in range(3):
        for j in range(3):
            matriz[i][j] = int(input(f"ingrese el numero de la posicion {i},{j}: "))
    return matriz
  
def mostrar_matriz(matriz):
    for i in range(3):
        for j in range(3):
            print(f"{matriz[i][j]} ", end="")
        print()
        
matriz = matriz()
matriz = rellenar_matriz(matriz)
mostrar_matriz(matriz)
