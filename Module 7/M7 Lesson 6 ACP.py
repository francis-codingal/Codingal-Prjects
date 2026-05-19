from tkinter import *
import random

window = Tk()
window.title('Length Converter App')
window.geometry('400x400')
window.configure(bg='#ECEFF1')

def play_round(user_choice):
    result_box.delete('1.0', END)
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    
    if user_choice == computer_choice:
        outcome = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        outcome = "You Win!"
    else:
        outcome = "Computer Wins!"
        
    summary_text = f"Your Choice: {user_choice}\nComputer's Choice: {computer_choice}\n\n{outcome}"
    result_box.insert(END, summary_text)

title_lbl = Label(
    window, 
    text="Rock Paper Scissors", 
    font=("Helvetica", 16, "bold"), 
    fg="#263238", 
    bg="#ECEFF1"
)
title_lbl.pack(pady=20)

btn_frame = Frame(window, bg="#ECEFF1")
btn_frame.pack(pady=20)

rock_btn = Button(
    btn_frame, 
    text="Rock", 
    command=lambda: play_round("Rock"), 
    width=10, 
    font=("Helvetica", 11, "bold"), 
    bg="#CFD8DC"
)
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = Button(
    btn_frame, 
    text="Paper", 
    command=lambda: play_round("Paper"), 
    width=10, 
    font=("Helvetica", 11, "bold"), 
    bg="#CFD8DC"
)
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = Button(
    btn_frame, 
    text="Scissors", 
    command=lambda: play_round("Scissors"), 
    width=10, 
    font=("Helvetica", 11, "bold"), 
    bg="#CFD8DC"
)
scissors_btn.grid(row=0, column=2, padx=5)

result_box = Text(
    window, 
    height=6, 
    width=35, 
    font=("Helvetica", 12), 
    bg="#FFFFFF", 
    fg="#263238", 
    relief=SOLID, 
    borderwidth=1
)
result_box.pack(pady=20)

window.mainloop()