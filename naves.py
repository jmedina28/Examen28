import csv

with open('naves.csv', 'r') as file:
    reader1 = csv.DictReader(file, delimiter=';')
    star_naves = list(reader1)

def ordenar_naves():
    naves = []
    for row in star_naves:
        naves.append(row['Name'])
    naves.sort()
    print(f"\n\nLas naves ordenadas por nombre son {naves}")

def ordenar_largo():
    naves_largo = []
    for row in star_naves:
        naves_largo.append(row['Name'] + " " + row['Length'])
    naves_largo.sort() ; naves_largo.reverse()
    print(f"\n\nLas naves ordenadas por largo son {naves_largo}")


def millenium_falcon():
    for row in star_naves:
        if row['Name'] == "Millennium Falcon":
            print(f"\n\nLa información del Falcón Milenario es {row}")

def death_star():
    for row in star_naves:
        if row['Name'] == "Death Star":
            print(f"\n\nLa información de la Estrella de la Muerte es {row}")

def cinco_naves():
    naves = []
    for row in star_naves:
        naves.append(row['Name'] + " " + row['Passengers'])
    naves.sort() ; naves.reverse()
    print(f"\n\nLas cinco naves con mayor cantidad de pasajeros son {naves[:5]}")
