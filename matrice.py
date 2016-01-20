import random

#-----------------------------------------
# contructeur et accesseurs
#-----------------------------------------

#crée une matrice de nbLignes lignes sur nbColonnes colonnes en mettant valeurParDefaut
# dans chacune des cases
# liste de nbLignes listes de nbColonnes valeurs
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
    if lig < 0 or lig >= getNbLignes(mat) or col < 0 or col >= getNbColonnes(mat): return None#si la valeur lig ou col n'existe pas
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
    matrice[numLig].append(nouvelleValeur)#on ajoute la nouvelle valeur dans la ligne voulu
    return matrice[numLig].pop(0)#retourne et supprime la premiere valeur de la ligne

# decale la ligne numLig d'une case vers la droite en insérant la nouvelleValeur
# dans la case ainsi libérée
# la fonction retourne la valeur de la case "ejectée" par le décalage
def decalageLigneADroite(matrice, numLig, nouvelleValeur=0):
    matrice[numLig].insert(0, nouvelleValeur)#on ajoute la nouvelle valeur dans la ligne voulu
    return matrice[numLig].pop()# retourne et supprime la derniere valeur de la ligne

# decale la colonne numCol d'une case vers le haut en insérant la nouvelleValeur
# dans la case ainsi libérée
# la fonction retourne la valeur de la case "ejectée" par le décalage
def decalageColonneEnHaut(matrice, numCol, nouvelleValeur=0):
    ans = getVal(matrice, 0, numCol)# recupere la valeur de la case éjectée sois la premiere de la collone
    for i in range(1, getNbColonnes(matrice)):#pour toutes les cases de la collone sauf la premiere
        setVal(matrice, i-1, numCol, getVal(matrice, i, numCol)) # affecte à la case precedente la valeur de la case courante
    setVal(matrice, getNbLignes(matrice)-1, numCol, nouvelleValeur)# affecte à la derniere case la nouvelle valeur
    return ans#retourne la valeur de la case éjectée
    
# decale la colonne numCol d'une case vers le bas en insérant la nouvelleValeur
# dans la case ainsi libérée
# la fonction retourne la valeur de la case "ejectée" par le décalage
def decalageColonneEnBas(matrice, numCol, nouvelleValeur=0):
    ans = getVal(matrice, getNbLignes(matrice)-1, numCol)#recupere la valeur de la case éjectée sois la derniere de la colonne
    for i in range(getNbLignes(matrice)-2, -1, -1):#pour toutes les cases de la colonne
        setVal(matrice, i+1, numCol, getVal(matrice, i, numCol))#affecte à la case suivante la valeur de la case courante
    setVal(matrice, 0, numCol, nouvelleValeur)#affecte à la premiere case la nouvelle valeur
    return ans#retoune la valeur de la case éjectée 


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

if __name__ == '__main__':
    m = Matrice(4, 4, 8)
    decalageColonneEnBas(m, 0, 0)
    decalageColonneEnHaut(m, 3, 3)
    decalageLigneADroite(m, 1, 1)
    decalageLigneAGauche(m, 2, 2)
    afficheMatrice(m)
