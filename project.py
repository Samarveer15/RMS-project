import tkinter as tk
from tkinter import ttk
import random

def play_game(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "Rock" and computer == "Scissors") or (user == "Paper" and computer == "Rock") or (user == "Scissors" and computer == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

root = tk.Tk()
root.geometry("400x400")
root.title("Rock Paper Scissors Game")

ttk.Label(root, text="Choose Rock, Paper, or Scissors:").pack(pady=10)

ttk.Button(root, text="Rock", command=lambda: play_game("Rock")).pack(pady=5)
ttk.Button(root, text="Paper", command=lambda: play_game("Paper")).pack(pady=5)
ttk.Button(root, text="Scissors", command=lambda: play_game("Scissors")).pack(pady=5)

result_label = ttk.Label(root, text="")
result_label.pack(pady=20)

root.mainloop()
