import math as m
import matplotlib.pyplot as plt
import pandas as pd
from operator import itemgetter
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

#extraction
def maListe():
    L=[]
    data=pd.read_csv("iris.txt")
    database=data.to_numpy() 
    for line in database:
        L.append([line[4],float(line[0]),float(line[1]),float(line[2])])
    return L

#affichage 3D
def D3(maListe):
    L=maListe
    x=[];y=[];z=[]
    x1=[];y1=[];z1=[]
    x2=[];y2=[];z2=[]
    for i in L:
        if(i[0]=='Iris-setosa'):
            x.append(i[1])
            y.append(i[2])
            z.append(i[3])
        if(i[0]=='Iris-versicolor'):
            x1.append(i[1])
            y1.append(i[2])
            z1.append(i[3])
        if(i[0]=='Iris-virginica'):
            x2.append(i[1])
            y2.append(i[2])
            z2.append(i[3])        
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(x,y,z,c='r',label='Iris-setosa')
    ax.scatter(x1,y1,z1,c='b',label='Iris-versicolor')
    ax.scatter(x2,y2,z2,c='g',label='Iris-virginica')
    ax.set_xlabel('Sepal length')
    ax.set_ylabel('Sepal width')
    ax.set_zlabel('Petal length')
    plt.legend()
    plt.show()
    return None

#calcule de distance
def distance(maListe,objet):
    maDist=[]
    for i in maListe:
        dist=m.sqrt((i[1]-objet[1])**2+(i[2]-objet[2])**2+(i[3]-objet[3])**2)
        maDist.append([i[0],dist])
    return maDist

#trier les distances
def trier(maDist):
    maDist=sorted(maDist,key=itemgetter(1))
    return maDist

#donne le top classement
def top(maDist,n):
    top=[]
    for i in range(n):
        top.append(maDist[i])
    return top


#verification
def verif(top):
    Nom=['Iris-setosa','Iris-versicolor','Iris-virginica']
    ctp=[0,0,0]
    for i in top:
        if(i[0]==Nom[0]):
            ctp[0]+=1
        if(i[0]==Nom[1]):
            ctp[1]+=1
        if(i[0]==Nom[2]):
            ctp[2]+=1
    a=max(ctp)
    for i in range(len(Nom)):
        if(ctp[i]==a):
            return(Nom[i])

#matrice de confusion
def tableauK():
    K=[['X','Iris-setosa','Iris-versicolor','Iris-virginica'],
       ['Iris-setosa',0,0,0],
       ['Iris-versicolor',0,0,0],
       ['Iris-virginica',0,0,0]]
    return K

# caractéristique d'une fleur
def objet():
    n=0
    L=['X','Iris-setosa','Iris-versicolor','Iris-virginica']
    print('1) Iris-setosa \n2) Iris-versicolor \n3) Iris-virginica')
    O=['.',0,0,0]
    while(n not in [1,2,3]):
        n=eval(input("fleur ?\n"))
    O[0]=L[n]
    print("Sepal length ?\n")
    O[1]=float(input())
    print("Sepal width ?\n")
    O[2]=float(input())
    print("Petal length ?\n")
    O[3]=float(input())
    return O


# ajouter fleur
def observation():
    n=0
    Reel=[]
    while(n==0):
        Reel.append(objet())
        print('0 si ajouter | autre sinon\n')
        n=eval(input())
    return Reel

def Test():
    L=[]
    data=pd.read_csv("test.txt")
    database=data.to_numpy() 
    for line in database:
        L.append([line[4],float(line[0]),float(line[1]),float(line[2])])
    return L

def K_nn(classement,Reel):
    
    #initialisation
    K=tableauK()
    Prediction=[]
    L=maListe()
    
    #verification
    for obj in Reel:
        maDist=distance(L,obj)
        maDist=trier(maDist)
        Top=top(maDist,classement)
        Prediction.append(verif(Top))
        
    # matrice K
    for i in range(len(Prediction)):
        ligne=3# prediction
        colonne=3# reel
        #insertion colonne
        if(Reel[i][0]=='Iris-setosa'):
            colonne=1
        if(Reel[i][0]=='Iris-versicolor'):
            colonne=2
        #insertion ligne
        if(Prediction[i]=='Iris-setosa'):
            ligne=1
        if(Prediction[i]=='Iris-versicolor'):
            ligne=2
        K[ligne][colonne]+=1
    cpt=K[1][1]+K[2][2]+K[3][3]
    return K,cpt

def Liste_k_nn():
    print("le but est de retourner le meilleur K ")
    ###
    #donner les plantes à observer
    #Reel=observation()
    ###
    Reel=Test()
    print("il y a ",len(Reel)," de tests")
    classement=10
    ListeK_nn=[]
    Liste_cpt=[]
    for i in range(51):
        K,C=K_nn(classement+i,Reel)
        ListeK_nn.append(K)
        Liste_cpt.append(C)
    return ListeK_nn,Liste_cpt

#affichage initial
D3(maListe())

# en cours de calcul
LK,Y=Liste_k_nn()
N=np.arange(10,61,1)
plt.plot(N,Y)
plt.title('Nombre de réponse correcte en fonction du top')
plt.show()

#Solution
print(LK[Y.index(max(Y))])
print("le meilleur k est : ",10+Y.index(max(Y)))
















            
            