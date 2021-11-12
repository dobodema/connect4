# Connect 4 devoir maison

def grille_vide(n,m):
    return[[0 for i in range(n)]for j in range(m)]

nomC = 7
nomR = 6
grille =()


def input_int(str, min, max):
    ch = -1
    while ch < min or ch > max:
        try:
            ch = int(input(str))
            if ch < min or ch > max:
                print('erreur choix entre', min, 'et', max)
        except ValueError:
            print('erreur choix entre', min, 'et', max)
    return ch


def debut():
    global grille
    global nomC, nomR
    grille = grille_vide(nomR, nomC)
    pass


def affichage_grille(t):
    for i in range (len(t[0])-1,-1, -1):
        for j in range(len(t)):
            print(t[j][i], ' ', end='')
        print()
    print('===================')
    print('1  2  3  4  5  6  7')


def grille_complete(t):
    # TODO check if grille is full, if so return True (or rather return False as soon as a space (0) is found
    for i in range (len(t[0])-1,-1, -1):
        for j in range(len(t)):
            if t[j][i] == 0:
                return False
    return True

def joueur(p):
    # toggle player
    return 2 if p == 1 else 1


def jouer(p, grille):
    # TODO choose
    global nomC, nomR
    print(f'joueur {p} a jouer')
    while True:
        # todo cope with non-numeric
        col = input_int('enter col', 1, nomC)
        if col < 1 or col > nomC:
            print(f'Le numéro doit être entre 1 et {nomC}')
        else:
            col = col - 1
            if grille[col][nomR-1] != 0:
                print(f'La colonne {nomC} est pleine, veuiillez entrez une autres colonne')
            else:
                for r in range (len(grille[col])):
                    if grille[col][r] == 0:
                        grille[col][r] = p
                        break
                break

    # TODO choose/verify column (loop)
    # TODO do it


def vertical4(p, grille):
    global nomC, nomR
    # TODO true if 4 found, false otherwise
    # pour toutes les colonnes tour a tour
    for c in range(len(grille) - 4):
        # for rows 0 to (6 - 4)
        col = grille[c]
        for r in range(len(col) - 4):
            # check start to start + 3
            trouve = True
            for i in range(4) :
                # if non-p set Trouve to False, break
                if grille[c][r+i] != p:
                    trouve = False
                    break;
            # end of loop if trouve return True
            if trouve :
                return True

    return False


def flip(t):
    # [len(t[0])][len(t)]
    flipped = grille_vide(len(t), len(t[0]))
    for i in range (len(t[0])-1,-1, -1):
        for j in range(len(t)):
            flipped[i][j] = t[j][i]
    return flipped



def horizontal(p, grille):
    # TODO true if 4 found, false otherwise
    # flip the grille
    flipped = flip(grille);
    return vertical4(p,flipped)


def diag_gauche(p, grille):
    # TODO true if 4 found, false otherwise
    global nomC, nomR
    # TODO true if 4 found, false otherwise
    # pour toutes les colonnes tour a tour
    numCols = len(grille)
    for c in range(numCols - 4 + 1, numCols):
        # for rows 0 to (6 - 4)
        col = grille[c]
        for r in range(len(col) - 4 + 1):
            # check start to start + 3
            trouve = True
            for i in range(4) :
                # if non-p set Trouve to False, break
                if grille[c-i][r+i] != p:
                    trouve = False
                    break;
            # end of loop if trouve return True
            if trouve :
                return True

    return False


def diag_droit(p, grille):
    # TODO true if 4 found, false otherwise
    # flip the grille
    # flipped = flip(grille);
    # return diag_gauche(p,flipped)
    # TODO true if 4 found, false otherwise
    global nomC, nomR
    # TODO true if 4 found, false otherwise
    # pour toutes les colonnes tour a tour
    numCols = len(grille)
    for c in range(numCols - 4 + 1):
        # for rows 0 to (6 - 4)
        col = grille[c]
        for r in range(len(col) - 4 + 1):
            # check start to start + 3
            trouve = True
            for i in range(4) :
                # if non-p set Trouve to False, break
                if grille[c+i][r+i] != p:
                    trouve = False
                    break;
            # end of loop if trouve return True
            if trouve :
                return True

    return False


def victoire(p, grille):
    return vertical4(p, grille) or horizontal(p, grille) or diag_gauche(p, grille) or diag_droit(p, grille)


def puissance4():
    global grille
    debut()
    p = 0
    while True:
        affichage_grille(grille)
        if grille_complete(grille) :
            print('impasse/match nul')
            break
            
        p = joueur(p) # or toggle p
        jouer(p, grille)
        if victoire(p, grille) :
            print(f'joueur {p} a gagné')
            affichage_grille(grille)
            break

if __name__ == '__main__':
    puissance4()
