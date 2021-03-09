import random as rd

def affichage(plateau):
    for i in plateau:
        print(i,"\n")
    

#donne les actions  
def action(plateau):
    L=[]
    for i in range(3):
        for j in range(3):
            if (plateau[i][j]=="."):
                L.append([i,j])
    return L


#realisation de l'IA
def realise(plateau,a):
    plateau[a[0]][a[1]]='O'
    return plateau


#realisation du joueur
def realiseJoueur(plateau,a):
    plateau[a[0]][a[1]]='X'
    return plateau



def Terminal_test(plateau):
    #verif ligne
    for i in range(3):
        if(plateau[i][0]==plateau[i][1] and plateau[i][0]==plateau[i][2]):
            if(plateau[i][0]=='X' or plateau[i][0]=='O'):
                return True
    #verif colonne
    for i in range(3):
        if(plateau[0][i]==plateau[1][i] and plateau[0][i]==plateau[2][i]):
            if(plateau[0][i]=='X' or plateau[0][i]=='O'):
                return True
    #verif diagonal
    if(plateau[0][0]==plateau[1][1] and plateau[0][0]==plateau[2][2]):
        if(plateau[0][0]=='X' or plateau[0][0]=='O'):
                return True
    if(plateau[0][2]==plateau[1][1] and plateau[0][2]==plateau[2][0]):
        if(plateau[2][0]=='X' or plateau[2][0]=='O'):
                return True
    #tous non remplis
    for i in range(3):
        for j in range(3):
            if(plateau[i][j]=='.'):
                return False
    return True #remplis


def utility(plateau):
    JVic=-5000 # risque victoire du joueur(2/3)
    IAVic=5000# victoire IA
    joueur=-50
    IAproche=50 # 2/3
    J=-1# 1/3
    IA=1# 1/3
    cpt=0
     #en cas de victoire
    for i in range(3):
        if(plateau[i][0]==plateau[i][1] and plateau[i][0]==plateau[i][2]):
            if(plateau[i][0]=='O'):
                return IAVic        
    for i in range(3):
        if(plateau[0][i]==plateau[1][i] and plateau[0][i]==plateau[2][i]):
            if(plateau[0][i]=='O'):
                return IAVic
    if(plateau[0][0]==plateau[1][1] and plateau[0][0]==plateau[2][2]):
        if(plateau[0][0]=='O'):
            return IAVic
    if(plateau[0][2]==plateau[1][1] and plateau[0][2]==plateau[2][0]):
        if(plateau[2][0]=='O'):
            return IAVic
    # en cas de defaite
    for i in range(3):
        if(plateau[i][0]==plateau[i][1] and plateau[i][0]==plateau[i][2]):
            if(plateau[i][0]=='O'):
                return JVic         
    for i in range(3):
        if(plateau[0][i]==plateau[1][i] and plateau[0][i]==plateau[2][i]):
            if(plateau[0][i]=='O'):
                return JVic
    if(plateau[0][0]==plateau[1][1] and plateau[0][0]==plateau[2][2]):
        if(plateau[0][0]=='O'):
            return JVic
    if(plateau[0][2]==plateau[1][1] and plateau[0][2]==plateau[2][0]):
        if(plateau[2][0]=='O'):
            return JVic
    # en cours de jeu
    # verif ligne 2/3
    for i in range(3):
        if(plateau[i][0]==plateau[i][1] and plateau[i][2]=='.'):
            if(plateau[i][0]=='X'):
                cpt+=joueur
            if(plateau[i][0]=='O'):
                cpt+=IAproche
    for i in range(3):
        if(plateau[i][0]==plateau[i][2] and plateau[i][1]=='.'):
            if(plateau[i][0]=='X'):
                cpt+=joueur
            if(plateau[i][0]=='O'):
                cpt+=IAproche
    for i in range(3):
        if(plateau[i][2]==plateau[i][1] and plateau[i][0]=='.'):
            if(plateau[i][2]=='X'):
                cpt+=joueur
            if(plateau[i][2]=='O'):
                cpt+= IAproche
                
    #verif colonne 2/3
    for i in range(3):
        if(plateau[0][i]==plateau[1][i] and plateau[2][i]=='.'):
            if(plateau[0][i]=='X'):
                cpt+=joueur
            if(plateau[0][i]=='O'):
                cpt+=IAproche
    for i in range(3):
        if(plateau[0][i]==plateau[2][i] and plateau[1][i]=='.'):
            if(plateau[0][i]=='X'):
                cpt+=joueur
            if(plateau[0][i]=='O'):
                cpt+=IAproche
    for i in range(3):
        if(plateau[2][i]==plateau[1][i] and plateau[0][i]=='.'):
            if(plateau[2][i]=='X'):
                cpt+=joueur
            if(plateau[2][i]=='O'):
                cpt+=IAproche
    #verif diagonal 1/3
    if(plateau[0][0]==plateau[1][1] and plateau[2][2]=='.'):
        if(plateau[0][0]=='X'):
            cpt+=joueur
        if(plateau[0][0]=='O'):
            cpt+=IAproche
    if(plateau[0][0]==plateau[2][2] and plateau[1][1]=='.'):
        if(plateau[0][0]=='X'):
            cpt+=joueur
        if(plateau[0][0]=='O'):
            cpt+=IAproche
    if(plateau[2][2]==plateau[1][1] and plateau[0][0]=='.'):
        if(plateau[2][2]=='X'):
            cpt+=joueur
        if(plateau[2][2]=='O'):
            cpt+=IAproche
    if(plateau[0][2]==plateau[1][1] and plateau[2][0]=='.'):
        if(plateau[0][2]=='X'):
            cpt+=joueur
        if(plateau[0][2]=='O'):
            cpt+=IAproche
    if(plateau[0][2]==plateau[2][0] and plateau[1][1]=='.'):
        if(plateau[0][2]=='X'):
            cpt+=joueur
        if(plateau[0][2]=='O'):
            cpt+=IAproche
    if(plateau[2][0]==plateau[1][1] and plateau[0][2]=='.'):
        if(plateau[2][0]=='X'):
            cpt+=joueur
        if(plateau[2][0]=='O'):
            cpt+=IAproche
             
