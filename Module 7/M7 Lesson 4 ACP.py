from tkinter import *

window = Tk()
window.title('Age Calculator App')
window.geometry('400x400')
window.configure(bg='#F9F9F9')

def calculate_interest():
    result_box.delete('1.0', END)
    try:
        p = float(principal_entry.get())
        t = float(time_entry.get())
        r = float(rate_entry.get())
        
        si = (p * t * r) / 100
        ci = p * ((1 + r / 100) ** t) - p
        
        output_text = f"Simple Interest: Rs. {si:.2f}\nCompound Interest: Rs. {ci:.2f}"
        result_box.insert(END, output_text)
    except ValueError:
        result_box.insert(END, "Error: Please enter valid numbers.")

title_lbl = Label(
    window, 
    text="Interest Calculator", 
    font=("Arial", 14, "bold"), 
    fg="#2C3E50", 
    bg="#F9F9F9"
)
title_lbl.pack(pady=15)

input_frame = Frame(window, bg="#F9F9F9")
input_frame.pack(pady=10)

principal_lbl = Label(input_frame, text="Principal Amount:", font=("Arial", 10), fg="#34495E", bg="#F9F9F9")
principal_lbl.grid(row=0, column=0, sticky=W, padx=10, pady=8)
principal_entry = Entry(input_frame, width=20, font=("Arial", 10))
principal_entry.grid(row=0, column=1, padx=10, pady=8)

time_lbl = Label(input_frame, text="Time (Years):", font=("Arial", 10), fg="#34495E", bg="#F9F9F9")
time_lbl.grid(row=1, column=0, sticky=W, padx=10, pady=8)
time_entry = Entry(input_frame, width=20, font=("Arial", 10))
time_entry.grid(row=1, column=1, padx=10, pady=8)

rate_lbl = Label(input_frame, text="Rate of Interest (%):", font=("Arial", 10), fg="#34495E", bg="#F9F9F9")
rate_lbl.grid(row=2, column=0, sticky=W, padx=10, pady=8)
rate_entry = Entry(input_frame, width=20, font=("Arial", 10))
rate_entry.grid(row=2, column=1, padx=10, pady=8)

calc_btn = Button(
    window, 
    text="Calculate", 
    command=calculate_interest, 
    font=("Arial", 11, "bold"), 
    bg="#16A085", 
    fg="white", 
    activebackground="#1ABC9C", 
    activeforeground="white",
    padx=15, 
    pady=3
)
calc_btn.pack(pady=15)

result_box = Text(
    window, 
    height=4, 
    width=38, 
    font=("Arial", 10), 
    bg="#FFFFFF", 
    fg="#2C3E50", 
    relief=SOLID, 
    borderwidth=1
)
result_box.pack(pady=10)

window.mainloop()