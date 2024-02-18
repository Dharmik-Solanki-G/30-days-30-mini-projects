import tkinter as tk
import random
from tkinter import messagebox
from tkinter import font

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe - Single Player")
        self.player = "X"
        self.computer = "O"
        self.board = [[" " for _ in range(3)] for _ in range(3)]

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text="", font=("Helvetica", 20), width=6, height=3,
                                                command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 16), fg="black", pady=10)
        self.result_label.grid(row=3, columnspan=3)

    def make_move(self, row, col):
        elephant_font = font.Font(family="Elephant", size=24)

        if self.board[row][col] == " ":
            self.board[row][col] = self.player
            self.buttons[row][col].config(text=self.player, bg="white")
            if self.check_winner(row, col):
                self.result_label.config(text="YOU WIN!", fg="green", font=elephant_font)
                self.highlight_winner(row, col)
                self.root.after(1000, self.reset_board)
            elif self.check_draw():
                self.result_label.config(text="It's a DRAW!", fg="blue", font=elephant_font)
                self.root.after(1000, self.reset_board)
            else:
                self.computer_move()

    def computer_move(self):
        best_score = float("-inf")
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = self.computer
                    score = self.minimax(False)
                    self.board[i][j] = " "
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        if best_move:
            row, col = best_move
            self.board[row][col] = self.computer
            self.buttons[row][col].config(text=self.computer, bg="lightcoral")
            if self.check_winner(row, col):
                self.result_label.config(text="YOU LOSS!", fg="red")
                self.highlight_winner(row, col)
                self.root.after(1000, self.reset_board)
            elif self.check_draw():
                self.result_label.config(text="It's a DRAW!", fg="lightblue")
                self.root.after(1000, self.reset_board)

    def minimax(self, is_maximizing):
        if self.check_winner(0, 0):
            return -1 if is_maximizing else 1
        if self.check_draw():
            return 0

        if is_maximizing:
            best_score = float("-inf")
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == " ":
                        self.board[i][j] = self.computer
                        score = self.minimax(False)
                        self.board[i][j] = " "
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == " ":
                        self.board[i][j] = self.player
                        score = self.minimax(True)
                        self.board[i][j] = " "
                        best_score = min(score, best_score)
            return best_score

    def check_winner(self, row, col):
        player = self.board[row][col]
        # Check row
        if all([cell == player for cell in self.board[row]]):
            return True
        # Check column
        if all([self.board[i][col] == player for i in range(3)]):
            return True
        # Check diagonals
        if all([self.board[i][i] == player for i in range(3)]) or \
           all([self.board[i][2-i] == player for i in range(3)]):
            return True
        return False

    def check_draw(self):
        return all([cell != " " for row in self.board for cell in row])

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = " "
                self.buttons[i][j].config(text="", bg="white")
        self.player = "X"
        self.computer = "O"
        self.result_label.config(text="")

    def highlight_winner(self, row, col):
        player = self.board[row][col]
        # Check row
        if all([cell == player for cell in self.board[row]]):
            for j in range(3):
                self.buttons[row][j].config(bg="lightgreen")
        # Check column
        if all([self.board[i][col] == player for i in range(3)]):
            for i in range(3):
                self.buttons[i][col].config(bg="lightgreen")
        # Check diagonals
        if all([self.board[i][i] == player for i in range(3)]):
            for i in range(3):
                self.buttons[i][i].config(bg="lightgreen")
        if all([self.board[i][2-i] == player for i in range(3)]):
            for i in range(3):
                self.buttons[i][2-i].config(bg="lightgreen")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
