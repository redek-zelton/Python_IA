# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 15:22:16 2020

@author: #nom
"""
from math import floor
from random import random
import copy
#### puissance 4 #### 
grille=[["-" for i in range (12)] for j in range (6)]

#Parametres du jeu
joueurCourant = 1

def parametres():
    global joueur1Algo, joueur2Algo, joueur1Profondeur, joueur2Profondeur, joueur1Heuristique, joueur2Heuristique, joueur1Bot, joueur2Bot
    
    print("Saisir le mode de jeu du joueur 1 :")
    print("0. Manuel")
    print("1. Coup Naif")
    print("2. Alpha Beta")
    joueur1Algo=int(input())        #par defaut 0
    
    joueur1Bot=False
    if joueur1Algo!=0:
        joueur1Bot=True
        
    if joueur1Algo==2:
        print("Saisr l'heuristique pour le joueur 1 :")
        print("1. Tableau d'évaluation")
        print("2. Nombre de cases alignées")
        joueur1Heuristique=int(input())     #par defaut 1
        
        print("Saisir la profondeur de l'élagage du joueur 1 :")
        joueur1Profondeur=int(input())      #par defaut 0
    
    print("Saisir le mode de jeu du joueur 2 :")
    print("0. Manuel")
    print("1. Coup Naif")
    print("2. Alpha Beta")
    joueur2Algo=int(input())        #par defaut 0
    
    joueur2Bot=False
    if joueur2Algo!=0:
        joueur2Bot=True
        
    if joueur2Algo==2:
        print("Saisr l'heuristique pour le joueur 2 :")
        print("1. Tableau d'évaluation")
        print("2. Nombre de cases alignées")
        joueur2Heuristique=int(input())     #par defaut 1
        
        print("Saisir la profondeur de l'élagage du joueur 2 :")
        joueur2Profondeur=int(input())      #par defaut 0
        
    return()

def afficherGrille():
    """Fonction d'affichage de la grille"""
    resultat = "["
    for l in range (0,6):
        resultat += "["
        for c in range (0,12):
            resultat = resultat + str(grille[l][c]) + " , "
        resultat += "]\n"
    resultat += "]"
    print(resultat)

#### jeu #### 

def ligneVide(colonne):
    """Renvoi la 1ere position libre (en partant du haut) de la colonne donnée"""
    ligne = 5
    while (ligne >= 0 and grille[ligne][colonne] != "-"):
        ligne-=1
    return ligne

def ajouterPion(joueur, colonne):
    global grille
    """Ajoute un pion à la colonne choisie, et l'ajoute dans la grille"""
    ligne = ligneVide(colonne);
    if (ligne >= 0):
        grille[ligne][colonne] = joueur
    return()

def jouer(grille) :
    """Algorithme de déroulement du jeu"""
    global joueurCourant
    
    # Joueur 1
    print("Tour du joueur 1")
    if (joueur1Bot):
        colonne=jouerBot(joueurCourant, joueur1Algo,grille)
        ajouterPion(joueurCourant, colonne)
        print("Le joueur 1 a ajouté un pion a la colonne ",colonne)
    else :
        print("Saisir la colone de votre pion (colonne numérotées de 2 à 11)")
        colonne=int(input())
        ajouterPion(joueurCourant, colonne)
        print("Le joueur 1 a ajouté un pion a la colonne ",colonne)
    afficherGrille()
    if (checkVictoire() == joueurCourant):
        messageFin(1, True)
        return()
    elif (checkNul()):
        messageFin(0, True)
        return()
    else:
        joueurCourant = 2
                
    #Joueur 2
    print("Tour du joueur 2")
    if (joueur2Bot):
        colonne=jouerBot(joueurCourant, joueur2Algo,grille)
        ajouterPion(joueurCourant, colonne)
        print("Le joueur 2 a ajouté un pion a la colonne ",colonne)
    else :
        print("Saisir la colone de votre pion (colonne numérotées de 2 à 11)")
        colonne=int(input())
        ajouterPion(joueurCourant, colonne)
        print("Le joueur 2 a ajouté un pion a la colonne ",colonne)
    afficherGrille()
    if (checkVictoire() == joueurCourant):
        messageFin(2, True)
        return()
    elif (checkNul()):
        messageFin(0, True)
        return()
    else :
        joueurCourant = 1
        jouer(grille)

