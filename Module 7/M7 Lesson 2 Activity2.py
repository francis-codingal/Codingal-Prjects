from tkinter import *

main_window = Tk()
main_window.title('Registration Interface')
main_window.geometry('450x450')

form_container = Frame(master=main_window, height=220, width=400, bg="#E8F0FE")

user_lbl = Label(form_container, text="User Name", bg="#4A90E2", fg='white', width=15)
contact_lbl = Label(form_container, text="Contact Email", bg="#4A90E2", fg='white', width=15)
security_lbl = Label(form_container, text="Set Password", bg="#4A90E2", fg='white', width=15)

user_field = Entry(form_container)
contact_field = Entry(form_container)
security_field = Entry(form_container, show="#")

def handle_submission():
    account_name = user_field.get()
    welcome_msg = "Welcome aboard, " + account_name
    status_msg = "\nYour profile has been successfully set up!"
    display_log.insert(END, welcome_msg)
    display_log.insert(END, status_msg)

display_log = Text(bg="#F5F5F5", fg="darkblue")

submit_action = Button(text="Register Now", command=handle_submission, bg="green", fg="white")

form_container.place(x=25, y=10)
user_lbl.place(x=20, y=20)
user_field.place(x=180, y=20)
contact_lbl.place(x=20, y=80)
contact_field.place(x=180, y=80)
security_lbl.place(x=20, y=140)
security_field.place(x=180, y=140)
submit_action.place(x=160, y=240)
display_log.place(y=290, width=450, height=150)

main_window.mainloop()