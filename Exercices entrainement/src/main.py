#utf-8

#Exercice 3 Version noob (CLEAN)
"""
import random

random_attack = True
random_damage = 0 



Joueur_1 = input("\
\n\
\n\
Insérer le nom du Joueur 1 : ")
print(f"Le joueur 1 est {Joueur_1}")
Joueur_2 = input("\n\
Insérer le nom du Joueur 2 : ")
print(f"Le joueur 2 est {Joueur_2}")

VieJ1 = int(250)
VieJ2 = int(250)


print(f"Bienvenue {Joueur_1} & {Joueur_2}!!!")

print(f"\n\
{Joueur_1} & {Joueur_2} vous commencez tous deux avec 250 points de vie")
print("En garde bande de pucelles, le combat commmence !")


#Attaque 1 (J1)

print(f"\n\
La première attaque est à {Joueur_1}")
random_attack = random.randint(0,1)
random_attack = bool(random_attack)

if random_attack == True: 
    random_damage = random.randint(0,100)
    VieJ2 -= random_damage
    print(f"Attaque réussie !!! {Joueur_2} vous avez perdu {random_damage} points vie, il ne vous reste maintenant plus que {VieJ2} points de vie : CUIDADITO")

else: 
    print(f"Attaque ratée... Sah {Joueur_1} t'es mauvais")


#Attaque 2 (J2)

print(f"\n\
La deuxième attaque est à {Joueur_2}")
random_attack = random.randint(0,1)
random_attack = bool(random_attack)

if random_attack == True: 
    random_damage = random.randint(0,100)
    VieJ1 -= random_damage
    print(f"Attaque réussie !!! {Joueur_1} vous avez perdu {random_damage} points vie, il ne vous reste maintenant plus que {VieJ1} points de vie : CUIDADITO")

else: 
    print(f"Attaque ratée... Sah {Joueur_2} t'es mauvais")

#Attaque 3 (J1)

print(f"\n\
La troisième attaque est à {Joueur_1}")
random_attack = random.randint(0,1)
random_attack = bool(random_attack)

if random_attack == True: 
    random_damage = random.randint(0,100)
    VieJ2 -= random_damage
    print(f"Attaque réussie !!! {Joueur_2} vous avez perdu {random_damage} points vie, il ne vous reste maintenant plus que {VieJ2} points de vie : CUIDADITO")

else: 
    print(f"Attaque ratée... Sah {Joueur_1} t'es mauvais")


#Attaque 4 (J2) 

print(f"\n\
La quatrième ET DERNIEREEEE attaque est à {Joueur_2}")
random_attack = random.randint(0,1)
random_attack = bool(random_attack)

if random_attack == True: 
    random_damage = random.randint(0,100)
    VieJ1 -= random_damage
    print(f"Attaque réussie !!! {Joueur_1} vous avez perdu {random_damage} points vie, il ne vous reste maintenant plus que {VieJ1} points de vie : CUIDADITO")

else: 
    print(f"Attaque ratée... Sah {Joueur_2} t'es mauvais")

#Résultats 

if VieJ1 > VieJ2:
    print(f"\n\
    VICTOIRE DE {Joueur_1}, avec {VieJ1} points de vie contre {VieJ2}")

else:
    print(f"\n\
    Victoire de {Joueur_2}..., avec {VieJ2} points de vie contre {VieJ1}")


"""

