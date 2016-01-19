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
def Labyrinthe(nbJoueurs=2, nbTresors=24, nbTresorMax=0):
    l = {'phase' : 1, 'current' : random.randint(1, nbJoueurs), 'joueurs' : Joueurs(nbJoueurs, nbTresors, nbTresorMax), 'plateau' : Matrice(7, 7, None), 'carteAJouer' : None, 'interdit' : None}
    initPlateau(l)
    return l

def initPlateau(labyrinthe):
    setVal(getPlateau(labyrinthe), 0, 0, Carte(True, False, False, True, 0, [1]))
    setVal(getPlateau(labyrinthe), 6, 0, Carte(False, False, True, True, 0, [2]))
    setVal(getPlateau(labyrinthe), 0, 6, Carte(True, True, False, False, 0, [3] if getNbJoueurs(labyrinthe) >= 3 else []))
    setVal(getPlateau(labyrinthe), 6, 6, Carte(False, True, True, False, 0, [4] if getNbJoueurs(labyrinthe) >= 4 else []))
    t = 1
    for i in [2, 4]:
        setVal(getPlateau(labyrinthe), i, 0, Carte(False, False, False, True, t))
        setVal(getPlateau(labyrinthe), i, 6, Carte(False, True, False, False, t+1))
        setVal(getPlateau(labyrinthe), 6, i, Carte(False, False, True, False, t+2))
        setVal(getPlateau(labyrinthe), 0, i, Carte(True, False, False, False, t+3))
        t += 4
    setVal(getPlateau(labyrinthe), 2, 2, Carte(False, False, False, True, t))
    setVal(getPlateau(labyrinthe), 2, 4, Carte(True, False, False, False, t+1))
    setVal(getPlateau(labyrinthe), 4, 2, Carte(False, False, True, False, t+2))
    setVal(getPlateau(labyrinthe), 4, 4, Carte(False, True, False, False, t+3))
    t += 4
    amov = creerCartesAmovibles(t, getNbTresors(labyrinthe))
    for i in range(getNbLignes(getPlateau(labyrinthe))):
        for j in range(getNbColonnes(getPlateau(labyrinthe))):
            if getVal(getPlateau(labyrinthe), i, j) == None:
                setVal(getPlateau(labyrinthe), i, j, amov.pop(0))
    setCarteAJouer(labyrinthe, amov[0])
    return labyrinthe

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
    labyrinthe['phase'] = (labyrinthe['phase'] + 1) if labyrinthe['phase'] < 2 else 1
    return labyrinthe

# indique combien de trésors il reste dans le labyrinthe
def getNbTresors(labyrinthe):
    nbTresorRest = 0
    for i in range(getNbJoueurs(labyrinthe)):
        nbTresorRest += nbTresorsRestants(getLesJoueurs(labyrinthe), i+1)
    return nbTresorRest

# retourne la structures qui gèrent les joueurs et leurs trésors
def getLesJoueurs(labyrinthe):
    return labyrinthe['joueurs']

# diminue le nombre de trésors de 1
def decTresor(labyrinthe):
    pass

# met à jour la structure qui gère les joueurs en enlevant le trésor que le joueur
# courant vient de trouver
def joueurCourantTrouveTresor(labyrinthe):
    tresorTrouve(getLesJoueurs(labyrinthe), getJoueurCourant(labyrinthe))

# retourne le nombre de trésors restant à trouver pour le joueur numJoueur
def nbTresorsRestantsJoueur(labyrinthe,numJoueur):
    return nbTresorsRestants(getLesJoueurs(labyrinthe), numJoueur)

# enlève le trésor numTresor sur la carte qui se trouve sur la case lin,col du plateau
# si le trésor ne s'y trouve pas la fonction ne fait rien
def prendreTresorL(labyrinthe,lin,col,numTresor):
    if getTresor(getVal(getPlateau(labyrinthe), lin, col)) ==  numTresor:
        prendreTresor(getVal(getPlateau(labyrinthe), lin, col))

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
    return labyrinthe['carteAJouer']

def setCarteAJouer(labyrinthe, c):
    labyrinthe['carteAJouer'] = c
    return labyrinthe

# fonction utilitaire qui permet de créer les cartes amovibles du jeu en y positionnant
# aléatoirement nbTresor trésors
# la fonction retourne la liste, mélangée aléatoirement, des cartes ainsi créées
def creerCartesAmovibles(tresorDebut,nbTresors):
    l = []
    for _ in range(16):
        l.append(tourneAleatoire(Carte(False, False, True, True)))
    for _ in range(6):
        l.append(tourneAleatoire(Carte(False, False, False, True)))
    for _ in range(12):
        l.append(tourneAleatoire(Carte(False, True, False, True)))
    l = sorted(l, key=lambda k: random.randint(0, 100))
    for i in range(tresorDebut, nbTresors+1):
        mettreTresor(l[i], i)
    l = sorted(l, key=lambda k: random.randint(0, 100))
    return l

