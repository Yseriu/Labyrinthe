import random

# permet de créer entre deux et quatre joueurs et leur distribue de manière équitable
# les trésors compris entre 1 et nbTresor avec au plus nbMaxTresor chacun
# si nbMaxTresor vaut 0, la fonction distribue le maximum de trésors possible

# Le dictionnaire de joueurs contient :
#  * owner : la liste des propriétaires des trésors - n° de trésor en indice, n° de proprio en valeur
#  * found : la liste des trésor : valeur -> boolean trouvé ou non
class Joueurs(object):
    def __init__(self,nbJoueurs=2, nbTresors=24, nbTresorMax=0):
        nbTr = max((min(nbTresors, nbTresorMax*nbJoueurs) if nbTresorMax != 0 else nbTresors), 12)
        self.NbJoueurs = nbJoueurs
        self.owner = [0] * nbTr
        self.found = [False] * nbTr
        # j = {'NbJoueurs' : nbJoueurs, 'owner' : [0] * nbTr, 'found' : [False] * nbTr}
        self.initTresor()
        self.found.insert(0, None)

    # attribue effectivement les trésors de manière aléatoire
    def initTresor(self):
        parJoueurs = len(self.owner) // self.NbJoueurs
        tres = []
        for j in range(1, self.NbJoueurs + 1):
            for _ in range(parJoueurs):
                tres.append(j)
        random.shuffle(tres)
        tres.insert(0, 0)
        self.owner = tres
        return self

    # retourne le numéro du prochain trésor à trouver pour le joueur numJoueur
    # None s'il n'y a pas de prochain trésor
    def prochainTresor(self, numJoueur):
        for i in range(1, len(self.owner)):
            if self.owner[i] == numJoueur and not self.found[i]: return i
        return None

    # enlève le trésor courant du joueur numJoueur et retourne le nombre de trésor
    # qu'il reste à trouver pour ce joueur
    def tresorTrouve(self, numJoueur):
        i = self.prochainTresor(numJoueur)
        if i is not None:
            self.owner[i] = 0
            self.found[i] = True
        return self.nbTresorsRestants(numJoueur)

    # retourne le nombre de trésors qu'il reste à trouver pour le joueur numJoueur
    def nbTresorsRestants(self, numJoueur):
        ans = 0
        for i in range(1, len(self.owner)):
            if self.owner[i] == numJoueur and not self.found[i]: ans += 1
        return ans
