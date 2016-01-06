import random

# permet de créer entre deux et quatre joueurs et leur distribue de manière équitable
# les trésors compris entre 1 et nbTresor avec au plus nbMaxTresor chacun
# si nbMaxTresor vaut 0, la fonction distribue le maximum de trésors possible
def Joueurs( nbJoueurs=2, nbTresors=24, nbTresorMax=0):
    pass

# attribue effectivement les trésors de manière aléatoire
def initTresor(joueurs):
    pass

# retourne le numéro du prochain trésor à trouver pour la joueur numJoueur
# None s'il n'y a pas de prochain trésor
def prochainTresor(joueurs,numJoueur):
    pass

# enlève le trésor courant du joueur numJoueur et retourne le nombre de trésor
# qu'il reste à trouver pour ce joueur
def tresorTrouve(joueurs,numJoueur):
    pass
    
# retourne le nombre de trésors qu'il reste à trouver pour le joueur numJoueur
def nbTresorsRestants(joueurs,numJoueur):
    pass
