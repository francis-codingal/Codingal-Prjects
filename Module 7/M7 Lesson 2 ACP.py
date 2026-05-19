from tkinter import *
from datetime import date

window = Tk()
window.title('Age Calculator App')
window.geometry('400x400')
window.configure(bg='#F5F7FA')

def calculate_age():
    result_box.delete('1.0', END)
    try:
        user_name = name_entry.get().strip()
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        
        today = date.today()
        birth_date = date(year, month, day)
        
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        
        if not user_name:
            user_name = "User"
            
        output_message = f"Hello {user_name}!\nYour present age is: {age} years old."
        result_box.insert(END, output_message)
    except ValueError:
        result_box.insert(END, "Error: Please enter a valid name and numeric date values.")

title_lbl = Label(
    window, 
    text="Age Calculator", 
    font=("Helvetica", 16, "bold"), 
    fg="#2C3E50", 
    bg="#F5F7FA"
)
title_lbl.pack(pady=15)

form_frame = Frame(window, bg="#F5F7FA")
form_frame.pack(pady=10)

name_lbl = Label(form_frame, text="Name:", font=("Helvetica", 11), fg="#34495E", bg="#F5F7FA")
name_lbl.grid(row=0, column=0, sticky=W, padx=10, pady=5)
name_entry = Entry(form_frame, width=22, font=("Helvetica", 11))
name_entry.grid(row=0, column=1, padx=10, pady=5)

day_lbl = Label(form_frame, text="Birth Date (DD):", font=("Helvetica", 11), fg="#34495E", bg="#F5F7FA")
day_lbl.grid(row=1, column=0, sticky=W, padx=10, pady=5)
day_entry = Entry(form_frame, width=22, font=("Helvetica", 11))
day_entry.grid(row=1, column=1, padx=10, pady=5)

month_lbl = Label(form_frame, text="Birth Month (MM):", font=("Helvetica", 11), fg="#34495E", bg="#F5F7FA")
month_lbl.grid(row=2, column=0, sticky=W, padx=10, pady=5)
month_entry = Entry(form_frame, width=22, font=("Helvetica", 11))
month_entry.grid(row=2, column=1, padx=10, pady=5)

year_lbl = Label(form_frame, text="Birth Year (YYYY):", font=("Helvetica", 11), fg="#34495E", bg="#F5F7FA")
year_lbl.grid(row=3, column=0, sticky=W, padx=10, pady=5)
year_entry = Entry(form_frame, width=22, font=("Helvetica", 11))
year_entry.grid(row=3, column=1, padx=10, pady=5)

calc_btn = Button(
    window, 
    text="Calculate Age", 
    command=calculate_age, 
    font=("Helvetica", 11, "bold"), 
    bg="#3498DB", 
    fg="white", 
    activebackground="#2980B9", 
    activeforeground="white",
    padx=10, 
    pady=5
)
calc_btn.pack(pady=15)

result_box = Text(
    window, 
    height=4, 
    width=40, 
    font=("Helvetica", 11), 
    bg="#FFFFFF", 
    fg="#2C3E50", 
    relief=SOLID, 
    borderwidth=1
)
result_box.pack(pady=10)

window.mainloop()