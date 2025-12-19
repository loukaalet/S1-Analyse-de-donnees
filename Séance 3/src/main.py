#coding : utf-8


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/

# Sources des données : production de M. Forriez, 2016-2023


#Définir une fonction 

with open(resultats-elections-presidentielles-2022-1er-tour.csv) as fichier:
        contenu = pd.read_csv(fichier)


print(contenu)