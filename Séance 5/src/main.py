#coding:utf8

import pandas as pd
import math
import scipy
from scipy.stats import *
import numpy as np
import matplotlib.pyplot as plt


#C'est la partie la plus importante dans l'analyse de données. D'une part, elle n'est pas simple à comprendre tant mathématiquement que pratiquement. D'autre, elle constitue une application des probabilités. L'idée consiste à comparer une distribution de probabilité (théorique) avec des observations concrètes. De fait, il faut bien connaître les distributions vues dans la séance précédente afin de bien pratiquer cette comparaison. Les probabilités permettent de définir une probabilité critique à partir de laquelle les résultats ne sont pas conformes à la théorie probabiliste.
#Il n'est pas facile de proposer des analyses de données uniquement dans un cadre univarié. Vous utiliserez la statistique inférentielle principalement dans le cadre d'analyses multivariées. La statistique univariée est une statistique descriptive. Bien que les tests y soient possibles, comprendre leur intérêt et leur puissance d'analyse dans un tel cadre peut être déroutant.
#Peu importe dans quelle théorie vous êtes, l'idée de la statistique inférentielle est de vérifier si ce que vous avez trouvé par une méthode de calcul est intelligent ou stupide. Est-ce que l'on peut valider le résultat obtenu ou est-ce que l'incertitude qu'il présente ne permet pas de conclure ? Peu importe également l'outil, à chaque mesure statistique, on vous proposera un test pour vous aider à prendre une décision sur vos résultats. Il faut juste être capable de le lire.

#Par convention, on place les fonctions locales au début du code après les bibliothèques.
def ouvrirUnFichier(nom):
    with open(nom, "r") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

def ouvrirUnFichier1(nom):
    with open(nom, "r") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

def ouvrirUnFichier2(nom):
    with open(nom, "r") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

donnees = pd.DataFrame(ouvrirUnFichier("./data/Echantillonnage-100-Echantillons.csv"))
fichier_test_1 = ouvrirUnFichier("./data/Loi-normale-test-1.csv")
fichier_test_2 = ouvrirUnFichier("./data/Loi-normale-test-2.csv")


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Théorie de l'échantillonnage (intervalles de fluctuation) (L'échantillonnage se base sur les fréquences observées dans les échantillons // la répétitivité.)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Ouvrir le fichier
print("---------------------------------------------------------------------------------------\n\
Résultat sur le calcul d'un intervalle de fluctuation\n\
---------------------------------------------------------------------------------------")

print("Voici le tableau de données : \n\
-----------------------------\n")
print(donnees)

#Calculer la moyenne de l'échantillon (et arrondir avec aucune décimale)
moyennesE = np.mean(donnees, axis = 0)
moyennesE = round(moyennesE, 0)
print(f"Voici les moyennes de la liste de l'échantillon {moyennesE}")


#Calculer les fréquences de l'échantillon (somme des trois moyennes / ensemble des moyennes)
somme_moyennesE = sum(moyennesE)
print(f"\nVoici la somme des moyennes {somme_moyennesE} de l'échantillon, nous allons maintenant calculer la fréquence pour chaque moyenne :")
frequencesE = moyennesE / somme_moyennesE
print("\nFréquences de l'échantillon estimées :")
print(f"Pour         : {frequencesE.iloc[0]:.4f}")
print(f"Contre       : {frequencesE.iloc[1]:.4f}")
print(f"Sans opinion : {frequencesE.iloc[2]:.4f}")

#Calculer les fréquences de la pop mère
moyennesM = pd.Series([852, 911, 422])
print(f"Voici les moyennes de la liste de la population mère {moyennesM}")
print(f"Pour         : {moyennesM.iloc[0]}")
print(f"Contre       : {moyennesM.iloc[1]}")
print(f"Sans opinion : {moyennesM.iloc[2]}")
somme_moyennesM = sum(moyennesM)

