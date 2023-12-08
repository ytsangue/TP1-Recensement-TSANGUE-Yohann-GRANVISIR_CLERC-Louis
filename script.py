import csv
table2008=[]
with open('donnees_2008.csv',newline='') as csvfile:
    reader1=csv.reader(csvfile,delimiter=',')
    for row in reader1:
        table2008.append(row)
del table2008[0]
#print(table2008)

table2016=[]
with open('donnees_2016.csv',newline='') as csvfile:
    reader2=csv.reader(csvfile,delimiter=',')
    for row in reader2:
        table2016.append(row)
del table2016[0]
#print(table2016)

table2021=[]
with open('donnees_2021.csv',newline='') as csvfile:
    reader3=csv.reader(csvfile,delimiter=';')
    for row in reader3:
        table2021.append(row)
del table2021[0]
#print(table2021)

#Etude de l'evolution de la population d'Auxerre
#Recuperation de la population d'Auxerre en 2008 et son agglo immédiate dans une variable
for element in table2008:
    if element[6]=='Auxerre':
        auxerre2008 = int(element[9])
    elif element[6]=='Appoigny':
        appoigny2008 = int(element[9])
    elif element[6]=='Monéteau':
        moneteau2008 = int(element[9])
    elif element[6]=='Perrigny':
        perrigny2008 = int(element[9])
    elif element[6]=='Saint-Georges-sur-Baulche':
        saintgeorges2008 = int(element[9])
agglo_imm_auxerre2008 = auxerre2008 + appoigny2008 + moneteau2008 + perrigny2008 + saintgeorges2008
#print(agglo_imm_auxerre2008)
#print(auxerre2008)

#Recuperation de la population d'Auxerre et son agglo immédiate en 2016 dans une variable
for element in table2016:
    if element[6]=='Auxerre':
        auxerre2016 = int(element[9])
    elif element[6]=='Appoigny':
        appoigny2016 = int(element[9])
    elif element[6]=='Monéteau':
        moneteau2016 = int(element[9])
    elif element[6]=='Perrigny':
        perrigny2016 = int(element[9])
    elif element[6]=='Saint-Georges-sur-Baulche':
        saintgeorges2016 = int(element[9])
agglo_imm_auxerre2016 = auxerre2016 + appoigny2016 + moneteau2016 + perrigny2016 + saintgeorges2016
#print(agglo_imm_auxerre2016)
#print(auxerre2016)


#Recuperation de la population d'Auxerre et son agglo immédiate en 2021 dans une variable
for element in table2021:
    if element[2]=='89024':
        auxerre2021 = int(element[5])
    elif element[2]=='89013':
        appoigny2021 = int(element[5])
    elif element[2]=='89263':
        moneteau2021 = int(element[5])
    elif element[2]=='89295':
        perrigny2021 = int(element[5])
    elif element[2]=='89346':
        saintgeorges2021 = int(element[5])
agglo_imm_auxerre2021 = auxerre2021 + appoigny2021 + moneteau2021 + perrigny2021 + saintgeorges2021
#print(agglo_imm_auxerre2021)
#print(auxerre2021)

print('Population 2008')
print('Auxerre :',auxerre2008)
print('Agglomération immédiate :',agglo_imm_auxerre2008)
print()
print('Population 2016')
print('Auxerre :',auxerre2016)
print('Agglomération immédiate :',agglo_imm_auxerre2016)
print()
print('Population 2021')
print('Auxerre :',auxerre2021)
print('Agglomération immédiate :',agglo_imm_auxerre2021)

#Creation de la courbe de la populaton d'Auxerre 2008-2021
import numpy as np 
import matplotlib.pyplot as plt

plt.plot([2008,2016,2021],[auxerre2008,auxerre2016,auxerre2021])
plt.plot([2008,2016,2021],[agglo_imm_auxerre2008,agglo_imm_auxerre2016,agglo_imm_auxerre2021])
plt.title("Population d'Auxerre (bleu) et son agglomération immédiate (orange)")
plt.show()

#Comme nous pouvons le voir sur le graphique la population d'Auxerre
#et de son agglomération immédiate diminue au fil des années