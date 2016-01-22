from carteOO import *
from matriceOO import *
from joueurOO import *
import random
import os

class Labyrinthe(object):
    # permet de créer un labyrinthe avec nbJoueurs joueurs, nbTresors trésors
    # chacun des joueurs aura au plus nbTresorMax à trouver
    # si ce dernier paramètre est à 0, on distribuera le maximum de trésors possible
    # à chaque joueur en restant équitable
    # un joueur courant est choisi et la phase est initialisée
    def __init__(self, nbJoueurs=2, nbTresors=24, nbTresorMax=0):
        self.phase = 1
        self.current = random.randint(1, nbJoueurs)
        self.joueurs = Joueurs(nbJoueurs, nbTresors, nbTresorMax)
        self.plateau = Matrice(7, 7, None)
        self.carteAJouer = None
        self.interdit = None
        self.initPlateau()
    
    def initPlateau(self):
        self.getPlateau().setVal(0, 0, Carte(True, False, False, True, 0, [1]))
        self.getPlateau().setVal(6, 0, Carte(False, False, True, True, 0, [2]))
        self.getPlateau().setVal(0, 6, Carte(True, True, False, False, 0, [3] if self.getNbJoueurs() >= 3 else []))
        self.getPlateau().setVal(6, 6, Carte(False, True, True, False, 0, [4] if self.getNbJoueurs() >= 4 else []))

        tl = list(range(1, self.getNbTresors()+1))
        random.shuffle(tl)

        for i in [2, 4]:
            self.getPlateau().setVal(i, 0, Carte(False, False, False, True, tl.pop()))
            self.getPlateau().setVal(i, 6, Carte(False, True, False, False, tl.pop()))
            self.getPlateau().setVal(6, i, Carte(False, False, True, False, tl.pop()))
            self.getPlateau().setVal(0, i, Carte(True, False, False, False, tl.pop()))
        self.getPlateau().setVal(2, 2, Carte(False, False, False, True, tl.pop()))
        self.getPlateau().setVal(2, 4, Carte(True, False, False, False, tl.pop()))
        self.getPlateau().setVal(4, 2, Carte(False, False, True, False, tl.pop()))
        self.getPlateau().setVal(4, 4, Carte(False, True, False, False, tl.pop()))

        amov = self.creerCartesAmovibles(tl)
        for i in range(self.getPlateau().getNbLignes()):
            for j in range(self.getPlateau().getNbColonnes()):
                if self.getPlateau().getVal(i, j) is None:
                    self.getPlateau().setVal(i, j, amov.pop(0))
        self.setCarteAJouer(amov[0])
        return self
    
    # retourne la matrice représentant le plateau de jeu
    def getPlateau(self):
        return self.plateau
    
    # retourne le nombre de joueurs engagés dans la partie
    def getNbJoueurs(self):
        return self.getLesJoueurs().NbJoueurs
    
    # indique quel est le joueur courant (celui qui doit jouer)
    def getJoueurCourant(self):
        return self.current
    
    # change de joueur courant
    def changerJoueurCourant(self):
        self.current = (self.current + 1) if self.current < self.getNbJoueurs() else 1
        return self
    
    # retourne la phase du jeu
    def getPhase(self):
        return self.phase
    
    # change la phase de jeu
    def changerPhase(self):
        self.phase = (self.phase + 1) if self.phase < 2 else 1
        return self
    
    # indique combien de trésors il reste dans le labyrinthe
    def getNbTresors(self):
        nbTresorRest = 0
        for i in range(self.getNbJoueurs()):
            nbTresorRest += self.getLesJoueurs().nbTresorsRestants(i+1)
        return nbTresorRest
    
    # retourne la structures qui gèrent les joueurs et leurs trésors
    def getLesJoueurs(self):
        return self.joueurs
    
    # diminue le nombre de trésors de 1
    def decTresor(self):
        pass
    
    # met à jour la structure qui gère les joueurs en enlevant le trésor que le joueur
    # courant vient de trouver
    def joueurCourantTrouveTresor(self):
        self.getLesJoueurs().tresorTrouve(self.getJoueurCourant())
    
    # retourne le nombre de trésors restant à trouver pour le joueur numJoueur
    def nbTresorsRestants(self, numJoueur):
        return self.getLesJoueurs().nbTresorsRestants(numJoueur)
    
    # enlève le trésor numTresor sur la carte qui se trouve sur la case lin,col du plateau
    # si le trésor ne s'y trouve pas la fonction ne fait rien
    def prendreTresorL(self, lin, col, numTresor):
        if self.getPlateau().getVal(lin, col).getTresor() == numTresor:
            self.getPlateau().getVal(lin, col).prendreTresor()
    
    # enlève le joueur courant de la carte qui se trouve sur la case lin,col du plateau
    # si le joueur ne s'y trouve pas la fonction ne fait rien
    def prendreJoueurCourant(self, lin, col):
        self.prendrePion(lin, col, self.getJoueurCourant())
    
    # pose le joueur courant de la carte qui se trouve sur la case lin,col du plateau
    # si le joueur s'y trouve déjà la fonction ne fait rien
    def poserJoueurCourant(self, lin, col):
        self.getPlateau().getVal(lin, col).poserPion(self.getJoueurCourant())
    
    # retourne la carte amovible supplémentaire que le joueur courant doit joueur
    def getCarteAJouer(self):
        return self.carteAJouer
    
    def setCarteAJouer(self, c):
        self.carteAJouer = c
        return self
    
    # fonction utilitaire qui permet de créer les cartes amovibles du jeu en y positionnant
    # aléatoirement les tresors passes en parametre
    # la fonction retourne la liste, mélangée aléatoirement, des cartes ainsi créées
    def creerCartesAmovibles(self, tresorListe):
        l = []
        for _ in range(16):
            l.append(Carte(False, False, True, True).tourneAleatoire())
        for _ in range(6):
            l.append(Carte(False, False, False, True).tourneAleatoire())
        for _ in range(12):
            l.append(Carte(False, True, False, True).tourneAleatoire())
        random.shuffle(l)
        i = 0
        while tresorListe:
            l[i].mettreTresor(tresorListe.pop())
            i += 1
        random.shuffle(l)
        return l
    
    # fonction qui retourne True si le coup proposé correspond au coup interdit
    # elle retourne False sinon
    def coupInterdit(self, direction, rangee):
        return self.interdit is not None and (direction, rangee) == self.interdit
    
    # fonction qui joue la carte amovible dans la direction et sur la rangée passées 
    # en paramètres. Cette fonction
    #      - met à jour le plateau du labyrinthe
    #      - met à jour la carte à jouer
    #      - met à jour la nouvelle direction interdite
    def jouerCarte(self, direction, rangee):
        direction = direction.lower()
        c = getattr(self.getPlateau(), {'n': 'decalageColonneEnBas',
        'e': 'decalageLigneAGauche',
        's': 'decalageColonneEnHaut',
        'o': 'decalageLigneADroite'}[direction])(rangee, self.getCarteAJouer())
        if c.getNbPions() != 0:
            if direction in 'ns':
                self.getPlateau().getVal(0 if direction == 'n' else self.getPlateau().getNbLignes()-1, rangee).addPions(c.getPions())
            else:
                self.getPlateau().getVal(rangee, 0 if direction == 'o' else self.getPlateau().getNbColonnes()-1).addPions(c.getPions())
        c.setPions([])
        self.setCarteAJouer(c)
        self.changerPhase()
        self.interdit = ('seno'['nose'.index(direction)], rangee)
        return self
        
    # Cette fonction tourne la carte à jouer dans le sens indiqué 
    # en paramètre (H horaire A antihoraire)
    def tournerCarte(self, sens='H'):
        self.getCarteAJouer().tournerHoraire() if sens == 'H' else self.getCarteAJouer().tournerAntiHoraire()
    
    # retourne le numéro du trésor à trouver pour le joueur courant
    def getTresorCourant(self):
        return self.getLesJoueurs().prochainTresor(self.getJoueurCourant())
    
    # retourne sous la forme d'un couple (lin,col) la position du trésor à trouver 
    # pour le joueur courant sur le plateau
    def getCoordonneesTresorCourant(self):
        for i in range(self.getPlateau().getNbColonnes()):
            for j in range(self.getPlateau().getNbLignes()):
                if self.getPlateau().getVal(i, j).getTresor() == self.getTresorCourant():
                    return i, j
    
    # retourne sous la forme d'un couple (lin,col) la position du joueur courant sur le plateau
    def getCoordonneesJoueurCourant(self):
        for i in range(self.getPlateau().getNbColonnes()):
            for j in range(self.getPlateau().getNbLignes()):
                if self.getPlateau().getVal(i, j).possedePion(self.getJoueurCourant()):
                    return i, j
        print("Joueur non trouvé")
    
    
    # prend le pion numJoueur sur sur la carte se trouvant en position (lin, col) du plateau
    def prendrePion(self, lin, col, numJoueur):
        if self.getPlateau().getVal(lin, col).possedePion(numJoueur):
            self.getPlateau().getVal(lin, col).prendrePion(numJoueur)
    
    # pose le pion numJoueur sur sur la carte se trouvant en position lin,col du plateau
    def poserPion(self,lin,col,joueur):
        self.getPlateau().getVal(lin, col).poserPion(joueur)

    # indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du labyrinthe
    def accessible(self,ligD,colD,ligA,colA):
        calque = accessible2(self.getPlateau(), (ligD, colD), (ligA, colA))
        return (calque.getVal(ligA, colA) != 0)

    
    # indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du labyrinthe
    # mais la valeur de retour est None s'il n'y a pas de chemin, sinon c'est un chemin possible entre ces deux cases
    def accessibleDist(self,ligD,colD,ligA,colA):
        calque = accessible2(self.getPlateau(), (ligD, colD), (ligA, colA))
        return cheminDecroissant(calque, (ligD, colD), (ligA, colA), self.getPlateau()) if (calque.getVal(ligA, colA) != 0) else None
    
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
    def executerActionPhase1(self,action,rangee):
        try:
            action = action.lower()
        except AttributeError:
            return 3
        if action == 't':
            self.getCarteAJouer().tournerHoraire()
            return 0
        if len(action) == 1 and action in 'neso' and rangee in [1, 3, 5]:
            if self.coupInterdit(action, rangee): return 2
            self.jouerCarte(action, rangee)
            return 1
        return 4
    
    # verifie si le joueur courant peut accéder la case ligA,colA
    # si c'est le cas la fonction retourne une liste représentant un chemin possible
    # sinon ce n'est pas le cas, la fonction retourne None
    def accessibleDistJoueurCourant(self, ligA,colA):
        return self.accessibleDist(self.getCoordonneesJoueurCourant()[0], self.getCoordonneesJoueurCourant()[1], ligA, colA)
    
    # vérifie si le le joueur courant vient de trouver un trésor (si oui fait le nécessaire)
    # vérifie si la partie est terminée, si ce n'est pas le cas passe au joueur suivant
    # le retour de la fonction est un entier qui vaut
    # 0 si le joueur courant n'a pas trouvé de trésor
    # 1 si le joueur courant a trouvé un trésor mais la partie n'est pas terminée
    # 2 si le joueur courant a trouvé son dernier trésor (la partie est donc terminée)
    def finirTour(self):
        ans = 0
        if self.getCoordonneesJoueurCourant() == self.getCoordonneesTresorCourant():
            ans = 1
            self.getLesJoueurs().tresorTrouve(self.getJoueurCourant())
            x, y = self.getCoordonneesJoueurCourant()
            self.getPlateau().getVal(x, y).prendreTresor()
            if self.nbTresorsRestants(self.getJoueurCourant()) == 0:
                return 2
        self.changerPhase()
        self.changerJoueurCourant()
        return ans
        

