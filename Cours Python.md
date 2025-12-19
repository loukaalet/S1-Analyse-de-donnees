#coding:utf8

Cours Python



Toujours commencer par #coding:utf-8



\# -> commentaire sur une ligne

""" """ -> commentaire sur plusieurs ligne



\\n saut à la ligne

\\p tabulation





Variables :

\- doit commencer par une lettre ou un underscore

\- ne doit pas contenir de caractères spéciaux

\- ne doit pas contenir d'espaces

\- possibilités d'utiliser des majuscules ou underscore pour mettre en avant un terme



Types de données :

\- entier numérique (int)

\- nombre flottant (float)

\- chaîne de caractères (str)

\- booléen (bool)





Le type de donnée définit,de fait nous conduira à effectuer des manipulations spécifiques à ce qu'il représente (eg: impossible de faire des calculs avec un type str(texte)).



Grâce à la commande print() il est possible d'afficher une variable. Si on rajoute dans la commande du texte grâce à "" (puis mettre une virgule /!\\) alors il est possible d'affiche à la fois du texte et la variable. Eg print("Le chat est"; couleurChat) -> Le chat est noir



Possibilité de faire la même chose grâce à des objets :

1\. définir une variable texte eg: texte = "Le chat est {}." ; et la variable classique couleurChat = "noir"

2\. Afficher le texte avec print, puis utiliser "format" et y insérer la variable que l'on souhaite afficher. Eg print(texte.format(couleurChat))



OU SINON 



directement inscrire 