"""
#Exercice 3 Version avancée (EN COURS)

import random

random_attack = True
random_damage = 0 



Joueur_1 = input("\
\n\
\n\
Insérer le nom du Joueur 1 : ")
print(f"Le joueur 1 est {Joueur_1}")
Joueur_2 = input("\n\
Insérer le nom du Joueur 2 : ")
print(f"Le joueur 2 est {Joueur_2}")

VieJ1 = int(250)
VieJ2 = int(250)


print(f"Bienvenue {Joueur_1} & {Joueur_2}!!!")

print(f"\n\
{Joueur_1} & {Joueur_2} vous commencez tous deux avec 250 points de vie")
print("En garde bande de pucelles, le combat commmence !")



#Attaque x (J1)

for tour in range(1,5):
    if tour % 2 == 1: #Attaque J1
        print(f"\n\
        L'attaque n°{tour} est à {Joueur_1}")
        random_attack = random.randint(0,1)
        random_attack = int(random_attack)

    
        if random_attack == 1:
            random_damage = random.randint(0,100)
            VieJ2 -= random_damage
            print(f"Attaque réussie !!! {Joueur_2} vous avez perdu {random_damage} points vie, il ne vous reste maintenant plus que {VieJ2} points de vie : CUIDADITO")
        else:
            print(f"Attaque ratée... Sah {Joueur_1} t'es mauvais")


    elif tour % 2 == 0:  #Attaque J2
        print(f"\n\
        L'attaque n°{tour} est à {Joueur_2}")
        random_attack = random.randint(0,1)
        random_attack = int(random_attack)


        if random_attack == 1:
            random_damage = random.randint(0,100)
            VieJ1 -= random_damage
            print(f"Attaque réussie !!! {Joueur_1} vous avez perdu {random_damage} points vie, il ne vous reste maintenant plus que {VieJ1} points de vie : CUIDADITO")
        else:
            print(f"Attaque ratée... Sah {Joueur_2} t'es mauvais")

 
#Résultat du combat
print(f"Voici le résumé du combat {Joueur_1} a {VieJ1} de points de vie & {Joueur_2} a {VieJ2} de points de vie")

if VieJ1 > VieJ2:
    print(f"\nLe joueur {Joueur_1} GAGNE")

else:
    print(f"Le joueur {Joueur_2} GAGNE")


"""

#Exercice 4

"""
import time

commande = "à définir par un utilisateur"
Nom_Terminal = "[Défault]"
terminal_launched = True
i = 0 

#NE PAS MODIFIER UNE COMMANDE DIRECTEMENT DANS LA COMMANDE

while terminal_launched:
    commande = input(f"[{Nom_Terminal}]> ")

    if commande == "run":
        
        while i < 5:
            i += 1
            print(".")
            time.sleep(1)
        i = 0


        #OU SINON (mais plus fastidieux)

        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")

    elif commande == "name":
        Nom_Terminal = input("Saisir nouveau nom du terminal : ")
        print(f"Le nouveau nom du terminal est désormais {Modif}.")

    elif commande == "help":
        print("Voici la liste de l'ensemble de commande\n\
        run  : affiche 5x un point avec une pause entre chaque affichage de 5s\n\
        name : modifie le nom du terminal\n\
        help : affiche la liste de commande\n\
        quit : termine l'exécution du programme")

    elif commande == "quit":
        print("Ciao muchachito !")
        terminal_launched = False
        
        

    else:
        print("Cette commande est inconnue, merci de rentrer de nouveau une commande. (taper 'help' pour avoir la liste des commandes)")

    print("Nouvelle commande")


"""

"""
# Exercice 5 : Modules 

import geoshape as geo


c = 2
r = 6

print("Voici les calculs réalisé grâce au module geoshape :\n")

périmètre_cercle = geo.F_carre(c)
print("\nLes résultats des cubes/carrés\n",périmètre_cercle)

aire = geo.A_carre(c)
print("\n",aire)

volume_cube = geo.V_cube(c)
print("\n",volume_cube)

périmètre_cercle = geo.P_cercle(r)
print("\nLes résultats des sphères/cercles\n",périmètre_cercle)

aire_sphère = geo.A_sphere(r)
print("\n",aire_sphère)

volume_sphère = geo.V_sphere(r)
print("\n",volume_sphère)

"""

