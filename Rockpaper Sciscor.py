import tkinter as tk
import random

root = tk.Tk()
root.geometry("300x200")
root.title("Rock Paper Scissors Game")

# Define the game logic
def play_game(user_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    result = ""

    if user_choice == computer_choice:
        result = "Tie!"
    elif user_choice == "rock" and computer_choice == "scissors":
        result = "You win!"
    elif user_choice == "paper" and computer_choice == "rock":
        result = "You win!"
    elif user_choice == "scissors" and computer_choice == "paper":
        result = "You win!"
    else:
        result = "You lose!"

    # Display the result
    result_label.config(text=f"Computer choice: {computer_choice}\nResult: {result}")

# Create the GUI
rock_button = tk.Button(root, text="Rock", command=lambda: play_game("rock"))
rock_button.pack()

paper_button = tk.Button(root, text="Paper", command=lambda: play_game("paper"))
paper_button.pack()

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game("scissors"))
scissors_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
