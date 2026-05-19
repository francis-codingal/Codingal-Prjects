from tkinter import *

root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x300')
root.configure(bg='#F4F6F7')

def calculate_product():
    result_box.delete('1.0', END)
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_text = f"The product of {num1} and {num2} is:\n{product}"
        result_box.insert(END, result_text)
    except ValueError:
        result_box.insert(END, "Error: Please enter valid numbers.")

desc_lbl = Label(
    root, 
    text="This app calculates the product of two numbers.", 
    fg="#2C3E50", 
    bg="#F4F6F7", 
    font=("Arial", 10, "italic")
)
desc_lbl.pack(pady=5)

lbl1 = Label(root, text="Enter First Number:", fg="#34495E", bg="#F4F6F7", font=("Arial", 10))
lbl1.pack()
entry1 = Entry(root, width=20, justify='center')
entry1.pack(pady=2)

lbl2 = Label(root, text="Enter Second Number:", fg="#34495E", bg="#F4F6F7", font=("Arial", 10))
lbl2.pack()
entry2 = Entry(root, width=20, justify='center')
entry2.pack(pady=2)

calc_btn = Button(
    root, 
    text="Calculate Product", 
    command=calculate_product, 
    bg="#27AE60", 
    fg="white", 
    activebackground="#2ECC71", 
    activeforeground="white",
    font=("Arial", 10, "bold")
)
calc_btn.pack(pady=10)

result_box = Text(root, height=3, width=35, font=("Arial", 10), bg="#FFFFFF", fg="#2C3E50")
result_box.pack(pady=5)

root.mainloop()