def matriz():
    matriz = []
    for i in range(3):
        matriz.append([])
        for j in range(3):
            matriz[i].append(0)
    return matriz
  
def mostrar_matriz(matriz):
    for i in range(3):
        for j in range(3):
            print(f"{matriz[i][j]} ", end="")
        print()
        
matriz = matriz()
mostrar_matriz(matriz)