Soit -> print("texte à afficher {}.".format(variable)

eg : print("Le chat est {}.".format(couleurChat)





LISTE FONCTIONS

input() -> lire au clavier

1\. nomVariable = input ("texte à afficher pour l'utilisateur")

2\. print("texte à afficher pour l'utilisateur", nomVariable)

/!\\ par défaut le type de données que reçoit la fonction est du texte (str), il faut donc "caster" (convertir) les données si on veut les utiliser avec d'autres choses que du texte



print () -> afficher à l'écran



type () -> retourne le type d'une donnée, variable…

str.format -> formater une chaîne



CASTER une donnée avec int/float/str/bool ()



1.Récupérer la donnée (soit définit en amont, soit avec input…)

2\. Caster la donnée nomVariable = int(nomVariable)



Eg prix HT --> TTC

1\. PrixHT = Input("prix à afficher")

2\. PrixHT = int(PrixHT)

3\. PrixTTC = PrixHT + PrixHT\*0,2



EG Booléen en texte

1.valeurbooleen = True

2.valeurbooleen = str(valeurbooleen)

3.print(valeurbooleen)

3.S'affichera 1, au lieu de True



OPERATEURS 



Comme sur Excel : + ; - ; \* ; / .

SAUF pour le "modulo" -> % (le reste de la division euclidienne)

S'utilise ainsi :

1\. calcul = 10/3

2\. calculR = 10%3

3\. print ("Résultat", calcul, "dont reste" , calculR)



Pour faire des calculs d'opérateurs, il est également possible de faire des calculs sur les variables.

Eg : 

Prix = 5 

Nouveau prix :

Prix = 5 + 1

OU 

Prix = prix + 1



/!\\ pour aller plus vite on peut inscrire directement : prix += 1 (possible avec toutes les opérations)



CONDITIONS

liste opérateurs de comparaison :

\- ==

\- !=

\- <

\- >

\- <=

\- >=



/!\\ possibilité de faire des fourchettes. Eg: if 5 < age < 18: (au lieu de if age < 5 and age > 18



"if x == x :" -> opérateur de comparaison /!\\ ne pas oublier les deux points qui exécutent la commande

Pour indiquer ce qu'il se passe quand la comparaison est validée on va à la ligne, tabulation, puis taper le code. 

Eg :

if x == x :

&nbsp;	print("x est correct") 



liste conditions multiples :

and (ET)

or (OU)

in / not in (DANS / PAS DANS)



liste mots clés conditions :

\- if (si)

\- else (sinon)

\- elif (sinon si -> deuxième condition)-> possibilité de mettre plusieurs elif 







fonctionne également avec des booléens :

majeur = True 



if majeur:

&nbsp;	print("vous pouvez voter")

else:

&nbsp;	print("vous ne pouvez pas voter")



BOUCLES :

S'utilise avec

\- while

\- For (For x in y)

\- Break/continue



on doit mettre en place un compteur pour arrêter la boucle !!!



While Eg: boucle qui se répète 



i : 0



while i < 10:

&nbsp;	print("Baka")

&nbsp;	i += 1





Il est possible de créer des boucles qui ne se répètent pas.



While Eg : 



Egibilité = True



while Egibilite: 



choixMenu = input("Quel personnage politique êtes vous ?")

&nbsp;	

&nbsp;	if choixMenu == "Macron":

&nbsp;		print ("Démission !!!")

&nbsp;	elif choixMenu == "Lepen":

&nbsp;		Egibilite = False

&nbsp;	elif choixMenu == "Sarko":

&nbsp;		Eligilite = False

&nbsp;	Else:

&nbsp;		print("Bravo tu n'es pas corrompu!!!")

&nbsp;		



print("perdu, "insérer réplique de Poutou sur l'Europe et les caisses")



Eg for  :

phrase = "Le chat mange"



for lettres in sentence:

&nbsp;	print(letter)





FONCTIONS 

se crée avec def puis retour à la ligne puis tabulation



on peut faire des sorties par défaut en précisant des paramètres optionnel avec =   

Eg : def dire (nom\_personne="Tom"):



Quand on ne précis rien, ce sera donc des paramètres obligatoires! (on devra obligatoirement rentrer des paramètres)



Quand on inscrit les paramètres obligatoires de la fonction, il vaut mieux les écrire dans le même ordre que celui de la fonction. Cependant si on précise à quel paramètre il font référence ("x"=argumentX) alors python les présentera correctement



Quand le nombre d'éléments dans la liste varie, on peut mettre une étoile avant le paramètre, puis utiliser la fonction for - in afin que tous les éléments présents soit affichés. 

Eg

def direAgeParticipants(\*listeAge):

&nbsp;	for age in listeAge

&nbsp;	print (age)



direAgeParticipants("19","30","49")





Lambda (Fonction prédéfinie )

Mettre lambda suivi des paramètres que l'on souhaite mobiliser, puis de ce qu'ils doivent effectuer 

eg : calcuer = lambda A, B: A + B





MODULES :

sert à importer des fichiers de fonctions  



import <nomModule>  

from <nomModule> import <nomFonction>

from <nomModule> import \*



EG : 



import math



resultat = math.sqrt(x)



print(resultat)





EG aussi :

from math import sqrt 



resultat = sqrt(x)



print(resultat)



EG : 



from math import \*



resultat = sqrt(x)



print(resultat)





on peut créer son propre module et importer ses fonctions dans d'autres fichiers. 



Pour cela on crée un fichier texte et utilise def pour créer des fonctions





/!\\ il est possible de réduire le nom des modules importés, notamment lorsque 'ils sont dans un sous dossier. 

Eg :

le dossier géomatique est dans le dossier module, alors on devra l'importer depuis modules.geomatique

Une fois que c'est fait on peut définir ce chemin grâce àce  ce qui suit 

import modules.geomatique as geo



Il faut tester chaque module indépendamment du programme principal et des autres modules afin de vérifier qu'il fonctionne et ne vas pas corrompre le fichier







**Attributs et classes sur objet :**



En gros créer des grandes familles/poupées russes (La classe) ou des éléments (les objets) ont des attributs (de classe ou personne)



La création est assez similaire à la création de fonctions



/!\\ l'attribut dans la classe et l'attribut une fois désigné pour un objet, n'est pas le même (pour éviter la confusion on peut mettre deux noms différents eg épee et classe\_épée)



On peut aussi créer des attributs généraux pour toute une classe (eg compteur d'humains, à chaque création on comptera un humain supplémentaire). Il faut compter le mettre dans la classe



class NomClasse:

&nbsp;	

&nbsp;	compteurH = 0



&nbsp;	def \_\_init\_\_(self, C\_attribut 1, C\_attribut 2...)

&nbsp;	self.attribut 1 = C\_attribut 12

&nbsp;	self.attribut 2 = C\_attribut 1

&nbsp;	NomClasse.compteurH += 1

#Créer des visualisations statistique

#La base est d'importer la bibliothèque



import matplotlib.pyplot as plt 
=> désormais on utilisera plt



#Construire les données
- graphique : plt.type(x, y, color='couleur souhaitée')

- les possibilités de type :
    - plot (courbe)
    Il y a 3 éléments modifialbes 
    - bar
       Il y  5 éléments modifiables plt.bar(x, y, width=taille, color='couleur barre', edgecolor='couleur contour')

    - hist

    - stem
        Il y a 5 éléments modifiables plt.stem(x, y, linefmt='couleur', markerfmt='élément en haut', bottom=taille de la base


#Créer un espace (ou figure) pour y dessiner un graphique
    fig, ax = plt.subplots() → « Crée une figure vide et un espace pour y dessiner mon graphique : je pourrais alors distinguer l'espace de création graphique et le graphique (très pratique si dois afficher plusieurs graphiques qui ont donc des caractéristiques différentes)

    fig = l'espace où on dessine des ax 
    ax = un graphique

    fig, ax = plt.subplots(figsize=(x, y)) => taille de la figure 
    fig.suptitle("xxx") => Titre global de la figure, pas besoin si j'ai que un axe

    pour créer et modifier des axes 
        fig, (ax1, ax2) = plt.subplots(1, 2)
        ax1.set_title("Graphique 1") => titre du 1er graphique
        ax2.set_title("Graphique 2") => titre du 2e graphique

#Constuire les éléments annexes du graphique
    plt.xlabel("Valeurs")
    plt.ylabel("Probabilité")
    plt.title("Eg : Loi uniforme discrète U({1,...,10})")
    plt.grid(True, linestyle=':')

#Définir la taille du graphique
    plt.xlim(0, 0)
    plt.ylim(0, max(pmf)*1.2)



#On termine par afficher le graphique
    plt.show()
