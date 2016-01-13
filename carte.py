import random

# la liste des caractère semi-graphiques correspondants aux différentes cartes
# l'indice du caractère dans la liste correspond au codage des murs sur la carte
# le caractère 'Ø' indique que l'indice ne correspond pas à une carte
listeCartes=['Ø','╦','╣','╗','╩','═','╝','Ø','╠','╔','║','Ø','╚','Ø','Ø','Ø']

# permet de créer une carte:
# les quatre premiers paramètres sont des booléens indiquant s'il y a un mur ou non dans chaque direction
# tresor est le numéro du trésor qui se trouve sur la carte (0 s'il n'y a pas de trésor)
# pions donne la liste des pions qui seront posés sur la carte (un pion est un entier entre 1 et 4)
def Carte( nord, est, sud, ouest, tresor=0, pions=[]):
    return {'nord': nord,
			'est': est,
			'sud': sud,
			'ouest': ouest,
			'tresor': tresor,
			'pions': set(pions)}
# retourne un booléen indiquant si la carte est valide ou non c'est à dire qu'elle a un ou deux murs
def estValide(c):
    x = 1 if murNord(c) else 0
    x +=  1 if murSud(c) else 0
    x +=  1 if murEst(c) else 0
    x +=  1 if murOuest(c) else 0
    return x in [1, 2]

# retourne un booléen indiquant si la carte possède un mur au nord
def murNord(c):
    return c['nord']

# retourne un booléen indiquant si la carte possède un mur au sud
def murSud(c):
    return c['sud']

# retourne un booléen indiquant si la carte possède un mur à l'est
def murEst(c):
    return c['est']

# retourne un booléen indiquant si la carte possède un mur à l'ouest
def murOuest(c):
    return c['ouest']

# retourne la liste des pions se trouvant sur la carte
def getListePions(c):
    return c['pions']

# retourne le nombre de pions se trouvant sur la carte
def getNbPions(c):
    return len(c['pions'])

# retourne un booléen indiquant si la carte possède le pion passé en paramètre
def possedePion(c,pion):
    return pion in c['pions']

# retourne le codage de la liste des pions
def getPions(c):
    pass

# affecte les pions de la cartes en utilisant directement le codage de la liste des pions
def setPions(c,pions):
    pass

# retourne la valeur du trésor qui se trouve sur la carte (0 si pas de trésor)
def getTresor(c):
    return c['tresor']

# enlève le trésor qui se trouve sur la carte et retourne la valeur de ce trésor
def prendreTresor(c):
	return mettreTresor(c, 0)

# met le trésor passé en paramètre sur la carte et retourne la valeur de l'ancien trésor
def mettreTresor(c,tresor):
    x = c['tresor']
	c['tresor'] = tresor
    return x

# enlève le pion passé en paramètre de la carte. Si le pion n'y était pas ne fait rien
def prendrePion(c, pion):
    c['pions'].discard(pion)
    return c

# pose le pion passé en paramètre sur la carte. Si le pion y était déjà ne fait rien
def poserPion(c, pion):
    c['pions'].add(pion)
    return c

# fait tourner la carte dans le sens horaire
def tournerHoraire(c):
    n = c['nord']
    o = c['ouest']
    s = c['sud']
    e = c['est']
    c['ouest'] = s
    c['sud'] = e
    c['est'] = n
    c['nord'] = o
    return c

# fait tourner la carte dans le sens anti horaire
def tournerAntiHoraire(c):
    n = c['nord']
    o = c['ouest']
    s = c['sud']
    e = c['est']
    c['ouest'] = n
    c['sud'] = o
    c['est'] = s
    c['nord'] = e
    return c

# faire tourner la carte dans nombre de tour aléatoire
def tourneAleatoire(c):
    pass

# code les murs sous la forme d'un entier dont le codage binaire 
# est de la forme bNbEbSbO où bN, bE, bS et bO valent 
#      soit 0 s'il n'y a pas de mur dans dans la direction correspondante
#      soit 1 s'il y a un mur dans la direction correspondante
# bN est le chiffre des unité, bE des dizaine, etc...
# le code obtenu permet d'obtenir l'indice du caractère semi-graphique
# correspondant à la carte dans la liste listeCartes au début de ce fichier
def coderMurs(c):
    x = 8 if murNord(c) else 0
    x +=  4 if murEst(c) else 0
    x +=  2 if murSud(c) else 0
    x +=  1 if murOuest(c) else 0
    return x

# positionne les mur d'une carte en fonction du code décrit précédemment
def decoderMurs(c,code):
    if code > 8:
		code -= 8
		c['nord'] = True
	if code > 4:
		code -= 4
		c['est'] = True
	if code > 2:
		code -= 2
		c['sud'] = True
	if code > 1:
		code -= 1
		c['ouest'] = True
	return c

# fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce script)
def toChar(c):
    return listeCartes[coderMurs(c)]

# suppose que la carte2 est placée au nord de la carte1 et indique
# s'il y a un passage entre ces deux cartes en passant par le nord
def passageNord(carte1,carte2):
    return !murNord(carte1) and !murSud(carte2)
# suppose que la carte2 est placée au sud de la carte1 et indique
# s'il y a un passage entre ces deux cartes en passant par le sud
def passageSud(carte1,carte2):
    return !murSud(carte1) and !murNord(carte2)

# suppose que la carte2 est placée à l'ouest de la carte1 et indique
# s'il y a un passage entre ces deux cartes en passant par l'ouest
def passageOuest(carte1,carte2):
    return !murOuest(carte1) and !murEst(carte2)

# suppose que la carte2 est placée à l'est de la carte1 et indique
# s'il y a un passage entre ces deux cartes en passant par l'est
def passageEst(carte1,carte2):
    return !murEst(carte1) and !murOuest(carte2)
