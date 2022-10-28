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
        
def determinantesarrus(matriz):
    determinante = 0
    for i in range(3):
        determinante += matriz[0][i] * matriz[1][(i+1)%3] * matriz[2][(i+2)%3]
        determinante -= matriz[0][i] * matriz[1][(i+2)%3] * matriz[2][(i+1)%3]
    return determinante


matriz = matriz()
matriz = rellenar_matriz(matriz)
mostrar_matriz(matriz)
determinante = determinantesarrus(matriz)
print(f"el determinante es {determinante}")
