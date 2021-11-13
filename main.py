# PROJET NSI: LE PUISSANCE 4

def grille_vide(n,m):
    return[[0 for i in range(n)]for j in range(m)]

# globals
nomC = 7
nomR = 6
grille = ()


def input_int(str, min, max):
    ch = -1
    while ch < min or ch > max:
        try:
            ch = int(input(str))
            if ch < min or ch > max:
                print('Erreur choix est entre', min, 'et', max)
        except ValueError:
            print('Erreur le choix est entre', min, 'et', max)
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
    # verifie si la grille est pleine, si oui return True (ou sinon return False des que un espace (0) est trouvé
    for i in range (len(t[0])-1,-1, -1):
        for j in range(len(t)):
            if t[j][i] == 0:
                return False
    return True

def joueur(p):
    # bascule le joueur
    return 2 if p == 1 else 1


def jouer(p, grille):
    # choisir la colonne
    global nomC, nomR
    print(f'C\'EST AU JOUEUR {p} A JOUER')
    while True:
        #pour s'occuper des inputs non entiers
        col = input_int('ENTREZ LA COLONNE:', 1, nomC)
        if col < 1 or col > nomC:
            print(f'Le numéro doit être entre 1 et {nomC}')
        else:
            col = col - 1
            if grille[col][nomR-1] != 0:
                print(f'La colonne {col + 1} est pleine, veuiillez entrez une autre colonne')
            else:
                for r in range (len(grille[col])):
                    if grille[col][r] == 0:
                        grille[col][r] = p
                        break
                break


def vertical4(p, grille):
    global nomC, nomR
    # true si on trouve 4 d'affilée, sinon False
    # pour toutes les colonnes tour a tour
    for c in range(len(grille)):
        # for rows 0 to (6 - 4)
        col = grille[c]
        for r in range(len(col) - 4):
            # Verifiez position jusqu'a position +3
            trouve = True
            for i in range(4) :
                # si ce n'est pas égal au joueur, mettre False, break
                if grille[c][r+i] != p:
                    trouve = False
                    break
            # fin de la boucle si 4 pions d'affilée sont trouvés, si oui return True
            if trouve :
                return True

    return False


def flip(t):
    flipped = grille_vide(len(t), len(t[0]))
    for i in range (len(t[0])-1,-1, -1):
        for j in range(len(t)):
            flipped[i][j] = t[j][i]
    return flipped


def horizontal(p, grille):
    #  true si 4 d'affiléé sont trouvés, sinon false
    # retourne la grille
    flipped = flip(grille)
    return vertical4(p,flipped)


def diag_gauche(p, grille):
    # true si 4 trouvés, sinon false
    global nomC, nomR
    # pour toutes les colonnes tour a tour
    numCols = len(grille)
    for c in range(numCols - 4, numCols):
        # pour les lignes de 0 à (6-4)
        col = grille[c]
        for r in range(len(col) - 4 + 1):
            # Verifiez position jusqu'a position +3
            trouve = True
            for i in range(4) :
                # si ce n'est pas égal au joueur, mettre False, break
                if grille[c-i][r+i] != p:
                    trouve = False
                    break
            # fin de la boucle si trouvé, return True
            if trouve :
                return True

    return False


def mirroir(t):
    cols = len(t)
    grille_mirroir = grille_vide(len(t[0]), cols)
    # créé un mirroir des colonnes, donc 6 devient 0, et 5 devient 1 etc...
    for c in range(cols):
        grille_mirroir[cols - 1 - c] = t[c]
    return grille_mirroir


def diag_droit(p, grille):
    grille_mirroir = mirroir(grille)
    return diag_gauche(p, grille_mirroir)


def victoire(p, grille):
    return vertical4(p, grille) or horizontal(p, grille) or diag_gauche(p, grille) or diag_droit(p, grille)


def puissance4():
    global grille
    debut()
    p = 0
    while True:
        affichage_grille(grille)
        if grille_complete(grille) :
            print('IMPASSE/MATCH NUL')
            break
            
        p = joueur(p) # ou bascule joueur
        jouer(p, grille)
        if victoire(p, grille) :
            print(f'FELICITATIONS LE JOUEUR {p} A GAGNE')
            affichage_grille(grille)
            break

if __name__ == '__main__':
    puissance4()
