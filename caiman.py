# -*- coding: utf-8 -*-

import random
random.seed()

#donnee utile pour les tests

grille = [["J","N","J","R","R","J","J","J"],
          ["J","R"," ","J","N","J","J","N"],
          ["R","J","R","R","J","J","N","J"],
          ["N","J","J","N","J","N","J","R"],
          ["J","R","R","J","R"," ","R","J"],
          ["N","J","J","R","N","J","J","R"],
          ["J","R","J","R","J","R","J","R"],
          ["R","R","J","J","N","J","R","J"],]

tresor = [0,0,0,0,0,0]


############Code atelier 2#############################
#######################################################


def afficher_grille(grille,joueur,tresor): #affiche la grille et les informations de partie
    
    """Affiche la grille et les informations de partie
    grille --> liste de liste de chaine de caractere
    joueur --> un entier (1 ou 2) indiquant le tour du joueur
    tresor --> une liste de 6 entiers indiquant respectivement les pions du joueur 1 et du joueur 2 """
    
    print("     -------------------------------")
    print("    | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
    print("|---|---|---|---|---|---|---|---|---|")

    ligne = ["A","B","C","D","E","F","G","H"]
    for i in range(8):#pour afficher les 8 lignes de la grille
        print("|",ligne[i],"|",end="")
        for elem in grille[i]:
            print("",elem,"|",end="")
        print("\n|---|   |   |   |   |   |   |   |   |")

    print("\nJoueur 1 J:",tresor[0],"R:",tresor[1],"N:",tresor[2])
    print("Joueur 2 J:",tresor[3],"R:",tresor[4],"N:",tresor[5],"\n")
   

############################## Configurations #####################################
def config_debut(grille,tresor): #configuration debut de partie
    grille[::] = [["J","N","J","R","R","J","J","J"],
              ["J","R"," ","J","N","J","J","N"],
              ["R","J","R","R","J","J","N","J"],
              ["N","J","J","N","J","N","J","R"],
              ["J","R","R","J","R"," ","R","J"],
              ["N","J","J","R","N","J","J","R"],
              ["J","R","J","R","J","R","J","R"],
              ["R","R","J","J","N","J","R","J"]]

    joueur = 1

    tresor[::] = [0,0,0,0,0,0]

    return joueur,grille,tresor


def config_centre(grille,tresor): #configuration en cours de partie
    grille[::] = [[" ","N","J","R","R","J","J","J"],
              [" "," "," "," "," "," ","J","N"],
              ["R"," "," ","J"," "," "," "," "],
              ["N","J"," "," "," "," ","J","R"],
              ["J","R","R"," "," "," ","R","J"],
              ["N","J"," ","R","N","J","J","R"],
              ["J","R","J","R","J","R","J","R"],
              ["R","R","J","J","N","J","R","J"]]

    joueur = 1

    tresor[::] = [6,3,3,5,1,1]

    return joueur,grille,tresor


def config_fin(grille,tresor): #configuration fin de partie
    grille[::] = [[" ","N"," ","R","R","J"," ","J"],
              [" "," "," "," "," "," "," ","N"],
              ["R"," "," "," "," "," "," "," "],
              ["N","J","J"," "," "," "," ","R"],
              [" ","R"," ","J"," "," "," "," "],
              ["N","J"," "," "," "," ","J","R"],
              [" "," "," "," "," "," "," ","R"],
              ["R","R"," "," ","N"," ","R"," "]]

    joueur = 1

    tresor[::] = [11,5,3,14,5,2]

    return joueur,grille,tresor


########### Fonctions Unitaires imposees ###################################
def test_est_au_bon_format():
    assert est_au_bon_format("A1"),"A1 doit etre condideree comme au bon format"
    assert est_au_bon_format("Z9"),"Z9 doit etre condideree comme au bon format"
    assert not(est_au_bon_format("AB")),"AB n'est pas un format correct"
    assert not(est_au_bon_format("41")),"41 n'est pas un format correct"
    assert not(est_au_bon_format("")),"'' est trop petit"
    assert est_au_bon_format("A12"),"A12 est doit etre condideree comme au bon format"
    assert not(est_au_bon_format("a1")),"la lettre doit etre en majuscule"
    assert not(est_au_bon_format("@A12!")),"Ce message doit etre invalide"
    assert not(est_au_bon_format("A12@!")),"Ce message doit etre invalide"

def test_est_dans_grille(grille):
    assert est_dans_grille("C",4,grille), "erreur sur le cas de base"
    assert est_dans_grille("H",8,grille), "erreur sur une coordonnee extreme (H8)"
    assert est_dans_grille("A",1,grille), "erreur sur  (A1)"
    assert not(est_dans_grille("A",0,grille)), "erreur sur une coordonnee sortie de la grille d'une seule case (A0)"
    assert not(est_dans_grille("I",1,grille)), "erreur sur une coordonnee sortie de la grille d'une seule case (I1)"
    assert not(est_dans_grille("K",33,grille)), "erreur sur une coordonnee fausse"

def est_un_nombre(nombre):
    """verifie si message est bien un nombre en passant par sa valeur ascii
       nombre -> chaine de caractere"""
    i = 0
    est_nombre = True
    
    while est_nombre and i != len(nombre): 
        chiffre = ord(nombre[i])
        if chiffre < 48 or chiffre > 57:
            est_nombre = False

        i += 1

    return est_nombre

def est_lettre_maj(lettre):
    """verifie si la lettre est une lettre en majuscule compris entre A et Z
       lettre -> chaine de caractere"""
    lettre = ord(lettre)
    if lettre < 65 or lettre > 90: 
        return False
    else:
        return True
    
def est_au_bon_format(message):
    """Renvoie True si le message est au bon format et False dans le cas contraire
       message -> chaine de caractere"""
    if len(message) < 2: #le message ne peut etre plus grand qu'une lettre est un chiffre
        return False

    #verifie si on a bien dans message une lettre suivi d'un nombre
    return est_lettre_maj(message[0]) and est_un_nombre(message[1::])

    
    

    

def est_dans_grille(ligne,colonne,grille):
    """Renvoie True si les coordonnees sont dans la grille est False dans le cas contraire
        ligne -> chaine de caractere
        colonne -> entier
        grille -> liste de liste de chaine de caractere"""
    #comme A est dans la table ascii egal a 65 il suffit de retirer a la lettre majuscule en ascii 65 pour obtenir l'indice de la ligne
    ligne = ord(ligne) - 65

    nb_ligne = len(grille)
    nb_colonne = len(grille[0])

    if ligne < 0 or ligne > 7:
        return False
    elif colonne-1 < 0 or colonne-1 > 7:
        return False
    else:
        return True


def saisir_coordonnees(grille):
    """demande une saisie des coordonnees jusqu'a qu'elle sois juste
       grille -> liste de liste de chaine de caractere"""
    coor = ""
    est_grille = False
    print("Celle ci doit être une lettre entre A et H suivi d'un chiffre en 1 et 8")
        
    while not(est_au_bon_format(coor)) or not(est_grille):
        coor = input(":")
        if est_au_bon_format(coor):
            lettre = coor[0]
            nombre = int(coor[1::])
            est_grille = est_dans_grille(lettre,nombre,grille)
            if not(est_grille):
                print("Vos coordonnees sorte de la grille")
        else:
            print("vos coordonnees sont au mauvais format")
    return coor

#######################################################
##############Code atelier 3###########################
def convert_coordonnee(coor):
    """convertie les coordonnees composer d'une lettre et d'un chiffre en tuple de coordonnee
       coor -> chaine de caracteres"""
    return (ord(coor[0])-65,int(coor[1])-1)
    
def verif_distance(depart,fin):
    """verifie si la distance entre la case de depart et de fin est correcte et renvoie True si oui sinon False
       depart -> coordonne de depart du joueur sous forme d'un tuple de deux nombres
       fin -> coordonne de fin du joueur sous forme d'un tuple de deux nombres"""

    x = depart[0] - fin[0]
    y = depart[1] - fin[1]
    # on soustrait les coordonnees entre elle
    # si on obtient -2 ou 2 on se deplace de 2 sur l'axe correspondant
    # si on obtient 0 on ne se deplace pas sur l'axe correspondant

    if x == 0 and y == 0: #le joueur ne se deplace pas
        return False
    elif (x==2 or x==-2 or x==0) and (y==2 or y==-2 or y==0):
        return True
    else :
        return False
def case_intermediaire(depart,fin):
    """renvoie les coordonnees de la case survole par le pion
       depart -> coordonne de depart du joueur sous forme d'un tuple de deux nombres
       fin -> coordonne de fin du joueur sous forme d'un tuple de deux nombres"""
    x = depart[0] - fin[0]
    y = depart[1] - fin[1]
    if x != 0:
        x *= 1/2
    if y != 0:
        y *= 1/2
    return(depart[0]-int(x),depart[1]-int(y))
    
def mettre_a_jour_tresor(tresor,joueur,pion):
    """met a jour le tresor des joueurs
       tresor -> liste de 6 int
       joueur -> int
       pion -> 'J' ou 'R' ou 'N'"""
    rang = 3
    if joueur == 1:
        rang = 0
    if pion == "J":
        tresor[rang] += 1
    elif pion == "R":
        tresor[rang+1] += 1
    else:
        tresor[rang+2] += 1
def deplacement_possible(grille,depart):
    """verifie si il y a un deplacement possible par rapport au depart
       grille -> liste de liste de chaine de caractere
       depart -> coordonne de depart du joueur sous forme d'un tuple de deux nombres"""

    possible = False
    for i in [-2,0,2]:
        for j in [-2,0,2]:
            if not(i==0 and j==0): #on ne verifie pas la case de depart
                if depart[0] + i >= 0 and depart[0] + i <= 7: #verifie que les coordonnees de sorte pas de la grille
                    if depart[1] + j >= 0 and depart[1] + j <= 7:
                        if grille[depart[0] + i][depart[1] + j] == " ":
                            if grille[depart[0] + int(1/2*i)][depart[1] + int(1/2*j)] != " ":
                                possible = True
    return possible
                                
                            
    
    
def deplacer(grille,depart,fin,tresor,joueur):
    """effectue le deplacement du pion du joueur et l'ajout de point
       grille -> liste de liste de chaine de caractere
       depart -> coordonne de depart du joueur sous forme d'un tuple de deux nombres
       fin -> coordonne de fin du joueur sous forme d'un tuple de deux nombres"""
    if verif_distance(depart,fin):
        if grille[depart[0]][depart[1]] == "J" and grille[fin[0]][fin[1]] == " ":
            x,y = case_intermediaire(depart,fin)
            val = grille[x][y]
            if val != " ":
                grille[depart[0]][depart[1]], grille[fin[0]][fin[1]] = " ","J"
                grille[x][y] = " "
                mettre_a_jour_tresor(tresor,joueur,val)
                return True
    return False
    

def saisir_deplacement_fin(grille,tresor,joueur,depart): ### a completer
    """effectue la saisie des coordonnees d'arrivee et l'execution d'un deplacement
       grille -> liste de liste de chaine de caractere
       tresor -> liste de 6 int
       joueur -> int
       depart -> coordonne de depart du joueur sous forme d'un tuple de deux nombres"""

    print("Entrez les coordonnees du pion d'arrivee:")
    fin = convert_coordonnee(saisir_coordonnees(grille))
    while not(deplacer(grille,depart,fin,tresor,joueur)):
        print("deplacement impossible, veuillez ressaisir vos coordonnees")
        fin = convert_coordonnee(saisir_coordonnees(grille))
    else:
        return fin

def saisir_deplacement_debut(grille,tresor,joueur):
    """effectue la saisie des premieres coordonnees
       grille -> liste de liste de chaine de caractere
       tresor -> liste de 6 int
       joueur -> int""" 
    print("\n\nEntrez les coordonnees du pion jaune d'ou vous souhaiter partir:")
    depart = convert_coordonnee(saisir_coordonnees(grille))
    while not(deplacement_possible(grille,depart)) or grille[depart[0]][depart[1]] != "J":
        print("Il n'y a aucun mouvement possible, veuillez ressaisir vos coordonnees: ")
        depart = convert_coordonnee(saisir_coordonnees(grille))
    return depart
    

def fin_partie(grille):
    """verifie si il y a encore des deplacements possibles dans la grille
       grille -> liste de liste de chaine de caractere"""

    taille = len(grille)
    fin = True
    for i in range(taille):
        for j in range(taille):
            if grille[i][j] == "J":
                if deplacement_possible(grille,(i,j)):
                    fin = False
    return fin

def tour_joueur(grille,tresor,joueur):
    """effectue le tour d'un joueur
       grille -> liste de liste de chaine de caractere
       tresor -> liste de 6 int
       joueur -> int"""

    afficher_grille(grille,joueur,tresor)
    print("C'est au tour du joueur",str(joueur)+"!\n")

    abandon = "0"
    while abandon!="1" and abandon!="2":
        abandon = input("1)Lancer le tour\n2)abandonner\n: ")
    if abandon == "2":
        return False
    
    
    depart = saisir_deplacement_debut(grille,tresor,joueur)
    fin = saisir_deplacement_fin(grille,tresor,joueur,depart)
    tour_fini = False
    
    while deplacement_possible(grille,fin) and not(tour_fini):
        
        afficher_grille(grille,joueur,tresor)
        print("Voulez vous enchainer:\n1) Oui\n2) Non\n")
        enchainer = input(": ")
        if enchainer == "1":
            fin = saisir_deplacement_fin(grille,tresor,joueur,fin)
            
        elif enchainer == "2":
            tour_fini = True
        else:
            print("Je n'ai pas compris votre reponse!")
    print("Le tour du joueur",joueur,"est fini!")
    return True


        
def test_atelier_3(grille):
    grille2 = [[" ","N"," ","R","R","J"," "," "],
               [" "," "," "," "," "," "," ","N"],
               ["R"," "," "," "," "," "," "," "],
               ["N"," "," "," "," "," "," ","R"],
               [" ","R"," ","J"," "," "," "," "],
               ["N"," "," "," "," "," ","J","R"],
               [" "," "," "," "," "," "," ","R"],
               ["R","R"," "," ","N"," ","R"," "]]
    
    print("verification de la distance entre une coordonnee de depart et de fin:")
    assert not(verif_distance((2,4),(2,8))), "deplacement invalide"
    assert verif_distance((2,4),(4,4)), "deplacement cas valide simple"
    assert verif_distance((2,4),(4,6)), "deplacement cas valide diagonale"
    assert verif_distance((2,4),(2,2)), "deplacement cas valide simple"
    assert not(verif_distance((1,1),(1,1))), "aucun deplacement"
    print("test fini\n")
    print("calcul des coordonnes d'une case entre la case de depart et de fin:")
    assert case_intermediaire((2,4),(4,4)) == (3,4), "mauvais calcul pour la case entre les coordonnes (2,4) et (4,4)"
    assert case_intermediaire((2,4),(4,6)) == (3,5), "mauvais calcul pour la case entre les coordonnes (2,4) et (4,6)"
    assert case_intermediaire((2,4),(2,2)) == (2,3), "mauvais calcul pour la case entre les coordonnes (2,4) et (2,2)"
    print("test fini\n")
    print("calcul de la conversion de coordonnees: ")
    assert convert_coordonnee("A1") == (0,0), "Mauvaise conversion de A1"
    assert convert_coordonnee("H8") == (7,7), "Mauvaise conversion de H8"
    assert convert_coordonnee("E4") == (4,3), "Mauvaise conversion de E4"
    print("test fini\n")
    print("verification de la possibilitee d'un deplacement vis a vis d'une case: ")
    assert deplacement_possible(grille,(3,2)), "Le deplacement est possible ici"
    assert not(deplacement_possible(grille,(4,0))), "Le deplacement est impossible ici"
    print("test fini\n")
    print("Verification de fin de partie: ")
    assert not(fin_partie(grille)), "On peut encore jouer des coups sur la grille"
    assert fin_partie(grille2), "On ne peut plus jouer de coup sur la grille"
    print("test fini\n")
    print("Tout les tests de l'atelier 3 ont été passé\n\n")
    
    
#######################################################
##############Code atelier 4###########################

def coordonnee_arrive(grille,depart):
    """renvoie les deplacements possibles depuis un depart
       grille -> liste de liste de chaine de caractere
       depart -> coordonne de depart du joueur sous forme d'un tuple de deux nombres"""
    arriver = []
    for i in [-2,0,2]:
        fin_i = depart[0] + i
        if fin_i >= 0 and fin_i <= 7:
            for j in [-2,0,2]:
                if not(i==0 and j==0):
                    fin_j = depart[1] + j
                    if fin_j >= 0 and fin_j <= 7:
                        if grille[fin_i][fin_j] == " ":
                            if grille[depart[0] + int(1/2*i)][depart[1] + int(1/2*j)] != " ":
                                arriver.append((fin_i,fin_j))
    return arriver

def lister_coup(grille):
    """Liste tout les coups possibles dans la grille et en renvoie la liste
       grille -> liste de liste de chaine de caractere"""
    depart = []
    arriver = []
    taille_grille = len(grille)
    for i in range(taille_grille):
        for j in range(taille_grille):
            if grille[i][j] == "J" and deplacement_possible(grille,(i,j)):
                depart.append((i,j))
                arriver.append(coordonnee_arrive(grille,(i,j)))
    return depart,arriver

def calcul_score(grille,tresor,dernier_joueur):
    """Calcul le score des joueurs
       grille -> liste de liste de chaine de caractere
       tresor -> liste de 6 int
       dernier_joueur -> int"""
    
    #calcul des points restants sur la grille    
    score_grille = 0
    taille_grille = len(grille)
    for i in range(taille_grille):
        for j in range(taille_grille):
            if grille[i][j] == "J":
                score_grille += 1
            elif grille[i][j] == "R":
                score_grille += 2
            elif grille[i][j] == "N":
                score_grille += 3

    ###

    score1 = tresor[0] + 2*tresor[1] + 3*tresor[2]
    score2 = tresor[3] + 2*tresor[4] + 3*tresor[5]

    if dernier_joueur == 1:
        score1 -= score_grille
    else:
        score2 -= score_grille



    return score1, score2
def lancer_partie(joueur,grille,tresor,mode):
    """Lance une partie contre l'IA (et choix du niveau de difficulte) ou a deux joueur en fonction du mode
       grille -> liste de liste de chaine de caractere
       tresor -> liste de 6 int
       joueur -> int
       mode -> chaine de caractere '1' ou '2'"""
    
    if mode == "1":
        partie_2_joueur(joueur,grille,tresor)
    else:
        reponse = "0"

        while reponse != "1" and reponse != "2":
            print("\nChoisissez le niveau de votre adversaire: \n1)Facile\n2)Difficile")
            reponse = input(": ")
        partie_1_joueur(joueur,grille,tresor,int(reponse))
    
def tour_IA(grille,tresor):
    """Joue le tour de l'IA
       grille -> liste de liste de chaine de caractere
       tresor -> liste de 6 int"""

    print("\nC'est au tour de l'IA de jouer\nElle a jouer les coups:\n")
    depart,arriver = lister_coup(grille)
    i_coor_dep = random.randint(0,len(depart)-1)
    dep = depart[i_coor_dep]
    fin = arriver[i_coor_dep][random.randint(0,len(arriver[i_coor_dep])-1)]
    fin_tour = 0
    
    while fin_tour == 0:
        print(chr(dep[0]+65)+str(dep[1]+1),"-->",chr(fin[0]+65)+str(fin[1]+1),"\n")
        deplacer(grille,dep,fin,tresor,2)
        dep = fin
        if deplacement_possible(grille,dep) and random.randint(0,3) != 0:
            fin = coordonnee_arrive(grille,dep)
            fin = fin[random.randint(0,len(fin)-1)]
        else:
            fin_tour = 1
            
    
    
def partie_1_joueur(joueur,grille,tresor,niv_IA=2):
    """Enchaine les tours IA / Joueur et annonce le gagnant
       grille -> liste de liste de chaine de caractere
       tresor -> liste de 6 int
       joueur -> int"""
    abandon = True
    while not fin_partie(grille) and abandon:
        if joueur == 1: #tour du joueur
            abandon = tour_joueur(grille,tresor,joueur)
            afficher_grille(grille,joueur,tresor)
            joueur = 2
        else:
            if niv_IA == 1:
                tour_IA(grille,tresor)
            else:
                tour_IA_avancer(grille,tresor)
            joueur = 1

    if abandon:
        dernier_joueur = 1
        if joueur == 1:
            dernier_joueur = 2
            
        afficher_grille(grille,joueur,tresor)
        print("\n\nIl n'y a plus aucun coup possible, la partie est fini!\n\n")

        score1, score2 = calcul_score(grille,tresor,dernier_joueur)
        if score1 > score2:
            print("Le Joueur à gagné!")
        else:
            print("L'IA à gagnée!")
        print("\nscore du Joueur:",score1,",  score de l'IA",score2)
    else:
        print("\nLe joueur a abandonné")
            
    
def partie_2_joueur(joueur,grille,tresor):
    """Enchaine les tours de joueurs et annonce le gagnant
       grille -> liste de liste de chaine de caractere
       tresor -> liste de 6 int
       joueur -> int"""
    abandon = True
    while not fin_partie(grille) and abandon:


        abandon = tour_joueur(grille,tresor,joueur)
       
        if joueur == 1:
            joueur = 2
        else:
            joueur = 1


    dernier_joueur = 1
    if joueur == 1:
        dernier_joueur = 2
            
    if abandon:
        afficher_grille(grille,joueur,tresor)
        print("\n\nIl n'y a plus aucun coup possible, la partie est fini!\n\n")

        score1, score2 = calcul_score(grille,tresor,dernier_joueur)
        if score1 > score2:
            print("Le joueur 1 à gagné!")
        else:
            print("Le joueur 2 à gagné!")
        print("\nscore du joueur 1:",score1,",  score du joueur 2:",score2)
    else:
        print("\nLe joueur",dernier_joueur,"a abandonné")            
            
        
def test_atelier_4(grille,tresor):
    joueur,grille,tresor = config_fin(grille,tresor)

    grille_fini = [["J"," "," ","R","R"," "," ","J"],
                   [" "," "," "," "," "," "," "," "],
                   ["R"," "," "," "," "," "," ","J"],
                   ["N"," "," "," "," "," "," "," "],
                   [" "," "," "," "," ","J"," "," "],
                   [" "," ","J"," "," "," "," ","R"],
                   ["J"," "," "," "," "," "," ","R"],
                   ["R","R"," ","J","N","J","R","J"]]
    tresor_fin = [12,5,7,11,7,1]

    print("Test Calcul de score:")
    assert calcul_score(grille_fini,tresor_fin,2) == (43,-3),"Mauvais calcul de score"
    assert calcul_score(grille_fini,tresor_fin,1) == (12,28),"Mauvais calcul de score"
    print("test fini\n")
    print("Verification de tout les coup possible dans une grille:")
    assert lister_coup(grille_fini) == ([],[]), "Il n'y a pas de coup possible dans ce test"
    assert lister_coup(grille) == ([(0,7),(3,1),(3,2),(4,3)],[[(2,7)],[(3,3)],[(5,4)],[(2,1)]]), 'Il y a 4 coups possible dans cette grille'
    print("test fini\n")
    print("Verification des cases d'arrivée possible")
    assert coordonnee_arrive(grille,(0,7)) == [(2,7)], "Il y a un deplacement possible"
    assert coordonnee_arrive(grille,(4,3)) == [(2,1)], "Il y a un deplacement possible"
    print("test fini\n")
    
    print("Tout les tests de l'atelier 4 ont été passé\n\n")
    
def menu(grille,tresor):
    """lance le menu de depart pour configurer la partie
       grille -> liste de liste de chaine de caractere
       tresor -> liste de 6 int"""
    
    reponse = "0"
    fin = False

    while not(fin):
        reponse = "0"
        
        while reponse != "1" and reponse != "2" and reponse != "3":
            reponse = input("\nQue voulez vous faire?\n1)Jouer au Caiman\n2)Lancer les tests\n3)Quitter\n: ")

        if reponse == "1":
            mode = "0"
            while mode != "1" and mode != "2":
                mode = input("\nContre qui allez vous jouer?\n1)Nous sommes deux!\n2)Je suis seul ;-;\n: ")

            reponse = "0"
            while reponse != "1" and reponse != "2" and reponse != "3":
                reponse = input("\nChoisissez la configuration\n1)debut de partie\n2)milieu de partie\n3)fin de partie\n: ")
            if reponse == "1":
                joueur, grille, tresor = config_debut(grille,tresor)
            elif reponse == "2":
                joueur, grille, tresor = config_centre(grille,tresor)
            else:
                joueur, grille, tresor = config_fin(grille,tresor)

            lancer_partie(joueur,grille,tresor,mode)
            
            

        elif reponse == "2":
            print("\n")
            config_debut(grille,tresor)
            test_atelier_3(grille)
            test_atelier_4(grille,tresor)
            test_atelier_5(grille,tresor)

        else:
            fin = True

        print("\n\n")



#######################################################
##############Code atelier 5###########################

def tour_IA_avancer(grille,tresor):
    """Joue le tour de l'IA avancee
       grille -> liste de liste de chaine de caractere
       tresor -> liste de 6 int"""

    print("\nC'est au tour de l'IA de jouer\nElle a jouer les coups:\n")

    chemin = max_point(grille)
    taille = len(chemin)
    for i in range(0,len(chemin)-2):
        print(chr(chemin[i][0]+65)+str(chemin[i][1]+1),"-->",chr(chemin[i+1][0]+65)+str(chemin[i+1][1]+1),"\n")
        deplacer(grille,chemin[i],chemin[i+1],tresor,2)
    if len(chemin) <= 2:
        i = 0
        print(chr(chemin[i][0]+65)+str(chemin[i][1]+1),"-->",chr(chemin[i+1][0]+65)+str(chemin[i+1][1]+1),"\n")
        deplacer(grille,chemin[i],chemin[i+1],tresor,2)
    else:
        #En cas d'enchainement l'IA regarde si ce coup est le dernier de la grille pour le laisser au joueur et ne pas avoir de malus
        #Si elle n'a pas d'enchainement elle jouera le coup pour ne pas contredire les règles
        case_inter = case_intermediaire(chemin[taille-1],chemin[taille-2])
        grille_simulation = creer_grille_simulation(grille,chemin[taille-1],[chemin[taille-2],case_inter])
        
        if not fin_partie(grille_simulation):
            i = taille-2
            print(chr(chemin[i][0]+65)+str(chemin[i][1]+1),"-->",chr(chemin[i+1][0]+65)+str(chemin[i+1][1]+1),"\n")
            deplacer(grille,chemin[i],chemin[i+1],tresor,2)
            
    

def compter_point(chemin,grille): 
    """Compte les points en suivant un enchainement ou un coup simple
       chemin -> liste de tuple de coordonnees
       grille -> liste de liste de chaine de caractere"""
    point = 0
    for i in range(0,len(chemin)-1):
        c = case_intermediaire(chemin[i],chemin[i+1])
        pion = grille[c[0]][c[1]]

        if pion == "J":
            point += 1
        elif pion == "R":
            point += 2
        else:
            point += 3
        
        

    return point

def transfo_liste(liste):
    """transforme la liste de tuple en liste de liste de tuple et
       cree une deuxieme liste de liste destiner au stockage de pion pris
       liste -> liste de tuple"""
    result = []
    trou = []

    for elem in liste:
        result.append([elem])
        trou.append([])

    return trou,result
    
def creer_grille_simulation(grille,coor_p_j,trou):
    """creer une grille en fonction de la grille de depart les pions pris et la position du pion jaune de l'IA
       grille -> liste de liste de chaine de caractere
       coor_p_j -> tuple de coordonnee
       trou -> liste de tuple de coordonnee"""
    new_grille = list()

    for i in range(len(grille)):
        ligne = list()
        for j in range(len(grille[0])):
            ligne.append(grille[i][j])

        new_grille.append(ligne)

    for elem in trou:
        new_grille[elem[0]][elem[1]] = " "

    new_grille[coor_p_j[0]][coor_p_j[1]] = "J"

    return new_grille

                
def trouver_chemins(coor_depart,grille):
    """recherche tout les chemin a partir d'une liste de depart
       grille -> liste de liste de chaine de caractere
       coor_depart -> liste de tuple de coordonnee"""

    trous,chemins = transfo_liste(coor_depart)
    chemins_fini = []

    while chemins:
        chemin_traite = chemins.pop(0)
        trou_traite = trous.pop(0)
        depart = chemin_traite[len(chemin_traite)-1]
        grille_simulation = creer_grille_simulation(grille,depart,trou_traite)
        arrivees = coordonnee_arrive(grille_simulation,depart)

        if arrivees == []:
            chemins_fini.append(chemin_traite)
        else:
            for elem in arrivees:
                chemins.append(chemin_traite+[elem])
                trous.append(trou_traite + [case_intermediaire(depart,elem)] + [depart])

    return chemins_fini

def max_point(grille):
    """renvoie le chemin maximisant les points sur une grille
       grille -> liste de liste de chaine de caractere"""
    chemins = trouver_chemins(lister_coup(grille)[0],grille)
    maxi = 0
    chemin_maxi = []
    for chemin in chemins:
        point = compter_point(chemin,grille)
        if point > maxi:
            maxi = point
            chemin_maxi = chemin

        elif maxi == point: #sert a rendre l'IA moins previsible
            if random.randint(0,1) == 0:
                maxi = point
                chemin_maxi = chemin

    return chemin_maxi

def test_atelier_5(grille,tresor):
    joueur,grille,tresor = config_fin(grille,tresor)

    print("test calcul du chemin maximisant les points sur configuration de fin:")
    assert max_point(grille) == [(0,7),(2,7),(4,7),(6,5)], "Erreur calcul du chemin"
    print("test fini\n")
    
    print("Le test de l'atelier 5 a été passé\n\n")
####Code Principale######

menu(grille,tresor)

    