# mode joueur        
# verif ligne 1/3  
    for i in range(3):
        if(plateau[i][0]==plateau[i][1] and plateau[i][2]=='X'):
            if(plateau[i][0]=='.'):
                cpt+=J
    for i in range(3):
        if(plateau[i][0]==plateau[i][2] and plateau[i][1]=='X'):
                cpt+=J
    for i in range(3):
        if(plateau[i][2]==plateau[i][1] and plateau[i][0]=='X'):
                cpt+= J         
    #verif colonne 1/3
    for i in range(3):
        if(plateau[0][i]==plateau[1][i] and plateau[2][i]=='X'):
            if(plateau[0][i]=='.'):
                cpt+=J
    for i in range(3):
        if(plateau[0][i]==plateau[2][i] and plateau[1][i]=='X'):
            if(plateau[0][i]=='.'):
                cpt+=J
    for i in range(3):
        if(plateau[2][i]==plateau[1][i] and plateau[0][i]=='X'):
            if(plateau[2][i]=='.'):
                cpt+=J
    #verif diagonal 1/3
    if(plateau[0][0]==plateau[1][1] and plateau[2][2]=='X'):
        if(plateau[0][0]=='.'):
             cpt+=J
    if(plateau[0][0]==plateau[2][2] and plateau[1][1]=='X'):
        if(plateau[0][0]=='.'):
             cpt+=J
    if(plateau[2][2]==plateau[1][1] and plateau[0][0]=='X'):
        if(plateau[2][2]=='.'):
             cpt+=J
    if(plateau[0][2]==plateau[1][1] and plateau[2][0]=='X'):
        if(plateau[0][2]=='.'):
             cpt+=J
    if(plateau[0][2]==plateau[2][0] and plateau[1][1]=='X'):
        if(plateau[0][2]=='.'):
             cpt+=J
    if(plateau[2][0]==plateau[1][1] and plateau[0][2]=='X'):
        if(plateau[2][0]=='.'):
             cpt+=J  
    
# mode IA       
# verif ligne 1/3  
    for i in range(3):
        if(plateau[i][0]==plateau[i][1] and plateau[i][2]=='O'):
            if(plateau[i][0]=='.'):
                cpt+=IA
    for i in range(3):
        if(plateau[i][0]==plateau[i][2] and plateau[i][1]=='O'):
                cpt+=IA
    for i in range(3):
        if(plateau[i][2]==plateau[i][1] and plateau[i][0]=='O'):
                cpt+=IA        
    #verif colonne 1/3
    for i in range(3):
        if(plateau[0][i]==plateau[1][i] and plateau[2][i]=='O'):
            if(plateau[0][i]=='.'):
                cpt+=IA
    for i in range(3):
        if(plateau[0][i]==plateau[2][i] and plateau[1][i]=='O'):
            if(plateau[0][i]=='.'):
                cpt+=IA
    for i in range(3):
        if(plateau[2][i]==plateau[1][i] and plateau[0][i]=='O'):
            if(plateau[2][i]=='.'):
                cpt+=IA
    #verif diagonal 1/3
    if(plateau[0][0]==plateau[1][1] and plateau[2][2]=='O'):
        if(plateau[0][0]=='.'):
             cpt+=IA
    if(plateau[0][0]==plateau[2][2] and plateau[1][1]=='O'):
        if(plateau[0][0]=='.'):
             cpt+=IA
    if(plateau[2][2]==plateau[1][1] and plateau[0][0]=='O'):
        if(plateau[2][2]=='.'):
             cpt+=IA
    if(plateau[0][2]==plateau[1][1] and plateau[2][0]=='O'):
        if(plateau[0][2]=='.'):
             cpt+=IA
    if(plateau[0][2]==plateau[2][0] and plateau[1][1]=='O'):
        if(plateau[0][2]=='.'):
             cpt+=IA
    if(plateau[2][0]==plateau[1][1] and plateau[0][2]=='O'):
        if(plateau[2][0]=='.'):
             cpt+=IA
    return cpt

