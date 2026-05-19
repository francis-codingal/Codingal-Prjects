from tkinter import *

window = Tk()
window.title('Length Converter App')
window.geometry('400x400')
window.configure(bg='#F8F9FA')

def check_strength():
    result_box.delete('1.0', END)
    password = pass_entry.get()
    length = len(password)
    
    if length == 0:
        result_box.insert(END, "Please enter a password.")
        result_box.configure(fg="black")
        return
        
    if length <= 5:
        strength = "Weak"
        color = "#FF3B30"
    elif 6 <= length <= 8:
        strength = "Medium"
        color = "#FFCC00"
    elif 9 <= length <= 12:
        strength = "Strong"
        color = "#34C759"
    else:
        strength = "Very Strong"
        color = "#00875A"
        
    result_box.insert(END, f"Password Strength: {strength}")
    result_box.configure(fg=color)

title_lbl = Label(
    window, 
    text="Password Strength Checker", 
    font=("Arial", 14, "bold"), 
    fg="#2C3E50", 
    bg='#F8F9FA'
)
title_lbl.pack(pady=20)

input_frame = Frame(window, bg='#F8F9FA')
input_frame.pack(pady=15)

pass_lbl = Label(
    input_frame, 
    text="Enter Password:", 
    font=("Arial", 11), 
    fg="#34495E", 
    bg='#F8F9FA'
)
pass_lbl.grid(row=0, column=0, padx=10)

pass_entry = Entry(
    input_frame, 
    width=20, 
    font=("Arial", 11), 
    show="*"
)
pass_entry.grid(row=0, column=1, padx=10)

check_btn = Button(
    window, 
    text="Check Strength", 
    command=check_strength, 
    font=("Arial", 11, "bold"), 
    bg="#2980B9", 
    fg="white", 
    activebackground="#3498DB", 
    activeforeground="white",
    padx=15, 
    pady=5
)
check_btn.pack(pady=20)

result_box = Text(
    window, 
    height=2, 
    width=30, 
    font=("Arial", 12, "bold"), 
    bg="#FFFFFF", 
    relief=SOLID, 
    borderwidth=1
)
result_box.pack(pady=10)

window.mainloop()