#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import scipy.stats

def ouvrirUnFichier(nom):
    with open(nom, "r") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu


#print(data brutes)
print("\n----------------------------------------------------------------------------------------")
print("Visualisation des données brutes")
print("----------------------------------------------------------------------------------------\n\n")
data = pd.DataFrame(ouvrirUnFichier("./data/pib-vs-energie.csv"))
print(f"Voici le tableau présentant les données sur le PIB et l'énergie :\n\
{data}")

#Extraire les colonnes PIB_2022 et Utilisation_d_energie_2022, et les visualiser
print("\n----------------------------------------------------------------------------------------")
print("Visualisation des 2 premières colonnes, sans traitement")
print("----------------------------------------------------------------------------------------\n\n")

analyse = data[["PIB_2022","Utilisation_d_energie_2022"]].copy()
print(f"Voici le tableau avec les colonnes extraites (PIB et énergie pour l'année 2022) :\n\
{analyse}")

#Copie du code sans données manquantes 
analyse_complete = analyse[
    analyse["PIB_2022"].notna() &
    analyse["Utilisation_d_energie_2022"].notna()
].copy()

#Visualisation des données
print("\n----------------------------------------------------------------------------------------")
print("Visualisation des données sans NaN")
print("----------------------------------------------------------------------------------------\n\n")
print(analyse_complete)

#Calcul de la régression linéaire pour la méthode des moindres carrées
print("\n----------------------------------------------------------------------------------------")
print("Calcul de la régression linéaire pour la méthode des moindres carrées")
print("----------------------------------------------------------------------------------------\n\n")

x = analyse_complete["Utilisation_d_energie_2022"].values #récuperer les données de x
y = analyse_complete["PIB_2022"].values #récuperer les données de y
regression = scipy.stats.linregress(x, y) #Soit énergie la variable explicative X et PIB la variable expliquée Y
print("regression réalisée")


#Calcul du coefficient de corrélation simple de Pearson
print("\n----------------------------------------------------------------------------------------")
print("Calcul du coefficient de corrélation simple de Pearson")
print("----------------------------------------------------------------------------------------\n\n")
correlation_scipy, p_value = scipy.stats.pearsonr(analyse_complete["PIB_2022"], analyse_complete["Utilisation_d_energie_2022"])
print(f"Corrélation (Scipy) : {correlation_scipy}")
print(f"Valeur p : {p_value}")


#Afficher les résultats sous forme de graphique
print("\n----------------------------------------------------------------------------------------")
print("Aller dans le dossier Séance 7>src et voir l'image extraite !")
print("----------------------------------------------------------------------------------------\n\n")
plt.scatter(x, y, label='Données')
plt.plot(x, regression.slope * x + regression.intercept, color='red', label='Régression linéaire')
plt.xlabel('Utilisation d\'énergie 2022')
plt.ylabel('PIB 2022')
plt.legend()
plt.savefig("Correlation Energie-PIB.png")

resultats_texte = (
    f"Résultats de la régression linéaire :\n"
    f"Pente (coefficient) : {regression.slope:.4f}\n"
    f"Ordonnée à l'origine : {regression.intercept:.4f}\n"
    f"Coefficient de corrélation (r) : {regression.rvalue:.4f}\n"
    f"Coefficient de détermination (r²) : {regression.rvalue**2:.4f}\n"
    f"Erreur standard : {regression.stderr:.4f}"
)

# Ajouter le texte des résultats sur la figure
plt.gca().text(
    0.02, 0.98,  # Position du texte (en coordonnées relatives)
    resultats_texte,
    transform=plt.gca().transAxes,  # Utiliser les coordonnées relatives
    fontsize=10,
    verticalalignment='top',
    bbox=dict(boxstyle='round', facecolor='white', alpha=0.8)  # Fond blanc semi-transparent
)

# Afficher la figure
plt.title('Utilisation d\'énergie VS PIB dans le monde en 2022')
plt.grid(True)
plt.show()
plt.savefig("Correlation Energie-PIB.png")
