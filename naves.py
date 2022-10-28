import csv

with open('naves.csv', 'r') as file:
    reader1 = csv.DictReader(file, delimiter=';')
    star_naves = list(reader1)
