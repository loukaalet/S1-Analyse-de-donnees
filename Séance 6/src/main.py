# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from scipy.stats import spearmanr, kendalltau


# --------------------------------------------------
# Fonctions
# --------------------------------------------------

def ouvrirUnFichier(nom):
    with open(nom, "r", encoding="utf-8") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu


def conversionLog(liste):
    return [math.log(x) for x in liste if x > 0]


def ordreDecroissant(liste):
    return sorted(liste, reverse=True)


def ordrePopulation(pop, etat):
    ordrepop = []
    for i in range(len(pop)):
        if not np.isnan(pop[i]):
            ordrepop.append([float(pop[i]), etat[i]])
    ordrepop = ordreDecroissant(ordrepop)
    for i in range(len(ordrepop)):
        ordrepop[i] = [i + 1, ordrepop[i][1]]
    return ordrepop


def classementPays(ordre1, ordre2):
    classement = []
    if len(ordre1) <= len(ordre2):
        for i in range(len(ordre2)):
            for j in range(len(ordre1)):
                if ordre2[i][1] == ordre1[j][1]:
                    classement.append([ordre1[j][0], ordre2[i][0], ordre1[j][1]])
    else:
        for i in range(len(ordre1)):
            for j in range(len(ordre2)):
                if ordre1[i][1] == ordre2[j][1]:
                    classement.append([ordre1[i][0], ordre2[j][0], ordre1[i][1]])
    return classement


# --------------------------------------------------
# Partie sur les îles
# --------------------------------------------------

print("--------------------------------------------------")
print("Partie sur les îles")
print("--------------------------------------------------")

iles = pd.DataFrame(ouvrirUnFichier("./data/island-index.csv"))

print("Voici le fichier sur les îles :")
print(iles.head(10))

surface = iles[["Toponyme", "Surface (km²)"]].copy()

surface_data = pd.DataFrame({
    "Toponyme": [
        "Asie / Afrique / Europe",
        "Amérique",
        "Antarctique",
        "Australie"
    ],
    "Surface (km²)": [
        85545323,
        37856841,
        7768030,
        7605049
    ]
})

surface = pd.concat([surface, surface_data], ignore_index=True)

surface_convertie = list(surface["Surface (km²)"].astype(float))
surface_convertie = ordreDecroissant(surface_convertie)

rangs = list(range(1, len(surface_convertie) + 1))

plt.figure(figsize=(10, 6))
plt.plot(rangs, surface_convertie, marker="o", linestyle="none")
plt.xlabel("Rang")
plt.ylabel("Surface (km²)")
plt.title("Loi rang-taille – version linéaire")
plt.grid(True)
plt.savefig("test_iles.png", dpi=300)
plt.show()

surface_log = conversionLog(surface_convertie)
rangs_log = conversionLog(rangs)

plt.figure(figsize=(10, 6))
plt.plot(rangs_log, surface_log, marker="o", linestyle="none")
plt.xlabel("log(Rang)")
plt.ylabel("log(Surface)")
plt.title("Loi rang-taille des îles (log-log)")
plt.grid(True)
plt.savefig("test_iles2.png", dpi=300)
plt.show()
#Question Est-il possible de faire un test sur les rangs? 
"""
C'est impossible de faire un test sur les rangs car on ne travaille que sur une seule liste, celle de la taille des Etats. Pour réaliser un test sur les rangs on doit en effet avoir deux listes hierachisées à partir de deux variables différentes.
"""
# --------------------------------------------------
# Partie sur les États
# --------------------------------------------------

print("--------------------------------------------------")
print("Partie sur les États")
print("--------------------------------------------------")

monde = pd.DataFrame(
    ouvrirUnFichier("./data/Le-Monde-HS-Etats-du-monde-2007-2025.csv")
)

extract_monde = monde[[
    "État",
    "Pop 2007",
    "Pop 2025",
    "Densité 2007",
    "Densité 2025"
]].copy()

print(extract_monde.head())

classementpop2007 = ordrePopulation(
    extract_monde["Pop 2007"],
    extract_monde["État"]
)

classementpop2025 = ordrePopulation(
    extract_monde["Pop 2025"],
    extract_monde["État"]
)

classementdensite2007 = ordrePopulation(
    extract_monde["Densité 2007"],
    extract_monde["État"]
)

classementdensite2025 = ordrePopulation(
    extract_monde["Densité 2025"],
    extract_monde["État"]
)

comparaison_liste = classementPays(
    classementpop2007,
    classementdensite2025
)

comparaison_liste.sort()

print("Extrait comparaison :", comparaison_liste[:10])

rangs_pop = []
rangs_densite = []

for element in comparaison_liste:
    rangs_pop.append(element[0])
    rangs_densite.append(element[1])

print("Rangs population :", rangs_pop[:10])
print("Rangs densité :", rangs_densite[:10])

correlation_spearman = spearmanr(rangs_pop, rangs_densite)
concordance_kendall = kendalltau(rangs_pop, rangs_densite)

print("Corrélation de Spearman :", correlation_spearman)
print("Concordance de Kendall :", concordance_kendall)
