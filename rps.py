import random
import tkinter as tk

def play_game(player_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    result_text.set(f"You choose: {player_choice.capitalize()}\n"
                    f"Computer chooses: {computer_choice.capitalize()}\n\n"
                    f"{determine_winner(player_choice, computer_choice)}")

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

root = tk.Tk()
root.title("Rock Paper Scissors Game")

player_label = tk.Label(root, text="Player's Choice:")
player_label.pack()

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.pack()

choices = ["rock", "paper", "scissors"]
for choice in choices:
    button = tk.Button(root, text=choice.capitalize(), command=lambda ch=choice: play_game(ch))
    button.pack(side=tk.LEFT)

quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.pack()

root.mainloop()
