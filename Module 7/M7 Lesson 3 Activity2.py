from tkinter import *
from tkinter import messagebox

app_frame = Tk()
app_frame.geometry("250x250")

def trigger_alert():
    messagebox.showwarning("System Notification", "Critical restriction encountered.")

action_element = Button(app_frame, text="Initialize Check", command=trigger_alert)
action_element.place(x=60, y=100)

app_frame.mainloop()