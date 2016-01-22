import random

# la liste des caractère semi-graphiques correspondants aux différentes cartes
# l'indice du caractère dans la liste correspond au codage des murs sur la carte
# le caractère 'Ø' indique que l'indice ne correspond pas à une carte
listeCartes=['Ø','╦','╣','╗','╩','═','╝','Ø','╠','╔','║','Ø','╚','Ø','Ø','Ø']
class Carte(object):
    # permet de créer une carte:
    # les quatre premiers paramètres sont des booléens indiquant s'il y a un mur ou non dans chaque direction
    # tresor est le numéro du trésor qui se trouve sur la carte (0 s'il n'y a pas de trésor)
    # pions donne la liste des pions qui seront posés sur la carte (un pion est un entier entre 1 et 4)
    def __init__(self, nord, est, sud, ouest, tresor=0, pions=[]):
        self.nord = nord
        self.est = est
        self.sud = sud
        self.ouest = ouest
        self.tresor = tresor
        self.pions = set(pions)
    # retourne un booléen indiquant si la carte est valide ou non c'est à dire qu'elle a un ou deux murs
    def estValide(self):
        x = 1 if self.murNord() else 0
        x +=  1 if self.murSud() else 0
        x +=  1 if self.murEst() else 0
        x +=  1 if self.murOuest() else 0
        return x in [1, 2]
    
    # retourne un booléen indiquant si la carte possède un mur au nord
    def murNord(self):
        return self.nord
    
    # retourne un booléen indiquant si la carte possède un mur au sud
    def murSud(self):
        return self.sud
    
    # retourne un booléen indiquant si la carte possède un mur à l'est
    def murEst(self):
        return self.est
    
    # retourne un booléen indiquant si la carte possède un mur à l'ouest
    def murOuest(self):
        return self.ouest
    
    # retourne la liste des pions se trouvant sur la carte
    def getListePions(self):
        return list(self.pions)
    
    # retourne le nombre de pions se trouvant sur la carte
    def getNbPions(self):
        return len(self.pions)
    
    # retourne un booléen indiquant si la carte possède le pion passé en paramètre
    def possedePion(self,pion):
        return pion in self.pions
    
    # retourne le codage de la liste des pions
    def getPions(self):
        return list(self.pions)
    
    # affecte les pions de la cartes en utilisant directement le codage de la liste des pions
    def setPions(self, pions):
        self.pions = set(pions)
    
    def addPions(self,pions):
        self.pions = self.pions | set(pions)
    
    # retourne la valeur du trésor qui se trouve sur la carte (0 si pas de trésor)
    def getTresor(self):
        return self.tresor
    
    # enlève le trésor qui se trouve sur la carte et retourne la valeur de ce trésor
    def prendreTresor(self):
        return self.mettreTresor(0)
    
    # met le trésor passé en paramètre sur la carte et retourne la valeur de l'ancien trésor
    def mettreTresor(self,tresor):
        x = self.tresor
        self.tresor = tresor
        return x
    
    # enlève le pion passé en paramètre de la carte. Si le pion n'y était pas ne fait rien
    def prendrePion(self, pion):
        self.pions.discard(pion)
        return self
    
    # pose le pion passé en paramètre sur la carte. Si le pion y était déjà ne fait rien
    def poserPion(self, pion):
        self.pions.add(pion)
        return self
    
    # fait tourner la carte dans le sens horaire
    def tournerHoraire(self):
        n = self.nord
        o = self.ouest
        s = self.sud
        e = self.est
        self.ouest = s
        self.sud = e
        self.est = n
        self.nord = o
        return self
    
    # fait tourner la carte dans le sens anti horaire
    def tournerAntiHoraire(self):
        n = self.nord
        o = self.ouest
        s = self.sud
        e = self.est
        self.ouest = n
        self.sud = o
        self.est = s
        self.nord = e
        return self
    
    # faire tourner la carte dans nombre de tour aléatoire
    def tourneAleatoire(self):
        for _ in range(random.randint(0, 4)):
            self.tournerHoraire()
        return self
    
    # code les murs sous la forme d'un entier dont le codage binaire 
    # est de la forme bNbEbSbO où bN, bE, bS et bO valent 
    #      soit 0 s'il n'y a pas de mur dans dans la direction correspondante
    #      soit 1 s'il y a un mur dans la direction correspondante
    # bN est le chiffre des unité, bE des dizaine, etc...
    # le code obtenu permet d'obtenir l'indice du caractère semi-graphique
    # correspondant à la carte dans la liste listeCartes au début de ce fichier
    def coderMurs(self):
        x = 1 if self.murNord() else 0
        x += 2 if self.murEst() else 0
        x += 4 if self.murSud() else 0
        x += 8 if self.murOuest() else 0
        return x
    
    # positionne les mur d'une carte en fonction du code décrit précédemment
    def decoderMurs(self,code):
        if code > 8:
            code -= 8
            self.ouest = True
        if code > 4:
            code -= 4
            self.sud = True
        if code > 2:
            code -= 2
            self.est = True
        if code > 1:
            code -= 1
            self.nord = True
        return self
    
    # fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce script)
    def toChar(self):
        return listeCartes[self.coderMurs()]

    # Ces fonctions sont toujours statiques : elles comparent deux cartes, nous avons donc choisi de les laisser statiques
    # Cependant, leur version objet a également été écrite, la voici
    #
    # def passageNord(self,carte2):
    #     if carte2 == None: return False
    #     return (not self.murNord()) and (not carte2.murSud())
    #
    # def passageSud(self,carte2):
    #     if carte2 == None: return False
    #     return (not self.murSud()) and (not carte2.murNord())
    #
    # def passageOuest(self,carte2):
    #     if carte2 == None: return False
    #     return (not self.murOuest()) and (not carte2.murEst())
    #
    # def passageEst(self,carte2):
    #     if carte2 == None: return False
    #     return (not self.murEst()) and (not carte2.murOuest())

# suppose que la carte2 est placée au nord de la carte1 et indique
# s'il y a un passage entre ces deux cartes en passant par le nord
def passageNord(carte1,carte2):
    if carte1 == None or carte2 == None: return False
    return (not carte1.murNord()) and (not carte2.murSud())
# suppose que la carte2 est placée au sud de la carte1 et indique
# s'il y a un passage entre ces deux cartes en passant par le sud
def passageSud(carte1,carte2):
    if carte1 == None or carte2 == None: return False
    return (not carte1.murSud()) and (not carte2.murNord())

# suppose que la carte2 est placée à l'ouest de la carte1 et indique
# s'il y a un passage entre ces deux cartes en passant par l'ouest
def passageOuest(carte1,carte2):
    if carte1 == None or carte2 == None: return False
    return (not carte1.murOuest()) and (not carte2.murEst())

# suppose que la carte2 est placée à l'est de la carte1 et indique
# s'il y a un passage entre ces deux cartes en passant par l'est
def passageEst(carte1,carte2):
    if carte1 == None or carte2 == None: return False
    return (not carte1.murEst()) and (not carte2.murOuest())
