from tkinter import *
from datetime import date

portal = Tk()
portal.title('User Registration Portal')
portal.geometry('500x400')

header_msg = Label(text="Welcome Client", fg="black", bg="#E0E0E0", height=2, width=400)

user_label = Label(text="Enter Username", bg="#A3C1AD")
user_input = Entry()

def show_welcome():
    username = user_input.get()
    global summary_text
    summary_text = "Access granted successfully. \nLogin Date: "
    greet = "Greetings, " + username + "!\n"
    output_area.insert(END, greet)
    output_area.insert(END, summary_text)
    output_area.insert(END, date.today())

output_area = Text(height=5)

submit_btn = Button(text="Submit", command=show_welcome, height=1, bg="#2E8B57", fg='white')

header_msg.pack()
user_label.pack()
user_input.pack()
submit_btn.pack()
output_area.pack()

portal.mainloop()