# fonction qui retourne True si le coup proposé correspond au coup interdit
# elle retourne False sinon
def coupInterdit(labyrinthe,direction,rangee):
    return labyrinthe['interdit'] != None and (direction, rangee) == labyrinthe['interdit']

# fonction qui joue la carte amovible dans la direction et sur la rangée passées 
# en paramètres. Cette fonction
#      - met à jour le plateau du labyrinthe
#      - met à jour la carte à jouer
#      - met à jour la nouvelle direction interdite
def jouerCarte(labyrinthe,direction,rangee):
    direction = direction.lower()
    c = {'n': decalageColonneEnBas,
    'e': decalageLigneAGauche,
    's': decalageColonneEnHaut,
    'o': decalageLigneADroite}[direction](getPlateau(labyrinthe), rangee, getCarteAJouer(labyrinthe))
    if getNbPions(c) != 0:
        if direction in 'ns':
            addPions(getVal(getPlateau(labyrinthe), 0 if direction == 'n' else getNbLignes(getPlateau(labyrinthe))-1, rangee), getPions(c))
        else:
            addPions(getVal(getPlateau(labyrinthe), rangee, 0 if direction == 'o' else getNbColonnes(getPlateau(labyrinthe))-1), getPions(c))
    setPions(c, [])
    setCarteAJouer(labyrinthe, c)
    changerPhase(labyrinthe)
    labyrinthe['interdit'] = ('seno'['nose'.index(direction)], rangee)
    return labyrinthe
    
# Cette fonction tourne la carte à jouer dans le sens indiqué 
# en paramètre (H horaire A antihoraire)
def tournerCarte(labyrinthe,sens='H'):
    tournerHoraire(getCarteAJouer(labyrinthe)) if sens == 'H' else tournerAntiHoraire(getCarteAJouer(labyrinthe))

# retourne le numéro du trésor à trouver pour le joueur courant
def getTresorCourant(labyrinthe):
    return prochainTresor(getLesJoueurs(labyrinthe), getJoueurCourant(labyrinthe))

# retourne sous la forme d'un couple (lin,col) la position du trésor à trouver 
# pour le joueur courant sur le plateau
def getCoordonneesTresorCourant(labyrinthe):
    for i in range(getNbColonnes(getPlateau(labyrinthe))):
        for j in range(getNbLignes(getPlateau(labyrinthe))):
            if getTresor(getVal(getPlateau(labyrinthe),i,j))==getTresorCourant(labyrinthe):
                return (i,j)

# retourne sous la forme d'un couple (lin,col) la position du joueur courant sur le plateau
def getCoordonneesJoueurCourant(labyrinthe):
    for i in range(getNbColonnes(getPlateau(labyrinthe))):
        for j in range(getNbLignes(getPlateau(labyrinthe))):
            if possedePion(getVal(getPlateau(labyrinthe),i,j),getJoueurCourant(labyrinthe)):
                return (i,j)
    print("Joueur non trouvé")


# prend le pion numJoueur sur sur la carte se trouvant en position (lin, col) du plateau
def prendrePionL(labyrinthe,lin,col,numJoueur):
    if possedePion(getVal(getPlateau(labyrinthe), lin, col), numJoueur):
        prendrePion(getVal(getPlateau(labyrinthe), lin, col), numJoueur)

# pose le pion numJoueur sur sur la carte se trouvant en position lin,col du plateau
def poserPionL(labyrinthe,lin,col,joueur):
    poserPion(getVal(getPlateau(labyrinthe),lin,col),joueur)


def marquageDirect(calque,mat,val,marque):
    ans = False
    for lig in range(getNbLignes(mat)):
        for col in range(getNbColonnes(mat)):
            if (getVal(calque, lig, col) == 0 and 
            (  (passageEst(getVal(mat, lig, col), getVal(mat, lig, col+1)) and val == getVal(calque, lig, col+1))
            or (passageOuest(getVal(mat, lig, col), getVal(mat, lig, col-1)) and val == getVal(calque, lig, col-1))
            or (passageNord(getVal(mat, lig, col), getVal(mat, lig-1, col)) and val == getVal(calque, lig-1, col))
            or (passageSud(getVal(mat, lig, col), getVal(mat, lig+1, col)) and val == getVal(calque, lig+1, col))
            )):
                setVal(calque, lig, col, marque)
                ans = True
    return ans      


# verifie qu'il existe un chemin entre pos1 et pos2 dans la matrice mat
def accessible2(mat,pos1,pos2):
    #initialisation du calque
    calque = Matrice(getNbLignes(mat), getNbColonnes(mat), 0)
    setVal(calque, pos1[0], pos1[1], 1)
    #propagation
    pr = True
    val = 1
    while pr and getVal(calque, pos2[0], pos2[1]) == 0:
        pr = marquageDirect(calque, mat, val, val + 1)
        val += 1
    return calque

