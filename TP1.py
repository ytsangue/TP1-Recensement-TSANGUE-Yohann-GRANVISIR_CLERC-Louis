#!/usr/bin/env python
# coding: utf-8

# # SAE15 Traitement des données 
# # TP 1 Recensement

# ## Exercice 1 : Problème ouvert

# Les fichiers donnees 2008.csv, donnees 2016.csv, donnees 2021.csv disponibles sur
# Plubel contiennent les données issues des recensements de la population Française de 2008,
# 2016 et 2021. On entend souvent dire que la population d’Auxerre et/ou de l’Yonne est en
# diminution.
# 
# L’objectif du TP est de traiter les données pour confirmer ou infirmer cette rumeur :
# on pourra considérer la population d’Auxerre, de l’agglomération immédiate (Appoigny,
# Auxerre, Monéteau, Perrigny, Saint-Georges-sur-Baulche) ou de l’agglomération totale
# (Appoigny, Augy, Auxerre, Bleigny-le-Carreau, Branches, Champs-sur-Yonne, Charbuy,
# Chevannes, Chitry, Coulanges-la-Vineuse, Escamps, Escolives Sainte-Camille, Gurgy,
# Gy-l’Evêque, Irancy, Jussy, Lindry, Monéteau, Montigny-la-Resle, Perrigny, Quenne,
# Saint-Bris-le-Vineux, Saint-Georges-sur-Baulche, Vallan, Venoy, Villefargeau, Villeneuve-
# Saint-Salves, Vincelles, Vincelottes) au fil des ans.
# 
# L’intégralité du traitement des données sera réalisé en langage Python (et éventuellement
# bash pour un pré-traitement). Le compte-rendu devra comporter les scripts commentés ainsi
# que des repr´esentations graphiques permettant de visualiser les r´esultats finaux (´egalement
# comment´es).
# 
# Tous les documents (code, compte-rendu, readme, etc) seront g´er´es avec Git
# et d´epos´es (publiquement) sur votre espace Github dans un projet nomm´e
# TP1-Recensement-NOM1-Pr´enom1-NOM2-Pr´enom2 avant la fin du TP (la date et l’ho-
# raire de d´epˆot sera indiqu´ee par Github). Le lien vers ce d´epˆot sera indiqu´e sur Plubel dans
# le questionnaire pr´evu `a cet effet (´egalement avant la fin du TP).

# In[65]:


import csv
import matplotlib.pyplot as plt


# In[66]:


table=[]
with open("/home/Etudiants/RT/BUT-RT-1/lg409538/Documents/SAE15/donnees_2008.csv",newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    for ligne in reader:
        table.append(ligne)

del table[0]


# In[75]:


table_1 = []
with open("/home/Etudiants/RT/BUT-RT-1/lg409538/Documents/SAE15/donnees_2016.csv", newline='') as csvfile:
    reader_1 = csv.reader(csvfile, delimiter=',')
    for ligne in reader_1:
        table_1.append(ligne)
del table_1[0]


# In[76]:


table2 = []
with open("/home/Etudiants/RT/BUT-RT-1/lg409538/Documents/SAE15/donnees_2021.csv", newline='') as csvfile:
    reader2 = csv.reader(csvfile, delimiter=';')
    for ligne in reader2:
        table2.append(ligne)
del table2[0]


# In[5]:


for i in range(len(table)):
    table[i][9] = int(table[i][9])
    popu_total = [int(popu_total[9]) for popu_total in table]
    popu_total_moyenne = sum(popu_total) / len(popu_total)

print(popu_total_moyenne)


# In[58]:


#2008
# Supposons que 'table' est une liste de listes avec des données
communes = [commune[6] for commune in table]  #6ème  colonne contient le nom de la commune
departements = [commune[2] for commune in table]  # 2ème colonne contient le code du département
populations = [int(commune[9]) for commune in table]  # 9ème colonne contient le nombre de population

# Liste des communes pour lesquelles vous souhaitez calculer la population totale
communes_a_inclure = [
    'Appoigny', 'Augy', 'Auxerre', 'Bleigny-le-Carreau', 'Branches', 'Champs-sur-Yonne', 'Charbuy', 'Chevannes',
    'Chitry', 'Coulanges-la-Vineuse', 'Escamps', 'Escolives Sainte-Camille', 'Gurgy', 'Gy-l’Evˆeque', 'Irancy',
    'Jussy', 'Lindry', 'Moneteau', 'Montigny-la-Resle', 'Perrigny', 'Quenne', 'Saint-Bris-le-Vineux',
    'Saint-Georges-sur-Baulche', 'Vallan', 'Venoy', 'Villefargeau', 'Villeneuve-Saint-Salves', 'Vincelles', 'Vincelottes'
]

# Code du département à vérifier (89 pour l'Yonne)
code_departement_a_verifier = '89'

# Initialiser la population totale
population_totale = 0

# Parcourir les données pour calculer la population totale des communes spécifiées dans le département 89
for commune, departement, population in zip(communes, departements, populations):
    if departement.isdigit() and commune in communes_a_inclure and int(departement) == int(code_departement_a_verifier):
        population_totale += population

# Afficher la population totale des communes spécifiées dans le département 89
print(f"Population totale des communes spécifiées dans le département 89 : {population_totale}")


# In[80]:


#2016
# Supposons que 'table' est une liste de listes avec des données
communes = [commune[6] for commune in table_1]  # 6ème colonne contient le nom de la commune
departements = [commune[2] for commune in table_1]  #2ème colonne contient le code du département
populations = [int(commune[9]) for commune in table_1]  # 9ème colonne contient le nombre de population

# Liste des communes pour lesquelles vous souhaitez calculer la population totale
communes_a_inclure = [
    'Appoigny', 'Augy', 'Auxerre', 'Bleigny-le-Carreau', 'Branches', 'Champs-sur-Yonne', 'Charbuy', 'Chevannes',
    'Chitry', 'Coulanges-la-Vineuse', 'Escamps', 'Escolives Sainte-Camille', 'Gurgy', 'Gy-l’Evˆeque', 'Irancy',
    'Jussy', 'Lindry', 'Moneteau', 'Montigny-la-Resle', 'Perrigny', 'Quenne', 'Saint-Bris-le-Vineux',
    'Saint-Georges-sur-Baulche', 'Vallan', 'Venoy', 'Villefargeau', 'Villeneuve-Saint-Salves', 'Vincelles', 'Vincelottes'
]

# Code du département à vérifier (89 pour l'Yonne)
code_departement_a_verifier = '89'

# Initialiser la population totale
population_totale = 0

# Parcourir les données pour calculer la population totale des communes spécifiées dans le département 89
for commune, departement, population in zip(communes, departements, populations):
    if departement.isdigit() and commune in communes_a_inclure and int(departement) == int(code_departement_a_verifier):
        population_totale += population

# Afficher la population totale des communes spécifiées dans le département 89
print(f"Population totale des communes spécifiées dans le département 89 : {population_totale}")


# In[87]:


plt.figure(figsize=(8, 6))
plt.plot(['2008', '2016'], [effectif_total_2008, effectif_total_2016], marker='o', linestyle='-', color='b')
plt.xlabel('Année')
plt.ylabel('Effectif total')
plt.title('Évolution de l\'effectif total des communes spécifiées en 2008 et 2016')
plt.show()


# In[ ]:




