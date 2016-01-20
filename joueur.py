import random

# permet de créer entre deux et quatre joueurs et leur distribue de manière équitable
# les trésors compris entre 1 et nbTresor avec au plus nbMaxTresor chacun
# si nbMaxTresor vaut 0, la fonction distribue le maximum de trésors possible

# Le dictionnaire de joueurs contient :
#  * owner : la liste des propriétaires des trésors - n° de trésor en indice, n° de proprio en valeur
#  * found : la liste des trésor : valeur -> boolean trouvé ou non

def Joueurs(nbJoueurs=2, nbTresors=24, nbTresorMax=0):
    nbTr = max((min(nbTresors, nbTresorMax*nbJoueurs) if nbTresorMax != 0 else nbTresors), 13)
    j = {'NbJoueurs' : nbJoueurs, 'owner' : [0] * nbTr, 'found' : [False] * nbTr}
    initTresor(j)
    j['found'].insert(0, None)
    return j

# attribue effectivement les trésors de manière aléatoire
def initTresor(joueurs):
    parJoueurs = len(joueurs['owner']) // joueurs['NbJoueurs']
    tres = []
    for j in range(1, joueurs['NbJoueurs']+1):
        for _ in range(parJoueurs):
            tres.append(j)
    random.shuffle(tres)
    tres.insert(0, 0)
    joueurs['owner'] = tres
    return joueurs

# retourne le numéro du prochain trésor à trouver pour le joueur numJoueur
# None s'il n'y a pas de prochain trésor
def prochainTresor(joueurs,numJoueur):
    for i in range(1, len(joueurs['owner'])):
        if joueurs['owner'][i] == numJoueur and not joueurs['found'][i]: return i
    return None

# enlève le trésor courant du joueur numJoueur et retourne le nombre de trésor
# qu'il reste à trouver pour ce joueur
def tresorTrouve(joueurs,numJoueur):
    i = prochainTresor(joueurs, numJoueur)
    if i != None:
        joueurs['owner'][i] = 0
        joueurs['found'][i] = True
    return nbTresorsRestants(joueurs, numJoueur)

# retourne le nombre de trésors qu'il reste à trouver pour le joueur numJoueur
def nbTresorsRestants(joueurs,numJoueur):
    ans = 0
    for i in range(1, len(joueurs['owner'])):
        if joueurs['owner'][i] == numJoueur and not joueurs['found'][i]: ans += 1
    return ans
