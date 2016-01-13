from carte import *
from matrice import *
from joueur import *
import random
import os


# permet de créer un labyrinthe avec nbJoueurs joueurs, nbTresors trésors
# chacun des joueurs aura au plus nbTresorMax à trouver
# si ce dernier paramètre est à 0, on distribuera le maximum de trésors possible 
# à chaque joueur en restant équitable
# un joueur courant est choisi et la phase est initialisée
def Labyrinthe(nbJoueurs=2,nbTresors=24, nbTresorMax=0):
    return {'phase' : 0, 'current' : random.randint(1, nbJoueurs+1), 'joueurs' : Joueurs(nbJoueurs, nbTresors, nbTresorMax), 'plateau' : Matrice(9, 9, Carte( True, True, False, False)), 'carteAJouer' : None}

# retourne la matrice représentant le plateau de jeu
def getPlateau(labyrinthe):
    return labyrinthe['plateau']

# retourne le nombre de joueurs engagés dans la partie
def getNbJoueurs(labyrinthe):
    return labyrinthe['joueurs']['NbJoueurs']

# indique quel est le joueur courant (celui qui doit jouer)
def getJoueurCourant(labyrinthe):
    return labyrinthe['current']

# change de joueur courant
def changerJoueurCourant(labyrinthe):
    labyrinthe['current'] = (labyrinthe['current'] + 1) if labyrinthe['current'] < getNbJoueurs(labyrinthe) else 1
    return labyrinthe

# retourne la phase du jeu
def getPhase(labyrinthe):
    return labyrinthe['phase']

# change la phase de jeu
def changerPhase(labyrinthe):
    pass

# indique combien de trésors il reste dans le labyrinthe
def getNbTresors(labyrinthe):
    pass

# retourne la structures qui gèrent les joueurs et leurs trésors
def getLesJoueurs(labyrinthe):
    return labyrinthe['joueurs']

# diminue le nombre de trésors de 1
def decTresor(labyrinthe):
    labyrinthe['joueurs']['NbTresors'] -= 1

# met à jour la structure qui gère les joueurs en enlevant le trésor que le joueur
# courant vient de trouver
def joueurCourantTrouveTresor(labyrinthe):
    tresorTrouve(labyrinthe['joueurs'], getJoueurCourant(labyrinthe))

# retourne le nombre de trésors restant à trouver pour le joueur numJoueur
def nbTresorsRestantsJoueur(labyrinthe,numJoueur):
    nbTresorsRestants(labyrinthe['joueurs'], numJoueur)

# enlève le trésor numTresor sur la carte qui se trouve sur la case lin,col du plateau
# si le trésor ne s'y trouve pas la fonction ne fait rien
def prendreTresorL(labyrinthe,lin,col,numTresor):
	if getTresor(getVal(lin, col)) ==  numTresor:
		prendreTresor(getVal(lin, col))

# enlève le joueur courant de la carte qui se trouve sur la case lin,col du plateau
# si le joueur ne s'y trouve pas la fonction ne fait rien
def prendreJoueurCourant(labyrinthe,lin,col):
    prendrePionL(labyrinthe, lin, col, getJoueurCourant(labyrinthe))        

# pose le joueur courant de la carte qui se trouve sur la case lin,col du plateau
# si le joueur s'y trouve déjà la fonction ne fait rien
def poserJoueurCourant(labyrinthe,lin,col):
    poserPion(getVal(labyrinthe['plateau'], lin, col), getJoueurCourant(labyrinthe))

# retourne la carte amovible supplémentaire que le joueur courant doit joueur
def getCarteAJouer(labyrinthe):
    pass

# fonction utilitaire qui permet de créer les cartes amovibles du jeu en y positionnant
# aléatoirement nbTresor trésors
# la fonction retourne la liste, mélangée aléatoirement, des cartes ainsi créées
def creerCartesAmovibles(tresorDebut,nbTresors):
    pass

# fonction qui retourne True si le coup proposé correspond au coup interdit
# elle retourne False sinon
def coupInterdit(labyrinthe,direction,rangee):
    pass

# fonction qui joue la carte amovible dans la direction et sur la rangée passées 
# en paramètres. Cette fonction
#      - met à jour le plateau du labyrinthe
#      - met à jour la carte à jouer
#      - met à jour la nouvelle direction interdite
def jouerCarte(labyrinthe,direction,rangee):
    pass

# Cette fonction tourne la carte à jouer dans le sens indiqué 
# en paramètre (H horaire A antihoraire)
def tournerCarte(labyrinthe,sens='H'):
    tournerHoraire(labyrinte['carteAJouer']) if sens == 'H' else tournerAntiHoraire(labyrinte['carteAJouer'])

# retourne le numéro du trésor à trouver pour le joueur courant
def getTresorCourant(labyrinthe):
    return prochainTresor(getLesJoueurs(labyrinthe), getJoueurCourant(labyrinthe))

# retourne sous la forme d'un couple (lin,col) la position du trésor à trouver 
# pour le joueur courant sur le plateau
def getCoordonneesTresorCourant(labyrinthe):
    pass

# retourne sous la forme d'un couple (lin,col) la position du joueur courant sur le plateau
def getCoordonneesJoueurCourant(labyrinthe):
    pass

# prend le pion numJoueur sur sur la carte se trouvant en position lin,col du plateau
def prendrePionL(labyrinthe,lin,col,numJoueur):
    if possedePion(getVal(getPlateau(labyrinthe), lin, col), numJoueur):
		prendrePion(getVal(getPlateau(labyrinthe), lin, col), numJoueur)

# pose le pion numJoueur sur sur la carte se trouvant en position lin,col du plateau
def poserPionL(labyrinthe,lin,col,joueur):
    mettrePion(getVal(getPlateau(labyrinthe),lin,col),joueur)

# indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du labyrinthe
def accessible(labyrinthe,ligD,colD,ligA,colA):
    pass

# indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du labyrinthe
# mais la valeur de retour est None s'il n'y a pas de chemin, sinon c'est un chemin possible entre ces deux cases
def accessibleDist(labyrinthe,ligD,colD,ligA,colA):
    pass

# exécute une action de jeu de la phase 1
# si action vaut 'T' => faire tourner la carte à jouer
# si action est une des lettres N E S O et rangee est un des chiffre 1,3,5 
# => insèrer la carte à jouer à la direction action sur la rangée rangee
# le retour de la fonction est un entier qui vaut
# 0 si l'action demandée était valide et s'est bien effectuée
# 1 si l'action est interdite car l'opposée de l'action précédente
# 2 si action et rangee sont des entiers positifs
# 3 dans tous les autres cas
def executerActionPhase1(labyrinthe,action,rangee):
    pass

# verifie si le joueur courant peut accéder la case ligA,colA
# si c'est le cas la fonction retourne une liste représentant un chemin possible
# sinon ce n'est pas le cas, la fonction retourne None
def accessibleDistJoueurCourant(labyrinthe, ligA,colA):
    pass

# vérifie si le le joueur courant vient de trouver un trésor (si oui fait le nécessaire)
# vérifie si la partie est terminée, si ce n'est pas le cas passe au joueur suivant
# le retour de la fonction est un entier qui vaut
# 0 si le joueur courant n'a pas trouvé de trésor
# 1 si le joueur courant a trouvé un trésor mais la partie n'est pas terminée
# 2 si le joueur courant a trouvé son dernier trésor (la partie est donc terminée)
def finirTour(labyrinthe):
    pass
    
