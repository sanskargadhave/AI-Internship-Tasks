import tkinter as tk
import random

# -------------------------------
# Step 1: Choices
# -------------------------------
choices = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0

# -------------------------------
# Step 2: Game Logic
# -------------------------------
def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    result = ""

    if user_choice == computer_choice:
        result = "It's a Draw 😐"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win 🎉"
        user_score += 1
    else:
        result = "Computer Wins 🤖"
        computer_score += 1

    # Update labels
    result_label.config(text=f"Computer: {computer_choice}\n{result}")
    score_label.config(text=f"Score -> You: {user_score} | Computer: {computer_score}")

# -------------------------------
# Step 3: GUI Setup
# -------------------------------
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")

title = tk.Label(root, text="Rock Paper Scissors Game", font=("Arial", 14))
title.pack(pady=10)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=20)

rock_btn = tk.Button(btn_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(btn_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(btn_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

# Score label
score_label = tk.Label(root, text="Score -> You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack()

# -------------------------------
# Step 4: Run App
# -------------------------------
root.mainloop()