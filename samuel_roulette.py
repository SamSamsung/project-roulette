import random

# On donne le capital = 1 000 Tunes

print("Votre capital initial est de 1 000 T")
capital = 1_000


# La fonction demander_nom permet de récupérer le nom de l'utilisateur

def demander_nom():
    prenom = str(input("Quel est votre prénom ? "))
    return prenom


# On stock le prénom entré par l'utilisateur pour ne pas avoir à réutiliser la fonction.

prenom = demander_nom()

# On affiche le schéma et les règles qui permettront au jouer de se décider

print("°°°°°Bienvenue à la roulette du casino de l'EIB°°°°°,", prenom)

print("""           ----------------------
           |          0         |
---------------------------------
  M  |     |   1  |   2  |   3  |   L1
  A  |  T  |   4  |   5  |   6  |   L2
  N  |  1  |   7  |   8  |   9  |   L3
  Q  |     |  10  |  11  |  12  |   L4
  U  |---------------------------
  E  |     |  13  |  14  |  15  |   L5
-----|  T  |  16  |  17  |  18  |   L6
     |  2  |  19  |  20  |  21  |   L7
  P  |     |  22  |  23  |  24  |   L8
  A  |---------------------------
  S  |     |  25  |  26  |  27  |   L9
  S  |  T  |  28  |  29  |  30  |   L10
  E  |  3  |  31  |  32  |  33  |   L11
     |     |  34  |  35  |  36  |   L12
---------------------------------
              C1     C2     C3


Pair
Impair
Manque : 1-18
Passe : 19-36
Rouge : 1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36
Noir : 2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35


Liste des paris :
	  - Si vous misez sur Numéro simple (Rapporte 36 fois la mise) : Saisir Plein et à la deuxième question un numéro entre 0 et 36 (Plein             36)
	  - Si vous misez sur Pair, vous remportez 2 fois la mise : Saisir P
	  - Si vous misez sur Impair, vous remportez 2 fois la mise : Saisir I
	  - Si vous misez sur Manque (Numéros de 1 à 18), vous remportez 2 fois la mise : Saisir M
	  - Si vous misez sur Passe (Numéros de 19 à 36), vous remportez 2 fois la mise : Saisir S
	  - Si vous misez sur Rouge, vous remportez 2 fois la mise : Saisir R
	  - Si vous misez sur Noir, vous remportez 2 fois la mise : Saisir N
	  - Si vous misez sur Tiers, vous remportez 3 fois la mise : Saisir Tiers et à la deuxième question le numéro du tiers (Tiers               2)
	  - Si vous misez sur Colonne, vous remportez 3 fois la mise : Saisir Colonne et à la deuxième question le numéro de la colonne (Colonne    3)
	  - Si vous misez sur Ligne, vous remportez 12 fois la mise : Saisie Ligne et à la deuxième question le numéro de la ligne (Ligne           7)
	 """)


# On créer une fonction est_pair pour vérifier si n est pair.

def est_pair(n):
    return n % 2 == 0 and n != 0


# On créer une fonction est_impair pour vérifier si n est imppair.

def est_impair(n):
    return n % 2 == 1


# On créer une fonction est_passe pour vérifier si n est passe.

def est_passe(n):
    return n >= 19 and n <= 36


# On créer une fonction est_manque pour vérifier si n est manque.

def est_manque(n):
    return n >= 1 and n <= 18


# On créer une fonction est_rouge pour vérifier si n est rouge.

def est_rouge(n):
    return n == 1 or n == 3 or n == 5 or n == 7 or n == 9 or n == 12 or n == 14 or n == 16 or n == 18 or n == 19 or n == 21 or n == 23 or n == 25 or n == 27 or n == 30 or n == 32 or n == 34 or n == 36


# On créer une fonction est_noir pour vérifier si n est noir.

def est_noir(n):
    return not est_rouge(n)


# On créer une fonction num_tiers pour retourner le numéro du Tiers.

def num_tiers(n):
    for i in range(1, 4):
        if n <= i * 12:
            return i


# On créer une fonction num_ligne pour retourner le numéro de la ligne.

def num_ligne(n):
    for i in range(1, 13):
        if n <= i * 3:
            return i


# On créer une fonction num_colonne pour retourner le numéro de la colonne.

def num_colonne(n):
    if n == 1 or n == 4 or n == 7 or n == 10 or n == 13 or n == 16 or n == 19 or n == 22 or n == 25 or n == 28 or n == 31 or n == 34:
        return 1
    if n == 2 or n == 5 or n == 8 or n == 11 or n == 14 or n == 17 or n == 20 or n == 23 or n == 26 or n == 29 or n == 32 or n == 35:
        return 2
    if n == 3 or n == 6 or n == 9 or n == 12 or n == 15 or n == 18 or n == 21 or n == 24 or n == 27 or n == 30 or n == 33 or n == 36:
        return 3