print(f"Nous allons maintenant calculer la fréquence pour chaque moyenne de la popualtion mère :")
frequencesM = moyennesM / somme_moyennesM

print("\nFréquences de l'échantillon estimées :")
print(f"Pour         : {frequencesM.iloc[0]:.4f}")
print(f"Contre       : {frequencesM.iloc[1]:.4f}")
print(f"Sans opinion : {frequencesM.iloc[2]:.4f}")

# Définir la fonction de calcul des intervalles de fluctuation pour chaque opinion de la population mère
def intervalle_fluctuation(f, n, z_c):
    sigma = np.sqrt((f * (1 - f)) / n)
    borne_inf = f - z_c * sigma
    borne_sup = f + z_c * sigma
    return borne_inf, borne_sup

# Taille de l'échantillon
n = 2185
# Seuil de confiance
z_c = 1.96

# Calcul des intervalles pour chaque opinion
intervalle_pour = intervalle_fluctuation(frequencesE.iloc[0], n, z_c)
intervalle_contre = intervalle_fluctuation(frequencesE.iloc[1], n, z_c)
intervalle_sans_opinion = intervalle_fluctuation(frequencesE.iloc[2], n, z_c)

# Affichage des résultats
print("\nIntervalles de fluctuation à 95% pour la population mère :")
print(f"Pour         : [{intervalle_pour[0]:.4f}, {intervalle_pour[1]:.4f}]")
print(f"Contre       : [{intervalle_contre[0]:.4f}, {intervalle_contre[1]:.4f}]")
print(f"Sans opinion : [{intervalle_sans_opinion[0]:.4f}, {intervalle_sans_opinion[1]:.4f}]")

#Test des résultats 

def est_dans_intervalle(frequence, intervalle): # Vérification si les fréquences de l'échantillon sont dans les intervalles de fluctuation
    return intervalle[0] <= frequence <= intervalle[1]

resultat_pour = est_dans_intervalle(frequencesE.iloc[0], intervalle_pour) # Vérification pour chaque opinion
resultat_contre = est_dans_intervalle(frequencesE.iloc[1], intervalle_contre) # Vérification pour chaque opinion
resultat_sans_opinion = est_dans_intervalle(frequencesE.iloc[2], intervalle_sans_opinion) # Vérification pour chaque opinion

print("\nVérification si les fréquences de l'échantillon sont dans les intervalles de fluctuation :") # Affichage des résultats de la vérification
print(f"Pour         : {'OK' if resultat_pour else 'Hors intervalle'}")
print(f"Contre       : {'OK' if resultat_contre else 'Hors intervalle'}")
print(f"Sans opinion : {'OK' if resultat_sans_opinion else 'Hors intervalle'}")


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Théorie de l'estimation (intervalles de confiance) #L'estimation se base sur l'effectif.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""On récupère quoi ??? les données initiales ou bien celles des fréquences ???"""

# Prendre le premier échantillon de laliste précédente en utilisant la méthode
print("---------------------------------------------------------------------------------------\n\
Résultat sur le calcul d'un intervalle de confiance\n\
---------------------------------------------------------------------------------------\n")
estimation = donnees.iloc[0]
estimation = list(estimation)
print(f"Voici le premier échantillon de la liste précédente :\n\
{estimation}")

#Calculer la somme de la ligne
somme_estimation = sum(estimation)
print(f"Voici la somme de la ligne : \n\
{somme_estimation}")

#Calculer les fréquences en utilisant l’effectif total de l’échantillon isolé
print("Nous allons maintenant calculer la fréquence pour l'échantillon isolé")
frequences_estimation = pd.Series(estimation) / somme_estimation

print("\nFréquences de l'échantillon isolé :")
print(f"Pour         : {frequences_estimation.iloc[0]:.4f}")
print(f"Contre       : {frequences_estimation.iloc[1]:.4f}")
print(f"Sans opinion : {frequences_estimation.iloc[2]:.4f}")

