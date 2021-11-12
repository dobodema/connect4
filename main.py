# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def grille_vide(n,m):
    return[[0 for i in range(m)]for j in range(n)]

nomC = 7
nomR = 6
grille =()

def debut():
    global grille
    global nomC, nomR
    grille = grille_vide(nomR, nomC)
    pass

def affichage_grille(t):
    for i in range (len(t)):
        for j in range(len(t[i])):
            print(t[i][j], ' ', end='')
        print()
    print('===================')
    print('1  2  3  4  5  6  7')


def gridfull():
    pass


def selectPlayer(p):
    pass


def play(p):
    pass


def victoire(p):
    pass


def connect4(name):
    global grille
    # print(f'Hi {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    debut()
    while True:
        affichage_grille(grille)
        if gridfull() :
            print('stalemate/draw')
            break
            
        p = selectPlayer(p) # or toggle p
        play(p)
        if victoire(p) :
            print('player {p} won')
            break

if __name__ == '__main__':
    connect4('Py:Charm')