def marquageDirect(calque,mat,val,marque):
    ans = False
    for lig in range(mat.getNbLignes()):
        for col in range(mat.getNbColonnes()):
            if (calque.getVal(lig, col) == 0 and
            (  (passageEst(mat.getVal(lig, col), mat.getVal(lig, col+1)) and val == calque.getVal(lig, col+1))
            or (passageOuest(mat.getVal(lig, col), mat.getVal(lig, col-1)) and val == calque.getVal(lig, col-1))
            or (passageNord(mat.getVal(lig, col), mat.getVal(lig-1, col)) and val == calque.getVal(lig-1, col))
            or (passageSud(mat.getVal(lig, col), mat.getVal(lig+1, col)) and val == calque.getVal(lig+1, col))
            )):
                calque.setVal(lig, col, marque)
                ans = True
    return ans


# verifie qu'il existe un chemin entre pos1 et pos2 dans la matrice mat
def accessible2(mat,pos1,pos2):
    #initialisation du calque
    calque = Matrice(mat.getNbLignes(), mat.getNbColonnes(), 0)
    calque.setVal(pos1[0], pos1[1], 1)
    #propagation
    pr = True
    val = 1
    while pr and calque.getVal(pos2[0], pos2[1]) == 0:
        pr = marquageDirect(calque, mat, val, val + 1)
        val += 1
    return calque

