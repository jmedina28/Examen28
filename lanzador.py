
def lanzador():
    print("Bienvenido al lanzador de ejercicios")
    print("1. Hanoi")
    print("2. Naves")
    print("3. Sarrus")
    print("4. Polinomio")
    print("5. Hash")
    print("5. Salir")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1: 
        import hanoi
    elif opcion == 2:
        import naves
    elif opcion == 3:
        import sarrus
    elif opcion == 4:
        print("No hay polinomio")
    elif opcion == 5:
        import ejercicio5