# La fonction tirer_numéro sert a simuler le lancer la bille.

def tirer_numero():
    numero = random.randint(0, 36)
    return numero


# La fonction calculer_gain permet de calculer le résultat. En fonction du capital, du pari gagnant ou perdant et de
# la mise, il retourne le capital du joueur.

def calculer_gain():
    Gain = 0 - Mise
    if Pari == "Plein":
        if Nombre == numero:
            Gain = Mise * 12 - Mise
    elif Pari == "Ligne":
        if Nombre == num_ligne(numero):
            Gain = Mise * 12 - Mise
    elif Pari == "Colonne":
        if Nombre == num_colonne(numero):
            Gain = Mise * 3 - Mise
    elif Pari == "Tiers":
        if Nombre == num_tiers(numero):
            Gain = Mise * 3 - Mise
    elif Pari == "P":
        if est_pair(numero):
            Gain = Mise * 2 - Mise
    elif Pari == "I":
        if est_impair(numero):
            Gain = Mise * 2 - Mise
    elif Pari == "M":
        if est_manque(numero):
            Gain = Mise * 2 - Mise
    elif Pari == "S":
        if est_passe(numero):
            Gain = Mise * 2 - Mise
    elif Pari == "R":
        if est_rouge(numero):
            Gain = Mise * 2 - Mise
    elif Pari == "N":
        if est_rouge(numero):
            Gain = Mise * 2 - Mise
    return Gain


# La fonction afficher_tirage permet d'afficher les caractéristes que détient le numéro tiré en fonction du Pari et
# des fonctions num_ligne, num_colonne, num tiers et calculer_gain..

def afficher_tirage():
    print("Numéro tiré : ", numero)
    if numero == 0:
        print("0 ne correspond à aucun pari sauf celui de choisir un nombre entre 0 et 36")
    else:
        if est_rouge(numero):
            print("Rouge")
        else:
            print("Noir")
        if est_pair(numero):
            print("Pair")
        else:
            print("Impair")
        if est_passe(numero):
            print("Passe")
        else:
            print("Manque")
        print("Ligne : ", num_ligne(numero), ", colonne : ", num_colonne(numero), ", tiers : ", num_tiers(numero))
    print(prenom, "votre nouveau capital est de :", calculer_gain() + capital, "T")


# Cette boucle ittérative permet de répéter les paris et les mise 10 fois puis, à la fin, demande au joueur s'il veut
# continuer. La boucle while est inutile car j'ai vérifié dans la boucle ittérative si le capital était égal à zéro.
# J'ai fait cela car je la boucle while attendait que les dix tours passent pour vérifier la condition (capital > 0),
# j'ai donc utilisé une boucle while qui ne s'arrete jamais pour que la boucle ittérative se répète si l'on input "Oui"

jouer = True

while jouer:
    for i in range(0, 10):

        # On récupère son Pari et sa mise.

        print(prenom, ", saisissez votre pari (une saisi invalide entrainera une perte de la mise) : ")
        Pari = str(input())
        if (Pari == "Ligne") or (Pari == "Colonne") or (Pari == "Tiers") or (Pari == "Plein"):
            print(prenom, ", saisissez un numéro")
            Nombre = int(input())
        print(prenom, ", combien voulez vous miser ? (mise maximale : 500) : ")
        Mise = int(input())

        # On affecte à la variable "numero", la fonction tirer_numero pur qu'un nouveau chiffre soit donné à chaque
        # tour.

        numero = tirer_numero()

        # Ces deux boucles while empechent l'utilisateur de parier au dessus de 500, en dessous de 0 et de parier
        # plus que son capital

        while Mise > 500 or Mise <= 0:
            print(prenom, ", votre mise maximale est : 500. Ressaisissez une mise valable : ")
            Mise = int(input())
        while Mise > capital:
            print(prenom, ", vous n'avez pas assez de T. Ressaisissez une mise valable : ")
            Mise = int(input())
        print("Les jeux sont faits ! ")

        afficher_tirage()
        capital = calculer_gain() + capital

        if capital == 0:
            print("Vous n'avez plus d'argent, à bientôt")
            jouer = False

    # A la fin des 10 tours, le programme propose à l'utilisateur s'il veut continuer la partie.

    Reponse = str(input("Voulez-vous continuer la partie ? Oui = Y et Non = N : "))
    if (Reponse == "N") or (Reponse == "Non") or (Reponse == "No"):
        print("Merci d'avoir joué !")
        jouer = False
    elif (Reponse == "O") or (Reponse == "Oui") or (Reponse == "Yes") or (Reponse == "Y"):
        print("La même question vous sera posée dans 10 tours ! Tachez de ne pas perdre vos gains !")

# IL N'Y A PAS DE .UPPER() Monsieur
