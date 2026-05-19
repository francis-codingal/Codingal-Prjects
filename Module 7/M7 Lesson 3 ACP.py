from tkinter import *

window = Tk()
window.title('Length Converter App')
window.geometry('400x400')
window.configure(bg='#ECEFF1')

def convert_length():
    result_box.delete('1.0', END)
    try:
        inches = float(inches_entry.get())
        centimeters = inches * 2.54
        output_text = f"{inches} inches =\n{centimeters:.2f} cm"
        result_box.insert(END, output_text)
    except ValueError:
        result_box.insert(END, "Error: Please enter a valid number.")

title_lbl = Label(
    window, 
    text="Inches to Centimeters", 
    font=("Helvetica", 14, "bold"), 
    fg="#37474F", 
    bg="#ECEFF1"
)
title_lbl.pack(pady=20)

desc_lbl = Label(
    window, 
    text="Enter the length in inches below to convert it to centimeters.", 
    font=("Helvetica", 10), 
    fg="#546E7A", 
    bg="#ECEFF1",
    wraplength=350
)
desc_lbl.pack(pady=5)

input_frame = Frame(window, bg="#ECEFF1")
input_frame.pack(pady=15)

input_lbl = Label(
    input_frame, 
    text="Length in Inches:", 
    font=("Helvetica", 11), 
    fg="#263238", 
    bg="#ECEFF1"
)
input_lbl.grid(row=0, column=0, padx=10)

inches_entry = Entry(
    input_frame, 
    width=15, 
    font=("Helvetica", 11), 
    justify='center'
)
inches_entry.grid(row=0, column=1, padx=10)

convert_btn = Button(
    window, 
    text="Convert", 
    command=convert_length, 
    font=("Helvetica", 11, "bold"), 
    bg="#00897B", 
    fg="white", 
    activebackground="#00695C", 
    activeforeground="white",
    padx=15, 
    pady=5
)
convert_btn.pack(pady=15)

result_box = Text(
    window, 
    height=4, 
    width=35, 
    font=("Helvetica", 11), 
    bg="#FFFFFF", 
    fg="#263238", 
    relief=SOLID, 
    borderwidth=1
)
result_box.pack(pady=10)

window.mainloop()