def reinitialiser():
    global grille, joueurCourant
    """Reinitialise la partie (grille + plateau)"""
    grille=[["-" for i in range (12)] for j in range (6)]
    joueurCourant = 1;

def checkNul():
    """Verifie si la grille est pleine ou si la limite de 42 pions joués a été dépassée"""
    estNul = False
    compteur=0
    for colonne in range (0,12):
        for ligne in range (0,6):
            if grille[ligne][colonne] != "-":
                compteur+=1
    if compteur >=42:
        estNul=True
    return estNul

def checkVictoire():
    """Verifie si quelqu'un a gagné la partie"""
    
    #Balayage horizontal
    for colonne in range (0,9):
        for ligne in range (5,-1,-1):
            if (grille[ligne][colonne] != "-" and grille[ligne][colonne] == grille[ligne][colonne + 1]
                    and grille[ligne][colonne] == grille[ligne][colonne + 2] 
                    and grille[ligne][colonne] == grille[ligne][colonne + 3]):
                return (grille[ligne][colonne])

    #Balayage vertical
    for colonne in range (0,12):
        for ligne in range (5,2,-1):
            if (grille[ligne][colonne] != "-" and grille[ligne][colonne] == grille[ligne - 1][colonne]
                    and grille[ligne][colonne] == grille[ligne - 2][colonne]
                    and grille[ligne][colonne] == grille[ligne - 3][colonne]):
                return (grille[ligne][colonne])
            
    # Balayage diagonale
    for colonne in range (0,8):
        for ligne in range (5,2,-1):
            if (grille[ligne][colonne] != "-" and grille[ligne][colonne] == grille[ligne - 1][colonne + 1]
                    and grille[ligne][colonne] == grille[ligne - 2][colonne + 2]
                    and grille[ligne][colonne] == grille[ligne - 3][colonne + 3]):
                return (grille[ligne][colonne])

    # Balayage diagonale
    for colonne in range (11,2,-1):
        for ligne in range (5,2,-1):
            if (grille[ligne][colonne] != "-" and grille[ligne][colonne] == grille[ligne - 1][colonne - 1]
                    and grille[ligne][colonne] == grille[ligne - 2][colonne - 2]
                    and grille[ligne][colonne] == grille[ligne - 3][colonne - 3]):
                return (grille[ligne][colonne])
    return(0)


#### ia #### 

def jouerBot(joueur, algorithme,grille):
    """Retourne la colonne jouée en fonction du joueur et de l'algorithme choisi"""
    #On commence toujours par jouer au milieu
    if (grille[5][5] == "-"):
        return (5)
    ligne=-1
    while ligne<0:
        if (algorithme == 1):
            coup = coupNaif(joueur)
    #    if (algorithme == 5):
    #        coup = coupMinMax()
        if (algorithme == 2):
            coup = coupAlphaBeta(grille)
        ligne=ligneVide(coup)
    return (coup)

def coupNaif(joueur) :
    """Algorithme qui empeche un coup gagnant de l'adversaire, joue un coup gagnant, ou joue au hasard"""
    if joueur=="1":
        joueurAdverse="2"
    else :
        joueurAdverse="1"
    #Defaite au prochain tour
    for i in range (0,7):
        ligne = ligneVide(i)
        if (ligne >= 0) :
            grille[ligne][i] = joueurAdverse
            if (checkVictoire() == joueurAdverse):
                grille[ligne][i] = "-"
                return (i)
            grille[ligne][i] = "-"

    #Victoire au prochain tour
    for i in range (0,7):
        ligne = ligneVide(i)
        if (ligne >= 0):
            grille[ligne][i] = joueur
            if (checkVictoire() == joueur):
                grille[ligne][i] = "-"
                return (i)
            grille[ligne][i] = "-"
    
    alea=floor(random() * (7))
    while ligneVide(alea)<0:
        alea=floor(random() * (7))
    return (alea)


