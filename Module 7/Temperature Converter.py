import tkinter as tk
from tkinter import ttk, messagebox

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        unit = combo_unit.get()

        if unit == "Celsius to Fahrenheit":
            result = (temp * 9/5) + 32
            label_result.config(text=f"{temp:.2f} °C = {result:.2f} °F")
        elif unit == "Fahrenheit to Celsius":
            result = (temp - 32) * 5/9
            label_result.config(text=f"{temp:.2f} °F = {result:.2f} °C")
        elif unit == "Celsius to Kelvin":
            result = temp + 273.15
            label_result.config(text=f"{temp:.2f} °C = {result:.2f} K")
        elif unit == "Kelvin to Celsius":
            result = temp - 273.15
            label_result.config(text=f"{temp:.2f} K = {result:.2f} °C")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Initialize window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("350x250")
root.resizable(False, False)

# UI Elements
label_title = tk.Label(root, text="Temperature Converter", font=("Arial", 14, "bold"))
label_title.pack(pady=10)

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

label_entry = tk.Label(frame_input, text="Enter Value:")
label_entry.grid(row=0, column=0, padx=5)

entry_temp = tk.Entry(frame_input, width=10)
entry_temp.grid(row=0, column=1, padx=5)

combo_unit = ttk.Combobox(
    root,
    values=[
        "Celsius to Fahrenheit",
        "Fahrenheit to Celsius",
        "Celsius to Kelvin",
        "Kelvin to Celsius"
    ],
    state="readonly",
    width=22
)
combo_unit.current(0)
combo_unit.pack(pady=5)

btn_convert = tk.Button(root, text="Convert", command=convert_temperature, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
btn_convert.pack(pady=10)

label_result = tk.Label(root, text="", font=("Arial", 12, "bold"))
label_result.pack(pady=10)

root.mainloop()