#EXERCICE PYTHON #6
"""
[Révision : gestion d'erreurs, classes et attributs, propriétés, méthodes]
> Vous êtes enseignant en programmation Python et un de vos étudiants vient de vous rendre un devoir. Malheureusement, le programme contient quelques erreurs, à vous de les corriger et permettre l'exécution de ce dernier.

> Le programme doit donner comme résultat l'affichage du fichier "out.txt"

> Le but de cet exercice, en plus de faire réviser les notions citées plus haut, est de vous familiariser avec le débogage d'un code qui n'a pas été fait par vous-même, et prendre l'habitude de lire les messages d'erreur retournés par l'interpréteur et savoir identifier l'origine des bugs dans le code.
"""
"""
#-------------------------------------------------------------------------------------
# CLASSE OBJET POUR JOUEUR
#-------------------------------------------------------------------------------------
class Weapon:
    def __init__(self, name, damages, sell_price):
        self.name = name
        self.damages = damages
        self.sell_price = sell_price

#-------------------------------------------------------------------------------------
# CLASSE JOUEUR
#-------------------------------------------------------------------------------------
class Player:
    def __init__(self, name, value = 200 , level = 1, golds = 5, HP = 100, maxHP = 100, MP = 100, EXP = 0, weapon = Weapon("Épée en bois", 32, 1)):
        self._name = name
        self.value = value
        self.level = level
        self.golds = golds
        self.HP = HP
        self.maxHP = maxHP
        self.MP = MP
        self.maxMP = MP
        self.EXP = EXP
        self.next_level_EXP = 100
        self.weapon = weapon
        

    def get_name(self):
        return self._name

    def set_name(self, name):
        if len(name) > 16:
            raise Exception("Le nom de votre personnage doit comporter 16 caractères max")

        self._name = name
        print(f"Vous changez de nom pour -> {self.name}")

    name = property(fget = get_name, fset = set_name)

    def to_string(self):
        print("----------------------------------------------")
        print("Nom : {}\nNiveau : {}\nOr : {}\nPV : {}\nPM : {}".format(self.name, self.level, self.golds, self.HP, self.MP))
        print("EXP : {}\nProchain niveau : {} EXP\nObjet équipé : {}\n".format(self.EXP, self.next_level_EXP, self.weapon.name))

    def say(self, message):
        print(f"{self.name} : {message}")

    def equip(self, weapon):
        print("{} a été vendu(e), vous empochez {} pièce(s) d'or.".format(self.weapon.name, self.weapon.sell_price))
        self.golds += self.weapon.sell_price
        self.weapon = weapon
        print("{} équipé !".format(self.weapon.name))

    def attack(self, target):
        print("{} attaque {} avec {} !".format(self.name, target.name, self.weapon.name))
        print("L'attaque inflige {} points de dégâts !".format(self.weapon.damages))

        target.HP -= self.weapon.damages

        if target.HP <= 0:
            target.die()

    def heal(self, value):
        self.HP += value
        if self.HP > self.maxHP:
            self.HP = self.maxHP
        print("{} : vous vous soignez et regagnez {} points de vie !".format(self.name, self.value))

    def level_up(self):
        if self.EXP >= self.next_level_EXP:
            self.next_level_EXP = 0
            self.level += 1
            print("{} monte au niveau {} !".format(self.name, self.level))
    

    def die(self):
        if self.HP <= 0:

            print("{} succombe de ses blessures...".format(self.name))
            print("FIN DE LA PARTIE !")


#-------------------------------------------------------------------------------------
# PARTIE PRINCIPALE (NE PAS MODIFIER !)
#-------------------------------------------------------------------------------------

# Création des personnages
hero = Player("Joueur", 5, 3, 200, 70)
monster = Player(name = "Golem de pierre", MP = 0, weapon = Weapon("Massue", 40, 25))

# Affichage des infos des personnages
hero.to_string()
monster.to_string()

# Changement du nom du héros
ask_player_name = True

while ask_player_name:
    try:
        player_name = input("Choisir un nom de point de 16 caractères : ")
        hero.name = player_name
        ask_player_name = False
    except Exception as message:
        print(message)

# Conversation entre le héros et le golem
print("\n", end='')
monster.say("Qui ose troubler mon profond sommeil?")
hero.say("Moi ! Le héros de cette histoire !!")
monster.say("Je vois...")
hero.say("Alors en garde, vil gredin !")

# Attaque du héros contre le monstre
hero.attack(monster)
hero.attack(monster)

# Mais ce dernier se soigne et contre-attaque
monster.heal(50)
monster.heal(50)
monster.attack(hero)

# Infos des personnages mises à jour
hero.to_string()
monster.to_string()

# Notre héros trébuche sur une bosse, et découvre à moitié enterré, un arc
# Il décide de l'équiper...
thunder_bow = Weapon("Arc de foudre", 240, 350)
hero.equip(thunder_bow)

# Et balance une nouvelle attaque dévastatrice !
hero.say("Meurs, monstre !")
hero.attack(monster)

# Le héros remporte le combat et gagne de l'EXP (montée de niveau)
hero.EXP = 131
hero.level_up()
"""
"""
#Exercice 7 : classes

import random

class Bouftous:


    def __init__(self, PV = random.randint(540,610), PA = 8, PM = 4):
        print("Creation d'un BOUFTOU")
        self.pv = PV
        self.pa = PA
        self.pm = PM

        

B1 = Bouftous()
print(f"ses caractéristieques sont PV = {B1.pv} PM = {B1.pm} & PA ={B1.pa}.")

class BouftouRoyal (Bouftous):
    def __init__(self):
        Bouftous.__init__(self, random.randint(10,100), 6, 24)
        print("Creation d'un bouftou ROYAL")
        self.pv = PV
        self.pa = PA
        self.pM = PM
    


class BouftouNoir (Bouftous):
    def __init__(self):
        Bouftous.__init__(self, random.randint(10,150), 5, 12)
        print("Creation d'un bouftou ROYAL")
        self.pv = PV
        self.pa = PA
        self.pM = PM

B2 = Bouftous()
B3 = Bouftous()
B4 = Bouftous()

print(type(B1))
print(type(B2))
print(type(B3))
print(type(B4))
"""
# Exercice 8 


