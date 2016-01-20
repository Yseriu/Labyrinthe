import random

# -----------------------------------------
# contructeur et accesseurs
# -----------------------------------------

# crée une matrice de nbLignes lignes sur nbColonnes colonnes en mettant valeurParDefaut
# dans chacune des cases
class Matrice(object):
    def __init__(self,nbLignes,nbColonnes,valeurParDefaut=0):
        self.matrice=[[valeurParDefaut for _ in range(nbColonnes)] for _ in range(nbLignes)]

    # retourne le nombre de ligne de la matrice
    def getNbLignes(self):
        return len(self.matrice)

    #retourne le nombre de colonnes de la matrice
    def getNbColonnes(self):
        return len(self.matrice[0])

    # retourne la valeur qui se trouve à la ligne et la colonne passées en paramètres
    def getVal(self,lig,col):
        if lig < 0 or lig >= self.getNbLignes() or col < 0 or col >= self.getNbColonnes(): return None
        return self.matrice[lig][col]

    # place la valeur à l'emplacement ligne colonne de la matrice
    def setVal(self,lig,col,val):
        #print(val)
        self.matrice[lig][col] = val
        return self

    # ------------------------------------------
    # decalages A IMPLEMENTER
    # ------------------------------------------

    # decale la ligne numLig d'une case vers la gauche en insérant la nouvelleValeur
    # dans la case ainsi libérée
    # la fonction retourne la valeur de la case "ejectée" par le décalage
    def decalageLigneAGauche(self, numLig, nouvelleValeur=0):
        self.matrice[numLig].append(nouvelleValeur)
        return self.matrice[numLig].pop(0)

    # decale la ligne numLig d'une case vers la droite en insérant la nouvelleValeur
    # dans la case ainsi libérée
    # la fonction retourne la valeur de la case "ejectée" par le décalage
    def decalageLigneADroite(self, numLig, nouvelleValeur=0):
        self.matrice[numLig].insert(0, nouvelleValeur)
        return self.matrice[numLig].pop()

    # decale la colonne numCol d'une case vers le haut en insérant la nouvelleValeur
    # dans la case ainsi libérée
    # la fonction retourne la valeur de la case "ejectée" par le décalage
    def decalageColonneEnHaut(self, numCol, nouvelleValeur=0):
        ans = self.getVal(0, numCol)
        for i in range(1, self.getNbColonnes()):
            self.setVal(i-1, numCol, self.getVal(i, numCol))
        self.setVal(self.getNbLignes()-1, numCol, nouvelleValeur)
        return ans

    # decale la colonne numCol d'une case vers le haut en insérant la nouvelleValeur
    # dans la case ainsi libérée
    # la fonction retourne la valeur de la case "ejectée" par le décalage
    def decalageColonneEnBas(self, numCol, nouvelleValeur=0):
        ans = self.getVal(self.getNbLignes()-1, numCol)
        for i in range(self.getNbLignes()-2, -1, -1):
            self.setVal(i+1, numCol, self.getVal(i, numCol))
        self.setVal(0, numCol, nouvelleValeur)
        return ans


    # -----------------------------------------
    # entrées sorties
    # -----------------------------------------
    # sauvegarde une matrice en mode texte
    # ATTENTION NE MARCHE QUE POUR DES MATRICE CONTENANT DES TYPES SIMPLES
    def sauveMatrice(self,nomFic):
        fic=open(nomFic,'w')
        ligne=str(self.getNbLignes())+','+str(self.getNbColonnes())+'\n'
        fic.write(ligne)
        for i in range(self.getNbLignes()):
            ligne=''
            for j in range(self.getNbColonnes()-1):
                val=self.getVal(i,j)
                if val==None:
                    ligne+=','
                else:
                    ligne+=str(val)+','
            val=self.getVal(i,j+1)
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
                    matrice.setVal(i,j,None)
                elif typeVal=='int':
                    matrice.setVal(i,j,int(elem))
                elif typeVal=='float':
                    matrice.setVal(i,j,float(elem))
                elif typeVal=='bool':
                    matrice.setVal(i,j,bool(elem))
                else:
                    matrice.setVal(i,j,elem)
                j+=1
            i+=1
        return matrice

    # fonction utilitataire
    def afficheLigneSeparatrice(self,tailleCellule=4):
        print()
        for i in range(self.getNbColonnes()+1):
            print('-'*tailleCellule+'+',end='')
        print()

    # fonction d'affichage d'une matrice
    def afficheMatrice(self,tailleCellule=4):
        nbColonnes=self.getNbColonnes()
        nbLignes=self.getNbLignes()
        print(' '*tailleCellule+'|',end='')
        for i in range(nbColonnes):
            print(str(i).center(tailleCellule)+'|',end='')
        self.afficheLigneSeparatrice(tailleCellule)
        for i in range(nbLignes):
            print(str(i).rjust(tailleCellule)+'|',end='')
            for j in range(nbColonnes):
                print(str(self.getVal(i,j)).rjust(tailleCellule)+'|',end='')
            self.afficheLigneSeparatrice(tailleCellule)
        print()

if __name__ == '__main__':
    m = Matrice(4, 4, 8)
    m.decalageColonneEnBas(0, 0)
    m.decalageColonneEnHaut(3, 3)
    m.decalageLigneADroite(1, 1)
    m.decalageLigneAGauche(2, 2)
    m.afficheMatrice()
