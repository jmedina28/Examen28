def Hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco de {origen} a {destino}")
    else:
        Hanoi(n-1, origen, auxiliar, destino)
        print(f"Mover disco de {origen} a {destino}")
        Hanoi(n-1, auxiliar, destino, origen)


Hanoi(int(input("Ingrese un número de discos: ")), "Origen", "Destino", "Auxiliar")