"""
affcicher la liste
trier par ordre alphabétique 
combien d'éléments
chercher l'élément bryan
supprimer les éléments qui commence par J (puis vérifier en affichant la liste)
transformer mike en michael
Ajouter les prénoms Bryan Junior, Henri et Kumiko
créer une nouvelle liste des prénims de plus de 5 lettres et l'afficher
Retrouver Bryan Junior et Francoise pour former un couple

#Définir liste + l'enregistrer

people = list
people = ["Laura", "Camille", "Bryan", "Josh", "Amelia", "Kamel", "Nami", "Clint", "Mike", "Samia", "Jean-Charles", "Quentin", "Ben", "Marie", "Françoise", "Jordana", "Farid"]

#Afficher la liste
print (people)

#Trier la liste 
people.sort()
print(people)

#Compter les éléments présents
print(f"\nIl y a {len(people)} éléments.")

#Chercher l'élement Bryan
if "Bryan" in people:
    print(f"\nBryan est un élément présent")
else:
    pass

print(f"Bryan est en position {people.index("Bryan")}\n\n\n")


#supprimer les éléments qui commence par J (puis vérifier en affichant la liste)


supprimerJ= "J"
people = [word for word in people if not word.startswith(supprimerJ)]

print(f"Voici la liste sans les mots commençants par J :\n{people}")


#transformer mike en michael
#trouver la position de mike 
positionMIKE = people.index("Mike")
print(f"la positon de mike est {positionMIKE}")
#remplacer mike
people [positionMIKE] = ["Michael"]
print(people)



#supprimer mike
int(positionMIKE) 
positionMIKE = positionMIKE +1
del people[positionMIKE]
print(people)


#Ajouter les prénoms Bryan Junior, Henri et Kumiko
people.append("Bryan Junior")
people.append("Henri")
people.append("Kumiko")
print(people)

#créer une nouvelle liste des prénpms de plus de 5 lettres et l'afficher
people = [objet for objet in people if len(objet) > 5]
print(f"Voici la liste FINALE : {people}")

#Retrouver Bryan Junior et Francoise pour former un couple
"""
"""
EXERCICE PYTHON #9
[Révision : tuples]

> Écrire quelques fonctions pour effectuer des manipulations sur le tuplet donné plus bas :
	1. chercher le caractère voulu et retourner vrai s'il est trouvé, faux sinon
	2. renvoyer un tuple concaténant les éléments de "letters" et de l'élément 'k' (à créer dans un second tuple)
	3. remplacer le n-ième élément de "letters" par un 'X'
	
> Indications :
	- gardez en tête ce qu'est un tuple et soyez logiques dans ce que vous voulez écrire
"""

