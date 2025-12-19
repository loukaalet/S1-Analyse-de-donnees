#coding : utf8
import pandas as pd
import requests

def geturl(method, format, stations, start, end, token):
    stationstexte = ""
    for element in stations:
        stationstexte += f"&stations[]={element}"
    return f"https://www.infoclimat.fr/opendata/?method={method}&format={format}{stationstexte}&start={start}&end={end}&token={token}"

def testConnexion(reponse):
    if reponse.status_code == 200:
        data = reponse.text
        data_lines = data.split("\n")
        data2 = []
        for line in data_lines:
            data2.append(line.split(";"))
        return data2
    else:
        return f"Erreur de connexion : Code {reponse.status_code}, Contenu : {reponse.text}"

# Paramètres
method = "get"
format = "csv"
stations = ["ME099"]  # Code de la station
start = "2025-10-01"
end = "2025-10-30"
token = "3qTUcA1fgV90xJO2HvkSZVwpkxfopiUC5CEeRFoE7FYNMuf8FQ"  #ma clé personnelle

# Générer l'URL
url = geturl(method, format, stations, start, end, token)
print("URL générée :", url)  # Affiche l'URL pour vérification

# Envoyer la requête et télécharger les données
reponse = requests.get(url)

# Utiliser testConnexion pour obtenir les données
data = testConnexion(reponse)


#XLSX
print("-" * 50)
print("XLSX")
print("-" * 50)
# Afficher les données brutes """OK""""
print("\n\
Données brutes :")
for line in data[:5]:  # Affiche les 5 premières lignes
    print(line)


#Isoler les données, les titres des colonnes et les métadonnées en créant trois listes data2, titre et metadata.
metadata = []
titre = []
data2 = []

for i, ligne in enumerate(data):
    if i in [0, 1, 2, 3, 4, 6]:
        metadata.append(ligne)
    elif i == 5:
        titre = ligne
    else:
        data2.append(ligne)

print(metadata[:5])
print(titre[:5])   
print(data2[:5]) 

#Convertir les listes data2 et metadata en objet Pandas
data = pd.DataFrame(data2)
data.columns = titre
metadata_df = pd.DataFrame(metadata)

with pd.ExcelWriter("donnees_meteo_complet_csv.xlsx", engine="openpyxl") as writer:
    metadata_df.to_excel(writer, sheet_name="Metadonnees", index=False)
    data.to_excel(writer, sheet_name="Donnees", index=False)
    print("XLSX : données et métadonnées enregistrées")

print("Nombre de champs :", len(titre))
print(titre)

#Etape bonus avec json
print("-" * 50)
print("JSON")
print("-" * 50)


# Paramètres
method = "get"
format = "json"
stations = ["ME099"]  # Code de la station
start = "2025-10-01"
end = "2025-10-30"
token = "3qTUcA1fgV90xJO2HvkSZVwpkxfopiUC5CEeRFoE7FYNMuf8FQ"  #ma clé personnelle

# Générer l'URL
url = geturl(method, format, stations, start, end, token)
print("URL générée :", url)  # Affiche l'URL pour vérification

# Envoyer la requête et télécharger les données
reponse = requests.get(url)

# Utiliser testConnexion pour obtenir les données
data = testConnexion(reponse)



metadata = []
titre = []
data2 = []

for i, ligne in enumerate(data):
    if i in [0, 1, 2, 3, 4, 6]:
        metadata.append(ligne)
    elif i == 5:
        titre = ligne
    else:
        data2.append(ligne)

print(metadata[:5])
print(titre[:5])   
print(data2[:5]) 

#Convertir les listes data2 et metadata en objet Pandas
data = pd.DataFrame(data2)
data.columns = titre
metadata_df = pd.DataFrame(metadata)

with pd.ExcelWriter("donnees_meteo_complet_json.xlsx", engine="openpyxl") as writer:
    metadata_df.to_excel(writer, sheet_name="Metadonnees", index=False)
    data.to_excel(writer, sheet_name="Donnees", index=False)
    print("XLSX : données et métadonnées enregistrées")

print("Nombre de champs :", len(titre))
print(titre)