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

ordenar_largo()
ordenar_naves()
