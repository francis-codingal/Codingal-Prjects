import secrets
import string
import tkinter as tk
from tkinter import messagebox, ttk


def generate_password():
    length = int(spin_length.get())

    char_pool = ""
    if var_uppercase.get():
        char_pool += string.ascii_uppercase
    if var_lowercase.get():
        char_pool += string.ascii_lowercase
    if var_digits.get():
        char_pool += string.digits
    if var_symbols.get():
        char_pool += string.punctuation

    if not char_pool:
        messagebox.showwarning(
            "Selection Error", "Select at least one character type."
        )
        return

    password = "".join(secrets.choice(char_pool) for _ in range(length))
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)

    update_strength(length, char_pool)


def update_strength(length, pool):
    types_selected = sum(
        [
            var_uppercase.get(),
            var_lowercase.get(),
            var_digits.get(),
            var_symbols.get(),
        ]
    )

    if length >= 14 and types_selected >= 3:
        lbl_strength.config(text="Strength: Strong", fg="#2e7d32")
    elif length >= 8 and types_selected >= 2:
        lbl_strength.config(text="Strength: Medium", fg="#f57f17")
    else:
        lbl_strength.config(text="Strength: Weak", fg="#c62828")


def copy_to_clipboard():
    password = entry_password.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password generated to copy.")


root = tk.Tk()
root.title("Password Generator")
root.geometry("380x360")
root.resizable(False, False)

frame = ttk.Frame(root, padding="15")
frame.pack(fill=tk.BOTH, expand=True)

ttk.Label(frame, text="Password Generator", font=("Arial", 14, "bold")).pack(
    pady=(0, 10)
)

frame_display = ttk.Frame(frame)
frame_display.pack(fill=tk.X, pady=5)

entry_password = ttk.Entry(frame_display, font=("Consolas", 12))
entry_password.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

btn_copy = ttk.Button(
    frame_display, text="Copy", width=6, command=copy_to_clipboard
)
btn_copy.pack(side=tk.RIGHT)

lbl_strength = tk.Label(frame, text="Strength: --", font=("Arial", 9, "bold"))
lbl_strength.pack(anchor=tk.W, pady=(2, 10))

frame_controls = ttk.LabelFrame(frame, text=" Settings ", padding="10")
frame_controls.pack(fill=tk.X, pady=5)

frame_len = ttk.Frame(frame_controls)
frame_len.pack(fill=tk.X, pady=5)

ttk.Label(frame_len, text="Password Length:").pack(side=tk.LEFT)
spin_length = ttk.Spinbox(frame_len, from_=6, to=64, width=5)
spin_length.set(16)
spin_length.pack(side=tk.RIGHT)

var_uppercase = tk.BooleanVar(value=True)
var_lowercase = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

ttk.Checkbutton(
    frame_controls, text="Include Uppercase (A-Z)", variable=var_uppercase
).pack(anchor=tk.W, pady=2)
ttk.Checkbutton(
    frame_controls, text="Include Lowercase (a-z)", variable=var_lowercase
).pack(anchor=tk.W, pady=2)
ttk.Checkbutton(
    frame_controls, text="Include Numbers (0-9)", variable=var_digits
).pack(anchor=tk.W, pady=2)
ttk.Checkbutton(
    frame_controls, text="Include Symbols (!@#$)", variable=var_symbols
).pack(anchor=tk.W, pady=2)

btn_generate = tk.Button(
    frame,
    text="Generate Password",
    command=generate_password,
    bg="#1976D2",
    fg="white",
    font=("Arial", 10, "bold"),
    pady=5,
)
btn_generate.pack(fill=tk.X, pady=(15, 0))

generate_password()

root.mainloop()
