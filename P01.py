# -*- coding: utf-8 -*-


# 22400305 DJOKO FOKOU Keyssel
# 22410790 ICHAS Gaspard


            #section1: les imports
from P01_utils import *
import math
import numpy as np 
import scipy.spatial.distance as sc

            #section2:
X_train,y_train=lire_donnees(100)
X_test,y_test=lire_donnees(10)
visualiser_donnees(X_test,y_test)
visualiser_donnees(X_train,y_train)

                    
                #3.3
#1

def dist(x_i,x_j):
    if len(x_i)==len(x_j):
        l=[]
        for i in range(len(x_i)):
            l.append((x_i[i]-x_j[i])**2)
        d=math.sqrt(sum(l))
    else:
        d="erreur vecteur de longueurs differentes"
    return(d)

#2

def proche(X,Z,k):
    l=[]
    for i in X:
        l.append(dist(i,Z))
    J=np.argsort(l)         #indices des valeurs triee par ordre croissant
    B=list(J[:k])
    return(B) #liste d'indices

#3

def classe(L,o="F"):    # o valeur par defaut en cas d'egalite?
    f=L.count("F")
    if f/len(L)>0.5:
        p="F"
    elif f/len(L)<0.5:
        p="H"
    else:
        p=o  
    return(p)
#4

def k_plus_proches_voisins_liste(X,Y,Z,k=1):
    l=[]
    for elem in Z:
        q=proche(X,elem,k)
        e=classe(list(Y[q]))
        l.append(e)
    return(l)

                #3.4
        

def k_plus_proches_voisins_liste_numpy(X,Y,Z,k=1):
    I=sc.cdist(Z,X)     #array contenaant les distances pour chaque elem de Z avec les elem de X  dim=10*100
    J=np.argsort(I)        #tri par indices sur chaque ligne
    B=J[:,:k]           #on garde les K premiere valeurs sur chaque ligne 
    l=[]
    for i in range(len(B)):
        h=[]
        h.extend(list(Y[B[i,:]])) #liste avec les genre des k plus proches
        s=h.count("F")/len(h)       #proportion de femmes dans les k plus proches
        if s<=0.5:
            u="H"
        else:
            u="F"
        l.append(u)
        
    return(l)

        
        #section3:Tests
print(k_plus_proches_voisins_liste(X_train,y_train,X_test,5))
print(k_plus_proches_voisins_liste_numpy(X_train,y_train,X_test,5))
   



