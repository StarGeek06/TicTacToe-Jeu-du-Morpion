import random

# Faire la grille

def makeboard(grille):
    for row in range(3):
        for col in range(3):
            print(grille[row][col], end='')
            if col < 2:
                print(' | ', end='')
        print()
        if row < 2:
            print("---------")

# Vérifier si la grille est pleine
def isfull(grille):
    return all(all(cell != '' for cell in row) for row in grille)

# Vérifier le gagnant
def winner(grille):
    for row in range(3):
        if grille[row][0] == grille[row][1] == grille[row][2] and grille[row][0] != '':
            return True

    for col in range(3):
        if grille[0][col] == grille[1][col] == grille[2][col] and grille[0][col] != '':
            return True

    if grille[0][0] == grille[1][1] == grille[2][2] and grille[0][0] != '':
        return True
    
    if grille[0][2] == grille[1][1] == grille[2][0] and grille[2][0] != '':
        return True


    return False

# Vérifier si c'est un match nul
def match_nul(grille):
    return isfull(grille) and not winner(grille)

# Jouer un coup
def allow_move(grille, row, col, symbol):
    if grille[row][col] == '':
        grille[row][col] = symbol
        return True
    else:
        return False
    
#Mon jeu proprement dit
def TicTacToe():
    print("\nOui oui, je te souhaite la bienvenue dans le légendaire jeu du morpion.\n")
    
    j1letter = random.choice(['X', 'O'])
    j2letter = 'O' if j1letter == 'X' else 'X'

    print("Le joueur 1 a la lettre:", j1letter)
    print("Le joueur 2 a la lettre:", j2letter)

    grille = [['' for _ in range(3)] for _ in range(3)]

    makeboard(grille)

    while not match_nul(grille) and not winner(grille):

        print(" Joueur 1, choisis ta position,\n")
        print("Les lignes et les colonnes sont entre 1 et 3\n")

        r1 = int(input("row: "))
        c1 = int(input("col: "))

        while r1 < 1 or r1 > 3 or c1 < 1 or c1 > 3 or not allow_move(grille, r1-1, c1-1, j1letter):

            print("Ewo, quand on vous parle faut écouter!!. \nLes lignes et les colonnes sont entre 1 et 3.\n")

            r1 = int(input("row: "))
            c1 = int(input("col: "))

        grille[r1-1][c1-1] = j1letter
        makeboard(grille)

        if not match_nul(grille) and not winner(grille):
            print("Au tour du joueur 2, choisis ta position,\n")
            print("Les lignes sont entre 1 et 3")
            print("Les colonnes sont entre 1 et 3\n")

            r2 = int(input("row: "))
            c2 = int(input("col: "))

            while r2 < 1 or r2 > 3 or c2 < 1 or c2 > 3 or not allow_move(grille, r2-1, c2-1, j2letter):
                print("Je pensais que tu étais différent. \nLes lignes et les colonnes sont entre 1 et 3.\n")

                r2 = int(input("row: "))
                c2 = int(input("col: "))

            grille[r2-1][c2-1] = j2letter
            makeboard(grille)

    if winner(grille):

        winning_player = j1letter if j1letter == grille[r1-1][c1-1] else j2letter
        print(f"Le joueur {winning_player} a gagné!")
    else:
        print("Match nul!")



TicTacToe()
