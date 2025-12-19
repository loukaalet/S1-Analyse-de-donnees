#coding:utf8

import numpy as np
import pandas as pd
import scipy
import scipy.stats
from scipy.stats import *

def ouvrirUnFichier(nom):
    with open(nom, "r") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

def tableauDeContingence(nom, donnees):
    indexValeurs = {}
    for element in range(0,len(nom)):
        indexValeurs.update({element: nom[element]})
    return pd.DataFrame(donnees).rename(index = indexValeurs)

def sommeDesColonnes(tableau):
    colonne = list(tableau.head(0))
    sommeColonne = []
    for element in colonne:
        sommeColonne.append(tableau[element].sum())
    return sommeColonne

def sommeDesLignes(tableau):
    colonne = list(tableau.head(0))
    sommeLigne = []
    for element1 in range(0,len(tableau)):
        ligne = []
        for element2 in range(0,len(colonne)):
            ligne.append(tableau.iloc[element1, element2])
        sommeLigne.append(np.sum(list(ligne)))
    return sommeLigne

#print(data)

#Création du tableau de contingence
#Contrairement à l'usage, vous ne devez pas créer de tableau croisé dynamique, puisque le fichier est déjà un tableau de contingence
data = pd.DataFrame(ouvrirUnFichier("./data/Socioprofessionnelle-vs-sexe.csv"))
tableauDeContingence = tableauDeContingence(data["Catégorie"], {"Femmes": data["Femmes"], "Hommes": data["Hommes"]})
print("\n----------------------------------------------------------------------------------------")
print("Voici le tableau de contingence")
print("----------------------------------------------------------------------------------------\n\n")
print(tableauDeContingence)

#Calculer les marges
print("\n----------------------------------------------------------------------------------------")
print("Calcul des marges")
print("----------------------------------------------------------------------------------------\n\n")
somme_colonnes = sommeDesColonnes(tableauDeContingence)
somme_lignes   = sommeDesLignes(tableauDeContingence)

print(somme_colonnes)
print(somme_lignes) 

if sum(somme_colonnes) == sum(somme_lignes):
    print(f"Résultat des marges correct :  la sommme marges équivaut à {sum(somme_colonnes)} !")
else : 
    print("problème sur la sommme du tableau de contingence")

#Faire le test du chi2 avec les outils Scipy.stats
print("\n----------------------------------------------------------------------------------------")
print("Test du chi2")
print("----------------------------------------------------------------------------------------\n\n")
res = scipy.stats.chi2_contingency(tableauDeContingence)
print(res)

#Calculer l'intensité de liaison phi2 de Pearson
print("-" * 50)
print("Intensité de liaison phi2")
print("-" * 50)


X = tableauDeContingence["Femmes"]
Y = tableauDeContingence["Hommes"]
Pearson = pearsonr(X,Y)

print("Correlation de Pearson :", Pearson)