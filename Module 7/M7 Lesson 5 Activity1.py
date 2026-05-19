from tkinter import *

base_window = Tk()
base_window.geometry("450x350")
base_window.title("Primary Stage")

def launch_overlay():
    overlay = Toplevel()
    overlay.geometry("200x120")
    overlay.title("Secondary Stage")

    popup_msg = Label(overlay, text="Secondary view active")
    popup_msg.pack(pady=10)

    overlay.mainloop()

main_msg = Label(base_window, text="Primary view active")
action_trigger = Button(base_window, text="Initialize secondary view", command=launch_overlay)

main_msg.pack(pady=10)
action_trigger.pack(pady=10)

base_window.mainloop()