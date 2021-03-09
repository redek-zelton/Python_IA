
import math as m
import numpy as np
import random as rd
import matplotlib.pyplot as plt

class Point:
    def __init__(self,visite,x,y,couleur):
        self.visite=visite # false or true
        self.x=x#abscisse
        self.y=y#ordonné
        self.couleur=couleur
        
    def __str__(self):
        return str(self.visite)+" "+str(self.x)+" "+str(self.y)+" "+str(self.couleur)
        
    def dist(self,P):
        return m.sqrt(float(self.x-P.x)**2+float(self.y-P.y)**2)
    




def DBSCAN(D,eps,MinPts):
    C=0
    for P in D:
        if(P.visite==False):
            P.visite=True
            PtsVoisins=espilonVoisinage(D,P,eps)
            if(tailleDe(PtsVoisins)<MinPts):
                P.visite=True
            else:
                C+=1
                etendreCluster(D,P,PtsVoisins,C,eps,MinPts)

def etendreCluster(D,P,PtsVoisins,C,eps,MinPts):
    Cluster=[]
    Cluster.append(P)
    for Pr in PtsVoisins:# Pr est p'
        if(Pr.visite==False):
            Pr=True
            PtsVoisinpr=espilonVoisinage(D,Pr,eps)
            if(tailleDe(PtsVoisinpr)>=MinPts):
                PtsVoisins=set(PtsVoisins+PtsVoisinpr)
            if(Pr not in Cluster):
                Cluster.append(Pr)

def espilonVoisinage(D,P,eps):
    L=[]
    for d in D:
        if(d.dist(P)<=eps):
            L.append(d)
    return L

def tailleDe(L):
    taille=0
    for P in L:
        if(P.visite==True):
            taille+=1
    return taille

def ListeRdPoint(n):
    choix=[True,False,False]
    col=['r','b','.','.']
    L=[]
    for i in range(n):
        visite=rd.choice(choix)
        x=rd.random()*10
        y=rd.random()*10
        couleur=rd.choice(col)
        P=Point(visite,x,y,couleur)
        L.append(P)
    return L

def affiche(L):
    for i in L:
        print(i)


L=ListeRdPoint(20)
affiche(L)
MinPts=3
eps=1
DBSCAN(L,eps,MinPts)





