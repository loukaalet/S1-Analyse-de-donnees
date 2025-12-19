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
token = "QDH1jwcsg47lV35924EGMeLf8QKDM8L8Y0KDIWAEJzVsa1Wot1eQ"  # Ton token

# Générer l'URL
url = geturl(method, format, stations, start, end, token)
print("URL générée :", url)  # Affiche l'URL pour vérification

# Envoyer la requête et télécharger les données
reponse = requests.get(url)

# Utiliser testConnexion pour obtenir les données
data = testConnexion(reponse)

# Afficher les données brutes """OK""""
print("\n\
Données brutes :")
for line in data[:10]:  # Affiche les 10 premières lignes
    print(line)




#Problèmes pour trier les colonnes !!!!

if isinstance(data, list):
    print("-*20\n\
    Données téléchargées avec succès dans la variable 'data'.")

    # Isoler les métadonnées, les titres et les données
    metadata = [data[i] for i in [0, 1, 2, 3, 4, 6]]
    titre = data[5]
    data2 = data[7:]

    # Convertir les listes en objets Pandas
    df_data = pd.DataFrame(data2[1:], columns=titre)  # On commence à data2[1:] pour éviter de reprendre l'en-tête
    df_metadata = pd.DataFrame(metadata, columns=['Metadata'])

    # Enregistrer les objets Pandas
    df_data.to_excel('donnees.xlsx', index=False)
    df_metadata.to_csv('metadata.csv', index=False, encoding='utf-8')

    print("-*20\n\
    Les données ont été enregistrées dans 'donnees.xlsx' et les métadonnées dans 'metadata.csv'.")
else:
    print(data)  # Affiche l'erreur