def copier(M):
    copy=[[".",".","."],
       [".",".","."],
       [".",".","."],]
    for i in range(3):
        for j in range(3):
            copy[i][j]=M[i][j]
    return copy


def minimax_decision(state):
    act=[0,0]
    L=[]
    for i in action(state):
        copy=copier(state)
        act.append(i)
        #L.append(min_value(realise(copy,i)))
        L.append(utility(realise(copy,i))) # mieux que minmax, il trouve l'utility la plus grande de l'étape suivante
    A=max(L)# argmax
    pos=action(state)
    for j in range(len(L)):
        if(L[j]==A):
            act=pos[j]
    return act
    

def min_value(state):
    if(Terminal_test(state)):
        return utility(state)
    v=1000000
    for a in action(state):
        v=min(v,max_value(realiseJoueur(state,a)))# joueur
    return v


def max_value(state):
    if(Terminal_test(state)):
        return utility(state)
    v=-1000000
    for a in action(state):
        v=max(v,min_value(realise(state,a)))# IA
    return v



def alpha_beta_search(state):
    # code proposer au TD
    """
    act=[0,0]
    alpha=-100000
    beta=100000
    v=Max_valueAB(state,alpha,beta)# return 5000 à chaque fois
    for i in action(state):
        if(Max_valueAB(copier(state),alpha,beta)==v):
            act=i # il n'a pas pris l'action
    return act 
    """
    # autre méthode
    L=[]
    act=[]
    alpha=-100000
    beta=100000
    #vmax=Max_valueAB(copier(state),alpha,beta)
    #print(vmax) # affiche que 5000
    for i in action(state):
        L.append(Min_valueAB(realise(copier(state),i),alpha,beta))
        act.append(i)
        #if(vmax==vM):
         #   act=i
    for j in range(len(L)):
        if(max(L)==L[j]):
            return act[j]

        


def Max_valueAB(state,alpha,beta):
    if(Terminal_test(state)):
        return utility(state)
    v=-100000
    for i in action(state):
        v=max(v,Min_valueAB(realise(state,i),alpha,beta))
        if v>=beta:
            return v
        alpha=max(alpha,v)
    return v

def Min_valueAB(state,alpha,beta):
    if(Terminal_test(state)):
        return utility(state)
    v=100000
    for i in action(state):
        v=min(v,Max_valueAB(realiseJoueur(state,i),alpha,beta))
        if v<=alpha:
            return v
        beta=min(beta,v)
    return v


def joueur(plateau):
    print(" à ton tour")
    n=-1  # chiffre
    L=action(plateau)
    print("choisir action")
    for i in range(len(L)):
        print(i,")",L[i]) 
    while (n<0 or n>len(L)-1):
        n=eval(input("choisir chiffre\n"))
    realiseJoueur(plateau,L[n])
    return None

def joueurAutre(plateau):
    print(" à joueur autre")
    n=-1  # chiffre
    L=action(plateau)
    print("choisir action")
    for i in range(len(L)):
        print(i,")",L[i]) 
    while (n<0 or n>len(L)-1):
        n=eval(input("choisir chiffre\n"))
    realise(plateau,L[n])
    return None


