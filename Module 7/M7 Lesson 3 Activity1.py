from tkinter import *

main_frame = Tk()
main_frame.title("Signal Capture")
main_frame.geometry("150x150")

def log_key(trigger):
    print(trigger.char)

main_frame.bind("<Key>", log_key)

def log_press(trigger):
    print("\nAction triggered successfully!")

action_node = Button(text="Execute")
action_node.pack()

action_node.bind("<Button-1>", log_press)

main_frame.mainloop()