"""
# Fonction n°1
def find_value(letters, element):
	pass

#--------------------------------------------------------
# Fonction n°2
def get_new_tuple(letters):
	# créer ici un tuple qui contient l'élement 'k'
	pass

#--------------------------------------------------------
# Fonction n°3
def set_letter(letters, n):
	pass

#----------------------------------------------------------------------------------

tuple_letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')

# Appel à la fonction n°1
print("\n=== Fonction 1 ==========")

if find_value(tuple_letters, 'e'):
	print("L'élement 'e' existe")
else:
	print("L'élément 'e' n'a pas été trouvé")

if find_value(tuple_letters, 'p'):
	print("L'élement 'p' existe")
else:
	print("L'élément 'p' n'a pas été trouvé")

#--------------------------------------------------------
# Appel à la fonction n°2
print("\n=== Fonction 2 ==========")

new_tuple_letters = get_new_tuple(tuple_letters)
print(f"Nouveau tuple : {new_tuple_letters}")

#--------------------------------------------------------
# Appel à la fonction n°3
print("\n=== Fonction 3 ==========")

print(f"Avant : {tuple_letters}")
set_letter(tuple_letters, 2)
print(f"Après : {tuple_letters}\n")


"""
"""
#Exercice python while

feuille = 1
feuille = float(1)
TourEiffel = float(365 * 1000)
CompteurPliage = 0

while feuille < TourEiffel :
    print(f"La taille de feuille est de {feuille} mm. Il faut donc encore doubler...\n\n")
    feuille *= 2
    CompteurPliage += 1

else:
    print(f"La feuille est maintenant d'une taille supérieure à celle de la tour, avec {feuille} mm contre {TourEiffel}.\
    \nCela a été fait en {CompteurPliage} pliages.")



#Exercice python for VS while

#Définir les éléments à mobiliser
valeur = float(100000)

#Trouver quand la valeur de l'investissement au bout de 10 ans
for i in range(10): 
    valeur = valeur * (1 + 1/100)
    print(f"En année {i} la valeur est de {valeur} €.")
while i < 9:
    pass
else:
    print(f"La {i}e année l'investissement vaut{valeur}\n\n")


#Trouver quand est-ce que l'investissemet surpassse les 200€
i = 0

valeur = 100000
while valeur < 2000000:
    valeur = valeur * (1 + 1/100)
    i += 1
    print(f"En année {i} la valeur est de {valeur} €. Continuez à investir")

else: 
    print(f"\n\nLa valeur a doublée au bout de {i} ans.")




#Exercice probabilités lièvre

#Définir les variables à utiliser
compteur_lièvre = 0
tirage_lièvre = 0
compteur_tortue = 0
tirage_tortue = 0
ordre_lièvre = 0
ordre_tortue = 0
test6 = 0

import random
tour = 1


#Programme partie 1 

#Trouver aléatoirement l'animal qui commencera 
tour = int(random.randint(0,1))
    
if tour % 2 == 1:
    ordre_lièvre = 1
    ordre_tortue = 1

elif tour % 2 == 0:
    ordre_lièvre = 0
    ordre_tortue = 0
    
tour = 1 

#Faire les tirages
while compteur_lièvre < 6 and compteur_tortue < 6:
    
    #s'assurer que le lièvre commence, et que la tortue commencera
    if ordre_lièvre % 2 == 0:

        ordre_lièvre += 1
        ordre_tortue += 1

        #trouver combien va gagner le lièvre
        tirage_lièvre = random.randint(1,6)

        #test si compteur lièvre > 6
        test6 = tirage_lièvre + compteur_lièvre
        if test6 > 6:
            compteur_lièvre = 6 
        else:
            compteur_lièvre += tirage_lièvre

        
        print(f"Tour {tour} : Le lièvre a avancé de {tirage_lièvre} est en position {compteur_lièvre}")


    #s'assurer que la tortue commence, et que le lièvre commencera
    elif ordre_tortue % 2 == 1:
        
        ordre_lièvre += 1
        ordre_tortue += 1

        #trouver combien va gagner la tortue
        tirage_tortue = random.randint(1,6)

        #test si compteur tortue > 6
        test6 = tirage_tortue + compteur_tortue
        if test6 > 6:
            compteur_tortue = 6 
        else:
            compteur_tortue += tirage_tortue

        print(f"Tour {tour} : La tortue a avancé de {tirage_tortue} est en position {compteur_tortue}")
    else:
        pass
        
    tour += 1

#Annoncer le gagnant
else:
    if compteur_lièvre >= 6:
        print("Bravo au lièvre")
    elif compteur_tortue >= 6:
        print("Bravo à la tortue")
    else:
        pass


#Exercice tables de multiplcations
 
import random

comptage_de_points = 0
zero = 0
i = 0

print("\n\
Bienvenue dans le module d'entrainement aux tables de mutliplication de 1 à 10\
\n")

for i in range(10):
    try:   
        
        
        #Faire un tirage et trouver son résultat
        tirage_A = random.randint(1,10)
        tirage_B = random.randint(1,10)
        résultat = tirage_A * tirage_B

        #Demander à l'utilisateur de le calculer
        calcul = input(f"> Combien font {tirage_A} x {tirage_B} ? Entrez votre réponse en chiffres : ")

        #Pour que l'erreur puisse être levée
        calcul = int(calcul)

        if calcul == str(résultat):
            comptage_de_points += 1
            print(f"{tirage_A} x {tirage_B} est effectivement égal à {résultat}, bravo bonne réponse !!!")
            
        #S"assurer que les points soient comptés de façon logique
        elif calcul != résultat:
            print("réponse incorrecte, réessayez !!")
            zero = comptage_de_points - 1
            if zero > 0:
                comptage_de_points -= 1
            elif zero <= 0:
                comptage_de_points = 0

    except ValueError:
            print("réponse non reconnue, recommencez.")
    
    #compteur de tours et nombre de points
    i += 1
    print(f"Fin du tour {i}, il vous reste {10 - i} tours, vous avez maintenant {comptage_de_points} points.\n")
    

#terminer le jeu après 10 tours
print(f"Vous avez terminé le jeu avec {comptage_de_points} points.")



#Exercice aire 

from random import *
test = 0
i = 0


for i in range(10000):

    #Trouver une coordonnée
    x = random()
    y = random()
    print(f"les nombres tirés sont {x} et {y}.")
    
    
    #Observer si en dehors ou dans l'aire
    if y <= x**2 :
        test += 1
        print(f"lors du test {i} il est dans la zone d'aire.")
    else:
        print(f"lors du test {i} il est en dehors de la zone d'aire.")

    i += 1

print(f"La fréquence est de {test / i}. Donc, la surface de la fonction carrée sous contraintes ]0 ; 1[ est égale à {(test / i) * 1}.")




#Exercice tracer la courbe d'une fonction


import numpy as np
import matplotlib.pyplot as plt

#Définir des points
x = np.linspace(-5,5,100)
y = x**2

x2 = np.linspace(-5,5,100)
y2 = 1- (x**2)

#Tracer les courbes
plt.plot(x,y,'r.')
plt.plot(x2,y2,'b.')

#Enregistrer la courbe
plt.savefig("courbe.png")


#Exercice tracer un cercle
from pylab import * 
import numpy as np
import matplotlib.pyplot as plt

#Définir des points du cercle
a = np.linspace(0,2*pi,100)
x = cos(a)
y = sin(a)

x1 = np.linspace(-50,50,1000)
y1 = x1 * 10


x2 = np.linspace(-5,5,100)
y2 = 1- (x**2)
plt.plot(x2,y2,'b.')

#Tracer les courbes
plt.plot(x,y,'r.')
plt.plot(x1,y1,'b.')

#Enregistrer la courbe
plt.savefig("courbe2.png")

  
#Exercice essayer de tracer un carré 

from pylab import *
import matplotlib.pyplot as plt

#Côté 1
c1 = linspace(-10,10,10)
c11 = linspace(-10,-10,10)
plt.plot(c1,c11,'r.')


#Côté 2
c2 = linspace(-10,10,10)
c22 = linspace(10,10,10)
plt.plot(c2,c22,'r.')

#Côté 3
c3 = linspace(-10,-10,10)
c33 = linspace(-10,10,10)
plt.plot(c3,c33,'r.')

#Côté 4
c4 = linspace(10,10,10)
c44 = linspace(-10,10,10)
plt.plot(c4,c44,'r.')


c5 = linspace(-50,50,10)
c55 = c5 * 2
plt.plot(c5,c55,'w.')


plt.savefig("carre.png")



#Exercice tracer un cercle
from pylab import * 
import numpy as np
import matplotlib.pyplot as plt

#Trouver les données
x = linspace(-1,1,1000)
y = sqrt(1 - x**2)

#Vérifier les données
"""
print(x)
print(y)
print(-y)
"""

#Tracer les courbes
plt.plot(x, y)
plt.plot(x,-y)

show()

#plt.savefig("cercle2.png")
""" 

#Créer une liste et la modifier
from copy import deepcopy
import random 

notes = [random.randint(0,20) for i in range(30)]
print(notes)

nouvelles_notes = deepcopy(notes)
print(notes)
print(nouvelles_notes)


nouvelles_notes = [x for x in nouvelles_notes if x >= 10]
print(nouvelles_notes)

#Autre technique
import random 

notes = [random.randint(0,20) for i in range(30)]
print(notes)
for i in notes:
    if i>= 10 
        nouvelles_notes = nouvelles_notes + [i]
print(nouvelles_notes)


        

       