def MorpionIA():
    #initialisation
    M=[[".",".","."],
       [".",".","."],
       [".",".","."],]
    print("Morpion joueur vs IA")
    print("joueur: X  et IA: O")
    affichage(M)
    # position
    R=rd.randint(1,2)
    if(R==1):
        while(Terminal_test(M)==False):
            joueur(M)
            affichage(M) # affichage fin joueur
            if(Terminal_test(M)):
                print("victoire joueur");break
            print("au tour de l'IA")
            capteur(M)                         # donne les valeurs de chaque zone
            ActionIA=minimax_decision(copier(M))
            realise(M,ActionIA)
            affichage(M) # affichage fin IA
            if(Terminal_test(M)):
                print("victoire IA");break
    else:
        while(Terminal_test(M)==False):
            print("au tour de l'IA")
            capteur(M)
            ActionIA=minimax_decision(copier(M))
            realise(M,ActionIA)
            affichage(M)
            if(Terminal_test(M)):
                print("victoire IA");break
            joueur(M)
            affichage(M)
            if(Terminal_test(M)):
                print("victoire joueur");break
    print("egalité ??")
    return None

def MorpionIA_alphabeta():
    #initialisation
    M=[[".",".","."],
       [".",".","."],
       [".",".","."],]
    print("Morpion joueur vs IA")
    print("joueur: X  et IA: O")
    affichage(M)
    # position
    R=rd.randint(1,2)
    if(R==1):
        while(Terminal_test(M)==False):
            joueur(M)
            affichage(M) # affichage fin joueur
            if(Terminal_test(M)):
                print("victoire joueur");break
            print("au tour de l'IA")
            ActionIA=alpha_beta_search(copier(M))
            realise(M,ActionIA)
            affichage(M) # affichage fin IA
            if(Terminal_test(M)):
                print("victoire IA");break
    else:
        while(Terminal_test(M)==False):
            print("au tour de l'IA")
            ActionIA=alpha_beta_search(copier(M))
            realise(M,ActionIA)
            affichage(M)
            if(Terminal_test(M)):
                print("victoire IA");break
            joueur(M)
            affichage(M)
            if(Terminal_test(M)):
                print("victoire joueur");break
    print("egalité ??")
    return None

def MorpionJoueur():
    #initialisation
    M=[[".",".","."],
       [".",".","."],
       [".",".","."],]
    print("Morpion joueur vs joueur autre")
    print("joueur: X  et joueurAutre: O")
    affichage(M)
    # position
    R=rd.randint(1,2)
    if(R==1):
        while(Terminal_test(M)==False):

            joueur(M)
            affichage(M) # affichage fin joueur
            if(Terminal_test(M)):
                print("victoire joueur");break
            joueurAutre(M)
            affichage(M) # affichage fin IA
            if(Terminal_test(M)):
                print("victoire joueurAutre");break
    else:
        while(Terminal_test(M)==False):
            joueurAutre(M)
            affichage(M)
            if(Terminal_test(M)):
                print("victoire joueurAutre");break
            joueur(M)
            affichage(M)
            if(Terminal_test(M)):
                print("victoire joueur");break
    print("egalité ??")
    return None

def aleatoire(plateau):
    print("au tour de l'IA")
    L=action(plateau)
    n=rd.randint(0,len(L)-1)
    realise(plateau,L[n])
    return None

def MorpionRandom():
    #initialisation
    M=[[".",".","."],
       [".",".","."],
       [".",".","."],]
    print("Morpion joueur vs random")
    print("joueur: X  et random: O")
    affichage(M)
    # position
    R=rd.randint(1,2)
    if(R==1):
        while(Terminal_test(M)==False):
            joueur(M)
            affichage(M) # affichage fin joueur
            if(Terminal_test(M)):
                print("victoire joueur");break
            aleatoire(M)
            affichage(M) # affichage fin IA
            if(Terminal_test(M)):
                print("victoire Random");break
    else:
        while(Terminal_test(M)==False):
            aleatoire(M)
            affichage(M)
            if(Terminal_test(M)):
                print("victoire Random");break
            joueur(M)
            affichage(M)
            if(Terminal_test(M)):
                print("victoire joueur");break
    print("egalité ??")
    return None

def capteur(M):
    P=[[0,0,0],[0,0,0],[0,0,0],]
    for i in range(3):
        for j in range(3):
            copy=copier(M)
            if(M[i][j]=='.'):
                P[i][j]=utility(realise(copy,[i,j]))
    print(P)


if __name__== "__main__":
    print('le MorpionIA marche très bien avec utility\nle alpha_beta est moins intelligent que le minimax\n')
    print("Morpion Choix:")
    print("1) vs IA\n2) vs Alpha_beta\n3) vs joueur \n4) vs random")
    k=0
    while(k not in [1,2,3,4]):
        k=eval(input("\nchoix mode\n"))
    if(k==1):
        MorpionIA()
    if(k==2):
        MorpionIA_alphabeta()
    if(k==3):
        MorpionJoueur()
    if(k==4):
        MorpionRandom()


    
    

    
    
    
    
    
    
    
    
    
    
    
        
    
    