#### heuristique 2 #### 
    
def heuristique2(joueur) :
    """Retourne une évaluation de la feuille en fonction du nombre de cases alignés par les joueurs"""
    print("h2")
    if joueur=="1":
        joueurAdverse="2"
    else :
        joueurAdverse=1
    evaluation = 128

    evaluation += nombreAlignement(3, joueur) * 3
    evaluation -= nombreAlignement(3, joueurAdverse) * 3
    evaluation += nombreAlignement(2, joueur) * 1
    evaluation -= nombreAlignement(2, joueurAdverse) * 1
    return (evaluation)

def nombreAlignement(alignement, joueur):
    """Retourne le nombre d'alignement passé en parametre d'un joueur"""
    nombre = 0
    sens = {"horizontal": [1,0], "vertical": [0,1], "diagonaleDroite": [-1, 1], "diagonaleGauche": [1,1] }
    for colonne in range (0,7):
        nombre += nombreCasesAlignes(colonne, 0, sens["vertical"], joueur, alignement)
        nombre += nombreCasesAlignes(colonne, 0, sens["diagonaleGauche"], joueur, alignement)
        nombre += nombreCasesAlignes(colonne, 0, sens["diagonaleDroite"], joueur, alignement)
    for ligne in range (0,6):
        nombre += nombreCasesAlignes(0, ligne, sens["horizontal"], joueur, alignement)
        nombre += nombreCasesAlignes(0, ligne, sens["diagonaleGauche"], joueur, alignement)
        nombre += nombreCasesAlignes(6, ligne, sens["diagonaleDroite"], joueur, alignement)
    return (nombre)

def nombreCasesAlignes(colonne, ligne, sens, joueur, alignement):
    """Retourne le nombre de case alignées selon le sens et l'alignement choisi"""
    nombreAlignes = 0;
    nombreCases = 0;
    caseAvant=""
    caseApres=""

    while (((colonne >= 0) and (colonne < 7)) and ((ligne >= 0) and (ligne < 6))):
        #Si la case appartient au joueur
        if (grille[ligne][colonne] == joueur) :
            if (nombreCases == 0) : # Nouvel alignement
                debutColonne = colonne
                debutLigne = ligne
            nombreCases+=1
        else : # Alignement rompu
            nombreCases = 0
            
        # Si on a atteint le nombre d'alignement,...
        if (nombreCases == alignement) :
            # ... on regarde si la case avant l'alignement ...
            if ((debutColonne - sens[0] < 7 and debutColonne - sens[0] >= 0) and (debutLigne - sens[1] < 6 and debutLigne - sens[1] >= 0)):
                caseAvant = grille[debutLigne - sens[1]][debutColonne - sens[0]];
            # ... ou la case après l'alignement ...
            if ((colonne + sens[0] < 7 and colonne + sens[0] >= 0) and (ligne + sens[1] < 6 and ligne + sens[1] >= 0)):
                
                caseApres = grille[ligne + sens[1]][colonne + sens[0]]
            # ... est jouable par le joueur
            if ((caseAvant == 0 or caseApres == 0) and (caseAvant != joueur and caseApres != joueur)):
                nombreAlignes+=1
                caseAvant = -1
                caseApres = -1
        colonne += sens[0]
        ligne += sens[1]
    return (nombreAlignes)


#### heuristique 1 #### 
tableauEvaluation = [[3, 4, 5, 7, 8, 8, 8, 8, 7, 5, 4, 3],
    [4, 6, 8, 10, 11, 11, 11, 11, 10, 8, 6, 4],
    [5, 8, 11, 13, 14, 14, 14, 14, 13, 11, 8, 5],
    [5, 8, 11, 13, 14, 14, 14, 14, 13, 11, 8, 5],
    [4, 6, 8, 10, 11, 11, 11, 11, 10, 8, 6, 4],
    [3, 4, 5, 7, 8, 8, 8, 8, 7, 5, 4, 3]]

