import random

#-----------------------------------------
# contructeur et accesseurs
#-----------------------------------------

#crée une matrice de nbLignes lignes sur nbColonnes colonnes en mettant valeurParDefaut
# dans chacune des cases
def Matrice(nbLignes,nbColonnes,valeurParDefaut=0):
    return [[valeurParDefaut for _ in range(nbColonnes)] for _ in range(nbLignes)]

# retourne le nombre de ligne de la matrice
def getNbLignes(matrice):
    return len(matrice)

#retourne le nombre de colonnes de la matrice
def getNbColonnes(matrice):
    return len(matrice[0])

# retourne la valeur qui se trouve à la ligne et la colonne passées en paramètres
def getVal(mat,lig,col):
    if lig < 0 or lig >= getNbLignes(mat) or col < 0 or col >= getNbColonnes(mat): return None
    return mat[lig][col]

# place la valeur à l'emplacement ligne colonne de la matrice
def setVal(matrice,lig,col,val):
    #print(val)
    matrice[lig][col] = val
    return matrice



#------------------------------------------        
# decalages A IMPLEMENTER
#------------------------------------------

# decale la ligne numLig d'une case vers la gauche en insérant la nouvelleValeur
# dans la case ainsi libérée
# la fonction retourne la valeur de la case "ejectée" par le décalage
def decalageLigneAGauche(matrice, numLig, nouvelleValeur=0):
    pass

# decale la ligne numLig d'une case vers la droite en insérant la nouvelleValeur
# dans la case ainsi libérée
# la fonction retourne la valeur de la case "ejectée" par le décalage
def decalageLigneADroite(matrice, numLig, nouvelleValeur=0):
    pass

# decale la colonne numCol d'une case vers le haut en insérant la nouvelleValeur
# dans la case ainsi libérée
# la fonction retourne la valeur de la case "ejectée" par le décalage
def decalageColonneEnHaut(matrice, numCol, nouvelleValeur=0):
    pass


# decale la colonne numCol d'une case vers le haut en insérant la nouvelleValeur
# dans la case ainsi libérée
# la fonction retourne la valeur de la case "ejectée" par le décalage
def decalageColonneEnBas(matrice, numCol, nouvelleValeur=0):
    pass


#-----------------------------------------
# entrées sorties
#-----------------------------------------
#sauvegarde une matrice en mode texte 
# ATTENTION NE MARCHE QUE POUR DES MATRICE CONTENANT DES TYPES SIMPLES
def sauveMatrice(matrice,nomFic):
    fic=open(nomFic,'w')
    ligne=str(getNbLignes(matrice))+','+str(getNbColonnes(matrice))+'\n'
    fic.write(ligne)
    for i in range(getNbLignes(matrice)):
        ligne=''
        for j in range(getNbColonnes(matrice)-1):
            val=getVal(matrice,i,j)
            if val==None:
                ligne+=','
            else:
                ligne+=str(val)+','
        val=getVal(matrice,i,j+1)
        if val==None:
            ligne+='\n'
        else:
            ligne+=str(val)+'\n'
        fic.write(ligne)
    fic.close()

# construit une matrice à partir d'un fichier texte 
# ATTENTION NE MARCHE QUE POUR DES MATRICE CONTENANT DES TYPES SIMPLES
def chargeMatrice(nomFic,typeVal='int'):
    fic=open(nomFic,'r')
    ligneLinCol=fic.readline()
    listeLinCol=ligneLinCol.split(',')
    matrice=Matrice(int(listeLinCol[0]),int(listeLinCol[1]))
    i=0
    for ligne in fic:
        listeVal=ligne.split(",")
        j=0
        for elem in listeVal:
            if elem=="" or elem=="\n":
                setVal(matrice,i,j,None)
            elif typeVal=='int':
                setVal(matrice,i,j,int(elem))
            elif typeVal=='float':
                setVal(matrice,i,j,float(elem))
            elif typeVal=='bool':
                setVal(matrice,i,j,bool(elem))
            else:
                matrice.setVal(i,j,elem)
            j+=1
        i+=1
    return matrice

# fonction utilitataire
def afficheLigneSeparatrice(matrice,tailleCellule=4):
    print()
    for i in range(getNbColonnes(matrice)+1):
        print('-'*tailleCellule+'+',end='')
    print()

# fonction d'affichage d'une matrice
def afficheMatrice(matrice,tailleCellule=4):
    nbColonnes=getNbColonnes(matrice)
    nbLignes=getNbLignes(matrice)
    print(' '*tailleCellule+'|',end='')
    for i in range(nbColonnes):
        print(str(i).center(tailleCellule)+'|',end='')
    afficheLigneSeparatrice(matrice,tailleCellule)
    for i in range(nbLignes):
        print(str(i).rjust(tailleCellule)+'|',end='')
        for j in range(nbColonnes):
            print(str(getVal(matrice,i,j)).rjust(tailleCellule)+'|',end='')
        afficheLigneSeparatrice(matrice,tailleCellule)
    print()
    