def passage(plateau, ligD, colD, ligA, colA):
    if ligA == ligD:
        # meme ligne
        if colD == (colA + 1):
            return passageOuest(getVal(plateau, ligD, colD), getVal(plateau, ligA, colA))
        if colD == (colA - 1):
            return passageEst(getVal(plateau, ligD, colD), getVal(plateau, ligA, colA))
    if colD == colA:
        # meme colonne
        if ligD == (ligA + 1):
            return passageNord(getVal(plateau, ligD, colD), getVal(plateau, ligA, colA))
        if ligD == (ligA - 1):
            return passageSud(getVal(plateau, ligD, colD), getVal(plateau, ligA, colA))
    return False

def cheminDecroissant(calque, pos1, pos2, plateau):
    last = getVal(calque, pos2[0], pos2[1])-1
    ans = [pos2]
    while last != 0:
        for lig, col in [(ans[-1][0]-1, ans[-1][1]),(ans[-1][0]+1, ans[-1][1]),(ans[-1][0], ans[-1][1]-1),(ans[-1][0], ans[-1][1]+1)]:
            if getVal(calque, lig, col) == last and passage(plateau, lig, col, ans[-1][0], ans[-1][1]):
                ans.append((lig, col))
                break
        last -= 1
    ans.reverse()
    #print(ans)
    return ans

# indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du labyrinthe
def accessible(labyrinthe,ligD,colD,ligA,colA):
    calque = accessible2(getPlateau(labyrinthe), (ligD, colD), (ligA, colA))
    return (getVal(calque, ligA, colA) != 0)


# indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du labyrinthe
# mais la valeur de retour est None s'il n'y a pas de chemin, sinon c'est un chemin possible entre ces deux cases
def accessibleDist(labyrinthe,ligD,colD,ligA,colA):
    calque = accessible2(getPlateau(labyrinthe), (ligD, colD), (ligA, colA))
    return cheminDecroissant(calque, (ligD, colD), (ligA, colA), getPlateau(labyrinthe)) if (getVal(calque, ligA, colA) != 0) else None

# exécute une action de jeu de la phase 1
# si action vaut 'T' => faire tourner la carte à jouer
# si action est une des lettres N E S O et rangee est un des chiffre 1,3,5 
# => insèrer la carte à jouer à la direction action sur la rangée rangee
# le retour de la fonction est un entier qui vaut
# 0 si la carte a été tournée avec succès
# 1 si la carte a été insérée avec succès
# 2 si l'action est interdite car l'opposée de l'action précédente
# 3 si action et rangee sont des entiers positifs
# 4 dans tous les autres cas
def executerActionPhase1(labyrinthe,action,rangee):
    try:
        action = action.lower()
    except AttributeError:
        return 3
    if action == 't':
        tournerHoraire(getCarteAJouer(labyrinthe))
        return 0
    if len(action) == 1 and action in 'neso' and rangee in [1, 3, 5]:
        if coupInterdit(labyrinthe, action, rangee): return 2
        jouerCarte(labyrinthe, action, rangee)
        return 1
    return 4

# verifie si le joueur courant peut accéder la case ligA,colA
# si c'est le cas la fonction retourne une liste représentant un chemin possible
# sinon ce n'est pas le cas, la fonction retourne None
def accessibleDistJoueurCourant(labyrinthe, ligA,colA):
    return accessibleDist(labyrinthe, getCoordonneesJoueurCourant(labyrinthe)[0], getCoordonneesJoueurCourant(labyrinthe)[1], ligA, colA)

# vérifie si le le joueur courant vient de trouver un trésor (si oui fait le nécessaire)
# vérifie si la partie est terminée, si ce n'est pas le cas passe au joueur suivant
# le retour de la fonction est un entier qui vaut
# 0 si le joueur courant n'a pas trouvé de trésor
# 1 si le joueur courant a trouvé un trésor mais la partie n'est pas terminée
# 2 si le joueur courant a trouvé son dernier trésor (la partie est donc terminée)
def finirTour(labyrinthe):
    ans = 0
    if getCoordonneesJoueurCourant(labyrinthe) == getCoordonneesTresorCourant(labyrinthe):
        ans = 1
        tresorTrouve(getLesJoueurs(labyrinthe), getJoueurCourant(labyrinthe))
        x, y = getCoordonneesJoueurCourant(labyrinthe)
        prendreTresor(getVal(getPlateau(labyrinthe), x, y))
        if nbTresorsRestantsJoueur(labyrinthe, getJoueurCourant(labyrinthe)) == 0:
            return 2
    changerPhase(labyrinthe)
    changerJoueurCourant(labyrinthe)
    return ans
    