#Calculer l'intervalle pour chaque opinion
z_c = 1.96

def intervalle_confiance(f, n, z_c):
    sigma = np.sqrt((f * (1 - f)) / n)
    borne_inf = f - z_c * sigma
    borne_sup = f + z_c * sigma
    return borne_inf, borne_sup

intervalle_pour = intervalle_confiance(frequences_estimation[0], n, z_c)
intervalle_contre = intervalle_confiance(frequences_estimation[1], n, z_c)
intervalle_sans_opinion = intervalle_confiance(frequences_estimation[2], n, z_c)

# Affichage des résultats
print("Intervalles de confiance à 95% pour le premier échantillon :")
print(f"Pour         : [{intervalle_pour[0]:.4f}, {intervalle_pour[1]:.4f}]")
print(f"Contre       : [{intervalle_contre[0]:.4f}, {intervalle_contre[1]:.4f}]")
print(f"Sans opinion : [{intervalle_sans_opinion[0]:.4f}, {intervalle_sans_opinion[1]:.4f}]")


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Théorie de la décision (tests d'hypothèse) #La décision se base sur la notion de risques alpha et bêta.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
Remarques : 
Problème sur le code, raison inconnue (voir dossier)
"""

#Comme à la séance précédente, l'ensemble des tests se trouve au lien : https://docs.scipy.org/doc/scipy/reference/stats.html
print("\n\
\n\
---------------------------------------------------------------------------------------\n\
Théorie de la décision\n\
---------------------------------------------------------------------------------------")
from scipy.stats import shapiro
# extraitre les données
col1 = fichier_test_1["Test"]
col2 = fichier_test_2["Test"]

stat1, p_value1 = scipy.stats.shapiro(col1)
stat2, p_value2 = scipy.stats.shapiro(col2)

# Test de Shapiro-Wilk pour loi1
print ("résultat du test de normalité de Shapiro-Wilk pour fichier 1")
print (f"statistique ={stat1} et p-value={p_value1}")
if p_value1 > 0.05:
        print("Conclusion : Les données suivent une loi normale (on ne rejette pas H0)\n")
else:
        print("Conclusion : Les données ne suivent pas une loi normale (on rejette H0)\n")

# Test de Shapiro-Wilk pour loi2
print ("résultat du test de normalité de Shapiro-Wilk pour fichier 2")
print (f"statistique ={stat2} et p-value={p_value2}")
if p_value2 > 0.05:
        print("Conclusion : Les données suivent une loi normale (on ne rejette pas H0)\n")
else:
        print("Conclusion : Les données ne suivent pas une loi normale (on rejette H0)\n")


#J'ai eu à souci pour le test de shapiro, dont les deux affichaient une pvalue < 0.95. J'ai donc choisi de faire un histogramme pour mieux comprendre
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# Charger les données
loi1 = pd.DataFrame(ouvrirUnFichier1("./data/Loi-normale-Test-1.csv"))
loi2 = pd.DataFrame(ouvrirUnFichier2("./data/Loi-normale-Test-2.csv"))

# Créer une figure avec des sous-graphiques
fig, axes = plt.subplots(1, 2, figsize=(14, 12))

# Histogramme pour loi1
axes[0].hist(loi1, bins=20, color='skyblue', edgecolor='black', alpha=0.7)
axes[0].set_title('Histogramme de Loi-normale-Test-1')
axes[0].set_xlabel('Valeurs')
axes[0].set_ylabel('Fréquence')

# Histogramme pour loi2
axes[1].hist(loi2, bins=20, color='salmon', edgecolor='black', alpha=0.7)
axes[1].set_title('Histogramme de Loi-normale-Test-2')
axes[1].set_xlabel('Valeurs')
axes[1].set_ylabel('Fréquence')

plt.tight_layout()
plt.savefig("tests_normale.png", dpi=300)
