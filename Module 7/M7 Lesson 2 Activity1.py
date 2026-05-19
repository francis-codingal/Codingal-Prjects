from tkinter import *

app_window = Tk()
app_window.title('Dialer Keypad')
app_window.geometry('300x350')

key_layout = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ['*', 0, '#']
]

for row_idx in range(4):
    app_window.columnconfigure(row_idx, weight=1, minsize=80)
    app_window.rowconfigure(row_idx, weight=1, minsize=60)
    
    for col_idx in range(3):
        cell_frame = Frame(
            master=app_window,
            relief=RAISED,
            borderwidth=2
        )
        cell_frame.grid(row=row_idx, column=col_idx, padx=5, pady=5)
        
        button_label = Label(
            master=cell_frame, 
            text=key_layout[row_idx][col_idx], 
            bg='#E8F5E9', 
            width=5, 
            font=('Helvetica', 12)
        )
        button_label.pack(padx=5, pady=5)

app_window.mainloop()