def heuristique1(joueur):
    """Retourne une evaluation de la feuille en fonction du tableau d'evaluation"""
    print("h1")
    if joueur=="1":
        joueurAdverse="2"
    else:
        joueurAdverse="1"
    evaluation = 0

    for col in range (0,7):
        for lig in range (0,6):
            if (grille[lig][col] == joueur):
                evaluation += tableauEvaluation[lig][col]
            elif (grille[lig][col] == joueurAdverse):
                evaluation -= tableauEvaluation[lig][col]
    return (evaluation)


#### alpha beta #### 

def coupAlphaBeta(grille):
    global colonneMax
    """Retourne la colonne determinée par l'algorithme Alpha Beta"""
    valeurMaxAB(0, -10000, 10000,grille)
    return (colonneMax)

def valeurMaxAB(profondeur, alpha, beta,state):
    grille=copy.deepcopy(state)
    print("max")
    #Verifie si victoire
    global colonneMax
    victoire = checkVictoire()
    if (victoire != 0):
        if (victoire == joueurCourant):
            return 1000 - profondeur
        else :
            return -1000 + profondeur

    # Verifie profondeur
    if ((joueurCourant == "1" and profondeur == joueur1Profondeur) or (joueurCourant == "2" and profondeur == joueur2Profondeur) or checkNul()):
        if (joueurCourant == "1" and joueur1Heuristique == 1) or (joueurCourant == "2" and joueur2Heuristique == 1):
            return heuristique1(joueurCourant)
        else:
            return heuristique2(joueurCourant)

    profondeur+=1
    colonne = 0
    for i in range (0,7):
        ligne = ligneVide(i)
        #Si la colonne est jouable
        if (ligne >= 0):
            #On simule le coup
            grille[ligne][i] = joueurCourant
            valeur = valeurMinAB(profondeur, alpha, beta,grille)
            if (valeur > alpha):
                alpha = valeur
                colonne = i
            #Retour à l'état antérieur
            grille[ligne][i] = "-"
            #Coupure
            if (alpha >= beta):
                return alpha
    colonneMax = colonne
    return alpha

def valeurMinAB(profondeur, alpha, beta,state):
    grille=copy.deepcopy(state)
    print("min")
    if joueurCourant==1:
        joueurCourantAdverse=2
    else :
        joueurCourantAdverse=1

    #Verifie si victoire
    victoire = checkVictoire()
    if (victoire != 0):
        if (victoire == joueurCourant):
            return 1000 - profondeur
        else:
            return -1000 + profondeur

    # Verifie profondeur
    if ((joueurCourant == 1 and profondeur == joueur1Profondeur) or (joueurCourant == 2 and profondeur == joueur2Profondeur) or checkNul()):
        if (joueurCourant == 1 and joueur1Heuristique == 1) or (joueurCourant == 2 and joueur2Heuristique == 1):
            return heuristique1(joueurCourant)
        else:
            return heuristique2(joueurCourant)

    profondeur+=1
    cpt=0
    for i in range (0,7):
        ligne = ligneVide(i)
        #Si la colonne est jouable
        if (ligne >= 0):
            #On simule le coup
            grille[ligne][i] = joueurCourantAdverse
            valeur = valeurMaxAB(profondeur, alpha, beta,grille)
            cpt+=1
            if(cpt==1):
                break;
            if (valeur < beta):
                beta = valeur
            # Retour à l'état antérieur
            grille[ligne][i] = "-"
            #Coupure
            if (beta <= alpha):
                return beta
    return beta

#### infos ####
def messageFin(joueur, gagnant):
    """Ecrit le message de fin"""
    if (gagnant):
        if joueur!="0":
            print("Le joueur ", joueur," a gagné.")
        else :
            print("Match Nul !")
#    if (gagnant):
#        if ((joueur == "1" and joueur1Bot==False) or (joueur == "2" and joueur2Bot==False)):
#            print("Joueur ", joueur, " : Vous avez gagné ! :D")
#        elif ((joueur == "1" and joueur1Bot) or (joueur == "2" and joueur2Bot)):
#            print("Joueur ", joueur, " : Vous avez perdu :(")
#        else :
#            print("Match Nul !")
    return()

#### programme principal ####
parametres()
jouer(grille)