def passage(plateau, ligD, colD, ligA, colA):
    if ligA == ligD:
        # meme ligne
        if colD == (colA + 1):
            return passageOuest(plateau.getVal(ligD, colD), plateau.getVal(ligA, colA))
        if colD == (colA - 1):
            return passageEst(plateau.getVal(ligD, colD), plateau.getVal(ligA, colA))
    if colD == colA:
        # meme colonne
        if ligD == (ligA + 1):
            return passageNord(plateau.getVal(ligD, colD), plateau.getVal(ligA, colA))
        if ligD == (ligA - 1):
            return passageSud(plateau.getVal(ligD, colD), plateau.getVal(ligA, colA))
    return False

def cheminDecroissant(calque, pos1, pos2, plateau):
    last = calque.getVal(pos2[0], pos2[1])-1
    ans = [pos2]
    while last != 0:
        for lig, col in [(ans[-1][0]-1, ans[-1][1]),(ans[-1][0]+1, ans[-1][1]),(ans[-1][0], ans[-1][1]-1),(ans[-1][0], ans[-1][1]+1)]:
            if calque.getVal(lig, col) == last and passage(plateau, lig, col, ans[-1][0], ans[-1][1]):
                ans.append((lig, col))
                break
        last -= 1
    ans.reverse()
    #print(ans)
    return ans