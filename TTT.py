import tkinter as tk
from tkinter import messagebox
import random

#Faire la grille
def makeboard(grille):
    for row in range(3):
        for col in range(3):
            print(grille[row][col], end='')
            if col < 2:
                print(' | ', end='')
        print()
        if row < 2:
            print("---------")

#On va vérifier que la grille est pleine
def isfull(grille):
    return all(all(cell != '' for cell in row) for row in grille)

#Vérifier les possibilités de gagner
def winner(grille):

    #Gagner sur les lignes
    for row in range(3):
        if grille[row][0] == grille[row][1] == grille[row][2] and grille[row][0] != '':
            return True
    
    #Gagner sur les colonnes
    for col in range(3):
        if grille[0][col] == grille[1][col] == grille[2][col] and grille[0][col] != '':
            return True

    #Gagner sur les diagonales
    if grille[0][0] == grille[1][1] == grille[2][2] and grille[0][0] != '':
        return True

    if grille[0][2] == grille[1][1] == grille[2][0] and grille[2][0] != '':
        return True

    return False

#Quand c'est un match nul
def match_nul(grille):
    return isfull(grille) and not winner(grille)

#Permetre le déplacement
def allow_move(grille, row, col, symbol):
    if grille[row][col] == '':
        grille[row][col] = symbol
        return True
    else:
        return False


def TicTacToe():

    #Interface Graphique

    root = tk.Tk()
    root.title("Morpion")

    joueur = random.choice(['X', 'O'])

    grid = [['' for _ in range(3)] for _ in range(3)]

    def make_move(row, col):

        nonlocal joueur

        if grid[row][col] == "":
            grid[row][col] = joueur

            update_board()
            check_winner()

            joueur = 'O' if joueur == 'X' else 'X'

    def update_board():
        for i in range(3):
            for j in range(3):
                button = buttons[i][j]
                button.config(text=grid[i][j])

    def check_winner():

        for row in range(3):
            if grid[row][0] == grid[row][1] == grid[row][2] and grid[row][0] != '':
                show_winner_message(grid[row][0])
                return
            
        for col in range(3):
            if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] != '':
                show_winner_message(grid[0][col])
                return
            
        if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != '':
            show_winner_message(grid[0][0])
            return
        
        if grid[0][2] == grid[1][1] == grid[2][0] and grid[2][0] != '':
            show_winner_message(grid[0][2])
            return
        
        if isfull(grid):
            messagebox.showinfo("Boff inh!!", "Match nul!")

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
    center_frame.pack(pady=20)

    

    buttons = []
    for i in range(3):
        button_row = []
        for j in range(3):
            button = tk.Button(center_frame, text="", bg="#451130", fg="#ffffff", width=15, height=5, font=('Helvetica', 14, 'bold'), command=lambda row=i, col=j: make_move(row, col))
            button.grid(row=i, column=j)
            button_row.append(button)
        buttons.append(button_row)

    root.configure(bg="#000000")  # Changement de la couleur de fond de l'interface
    root.geometry("400x400")  # Définition de la taille de l'interface

    reset_button = tk.Button(root, text="Nouvelle partie", bg="#451130", fg="#ffffff", font=('Helvetica', 14, 'bold'),width=15, height=2, command=reset_game)
    reset_button.pack()

    root.mainloop()

TicTacToe()
