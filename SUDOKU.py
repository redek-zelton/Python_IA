
from ortools.sat.python import cp_model
import random as rd


def matrice(n):
    matrix = []
    for i in range(n):
        line = []
        for j in range(n):
            line.append(0)
        matrix.append(line)
    return matrix
# Sudoku random à completer à la main
rand=[[4,0,6,3,8,0,0,2,0],
      [5,0,3,7,0,4,0,0,0],
      [0,0,0,9,0,0,8,4,3],
      [2,3,0,0,1,0,9,0,0],
      [0,4,0,0,0,0,5,7,1],
      [0,5,0,6,4,7,0,0,0],
      [9,0,1,4,0,8,3,0,0],
      [0,6,4,0,0,0,0,0,7],
      [8,0,5,1,0,3,0,9,2]]

# la matrice d'erreur en cas de non résolution
erreur=[[1,1,1,1,1,1,1,1,1],
      [1,2,2,2,2,2,2,2,1],
      [1,2,3,3,3,3,3,2,1],
      [1,2,3,4,4,4,3,2,1],
      [1,2,3,4,5,4,3,2,1],
      [1,2,3,4,4,4,3,2,1],
      [1,2,3,3,3,3,3,2,1],
      [1,2,2,2,2,2,2,2,1],
      [1,1,1,1,1,1,1,1,1]]

# ot tools sudoku
def Sudoku9x9():
    model = cp_model.CpModel()
    Solution=matrice(9)
    for i in range(0,9):
        for j in range(9):
            Solution[i][j]=model.NewIntVar(1,9,"Soluce"+str(i)+str(j))
            
    # affectation
    for x in range(9):
        for y in range(9):
            if rand[x][y]!=0:
                model.Add(Solution[x][y] == rand[x][y])
                
    # verif ligne et colonne
    for i in range(9):
        model.AddAllDifferent([Solution[i][j] for j in range(9)])
        model.AddAllDifferent([Solution[j][i] for j in range(9)])
    

    # vérif cellule
    for i in range(3):
        for j in range(3):
            case=[]
            for k in range(3):
                for d in range(3):
                    case.append(Solution[i*3+k][j*3+d])
            model.AddAllDifferent(case)
            
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    if status == cp_model.FEASIBLE:
        
        for i in range(9):
           print([int(solver.Value(Solution[i][j])) for j in range(9)])
        print("EST SOLUTION")
        S=matrice(9)
        for i in range(9):
            for j in range(9):
                S[i][j]=int(solver.Value(Solution[i][j]))
        return S 
    else: 
        print("failed: can not be resolved")
        return erreur


# Cache les réponses
def G(tot):
    Solution=Sudoku9x9()
    Cache=Solution
    cpt=0
    while(cpt<(81-tot)):
        i=rd.randint(0,8)
        j=rd.randint(0,8)
        if(Cache[i][j]!=0):
            Cache[i][j]=0
            cpt+=1
    return Cache

# modèle affichage classique
def modele(grille):
    for i in range(9):
       print([grille[i][j] for j in range(9)])
            
                     
# le menu
def menu():
    N=[1,2,3,4,5]
    L=[0,50,40,33,26,17]
    print("Choisir la dificulté")
    print("------------------------------------------")
    print(" 1) débutant (50 cases données)")
    print(" 2) facile (40 cases données)")
    print(" 3) moyen (33 cases données)")
    print(" 4) difficile (26 cases données")
    print(" 5) très difficile(17 cases données)")
    print("-------------------------------------------")
    n=0
    while(n not in N):
        n=eval(input("choisir chiffre 1 à 5\n"))
    print("--------------------------------------------")
    print("nombre de valeurs données : ",L[n])
    Cache=G(L[n])
    modele(Cache)
    print("A COMPLETER")
    return None
    

if __name__== "__main__":
    print("SUDOKU 9X9 Chi Antoine Groupe B\n")
    menu()

