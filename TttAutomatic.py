import tkinter as tk
from tkinter import messagebox
import random
import math

# On va vérifier que la grille est pleine
def isfull(grille):
    return all(all(cell != '' for cell in row) for row in grille)

def evaluate(board):
    # Fonction d'évaluation simple pour le morpion
    # Vous pouvez ajuster cette fonction en fonction de votre stratégie
    if check_winner(board, 'X'):
        return 1
    elif check_winner(board, 'O'):
        return -1
    elif isfull(board):
        return 0
    else:
        return None

def check_winner(grille, symbol):
    # Vérifie le gagnant sur le morpion
    for row in range(3):
        if grille[row][0] == grille[row][1] == grille[row][2] == symbol:
            return True

    for col in range(3):
        if grille[0][col] == grille[1][col] == grille[2][col] == symbol:
            return True

    if grille[0][0] == grille[1][1] == grille[2][2] == symbol:
        return True

    if grille[0][2] == grille[1][1] == grille[2][0] == symbol:
        return True

    return False

def minimax(board, depth, maximizingPlayer):
    result = evaluate(board)

    if result is not None:
        return result

    if maximizingPlayer:
        maxEval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'X'
                    eval = minimax(board, depth - 1, False)
                    board[i][j] = ''
                    maxEval = max(maxEval, eval)
        return maxEval
    else:
        minEval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'O'
                    eval = minimax(board, depth - 1, True)
                    board[i][j] = ''
                    minEval = min(minEval, eval)
        return minEval

def bestMove(board):
    bestVal = -math.inf
    bestMove = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                board[i][j] = 'X'
                moveVal = minimax(board, 0, False)
                board[i][j] = ''
                if moveVal > bestVal:
                    bestMove = (i, j)
                    bestVal = moveVal

    return bestMove

def TicTacToe():

    # Interface Graphique

    root = tk.Tk()
    root.title("Morpion")

    joueur = random.choice(['X', 'O'])

    grid = [['' for _ in range(3)] for _ in range(3)]

    def make_move(row, col):

        nonlocal joueur

        if grid[row][col] == "":
            grid[row][col] = joueur

            update_board()
            if check_winner(grid, joueur):
                show_winner_message(joueur)
            elif isfull(grid):
                messagebox.showinfo("Boff inh!!", "Match nul")
            else:
                # C'est maintenant le tour de l'ordinateur
                computer_move()

            joueur = 'O' 
            

    def computer_move():
        move = bestMove(grid)

        if move:
            row, col = move


            grid[row][col] = 'X' 

            update_board()

            if check_winner(grid, 'X'):
                show_winner_message('X')

            elif isfull(grid):
                messagebox.showinfo("Boff inh!!", "Match nul")

    def update_board():
        for i in range(3):
            for j in range(3):
                button = buttons[i][j]
                button.config(text=grid[i][j])

    def show_winner_message(winner):
        messagebox.showinfo("Fini!!", f"Le joueur {winner} a gagné!")

    def reset_game():
        for i in range(3):
            for j in range(3):
                grid[i][j] = ''
                button = buttons[i][j]
                button.config(text='')

    bienvenue = tk.Label(root, text="Bienvenue dans mon jeu du morpion.", font=('Helvetica', 16, 'bold'), bg='#000000', fg='#ffffff')
    bienvenue.pack(pady=20)

    center_frame = tk.Frame(root)
    center_frame.pack(pady=50)

    buttons = []
    for i in range(3):
        button_row = []
        for j in range(3):
            button = tk.Button(center_frame, text="", bg="#451130", fg="#ffffff", width=10, height=5, font=('Helvetica', 14, 'bold'), command=lambda row=i, col=j: make_move(row, col))
            button.grid(row=i, column=j)
            button_row.append(button)
        buttons.append(button_row)
    
    
    root.configure(bg="#000000")  # Changement de la couleur de fond de l'interface
    root.geometry("400x400")  # Définition de la taille de l'interface


    reset_button = tk.Button(root, text="Nouvelle partie", bg="#451130", fg="#ffffff", font=('Helvetica', 14, 'bold'),width=15, height=2, command=reset_game)
    reset_button.pack()

    root.mainloop()

TicTacToe()
