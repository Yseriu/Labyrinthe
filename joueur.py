import random

# permet de créer entre deux et quatre joueurs et leur distribue de manière équitable
# les trésors compris entre 1 et nbTresor avec au plus nbMaxTresor chacun
# si nbMaxTresor vaut 0, la fonction distribue le maximum de trésors possible

# Le dictionnaire de joueurs contient :
#  * owner : la liste des propriétaires des trésors - n° de trésor en indice, n° de proprio en valeur
#  * found : la liste des trésor : valeur -> boolean trouvé ou non

def Joueurs( nbJoueurs=2, nbTresors=24, nbTresorMax=0):
    nbTr = min(nbTresors, nbTresorMax*nbJoueurs) if nbTresorMax != 0 else nbTresors
    return {'NbJoueurs' : nbJoueurs, 'owner' : [0] * nbTr, 'Found' : [False] * nbTr}

# attribue effectivement les trésors de manière aléatoire
def initTresor(joueurs):
    parJoueurs = len(joueurs['owner']) // joueurs['NbJoueurs']
    tres = []
    for j in range(1, joueurs['NbJoueurs']+1):
        for _ in range(parJoueurs):
            tres.append(j)
    tres = sorted(tres, key=lambda k: random.randint(0, 100))
    joueurs['owner'] = tres
    return joueurs

# retourne le numéro du prochain trésor à trouver pour la joueur numJoueur
# None s'il n'y a pas de prochain trésor
def prochainTresor(joueurs,numJoueur):
    try:
        return joueurs['owner'].index(numJoueur)
    except ValueError:
        return None

# enlève le trésor courant du joueur numJoueur et retourne le nombre de trésor
# qu'il reste à trouver pour ce joueur
def tresorTrouve(joueurs,numJoueur):
	i = prochainTresor(joueurs, numJoueur)
	if i != None:
		joueurs['owner'][i] = 0
    return nbTresorsRestants(joueurs, numJoueur)

# retourne le nombre de trésors qu'il reste à trouver pour le joueur numJoueur
def nbTresorsRestants(joueurs,numJoueur):
    return len([x for x in joueurs['owner'] if x == numJoueur])
