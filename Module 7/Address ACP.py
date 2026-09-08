import tkinter as tk
from tkinter import ttk, messagebox

def submit_form():
    # Extract values
    data = {
        "Full Name": entry_name.get().strip(),
        "Street": entry_street.get().strip(),
        "City": entry_city.get().strip(),
        "State": entry_state.get().strip(),
        "ZIP Code": entry_zip.get().strip(),
        "Country": combo_country.get()
    }
    
    # Simple validation check
    missing_fields = [field for field, val in data.items() if not val]
    if missing_fields:
        messagebox.showwarning("Incomplete Form", f"Please fill in: {', '.join(missing_fields)}")
        return
        
    # Process or save data (displays a success message here)
    details = "\n".join([f"{k}: {v}" for k, v in data.items()])
    messagebox.showinfo("Address Saved", f"Submitted Address:\n\n{details}")
    clear_fields()

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_street.delete(0, tk.END)
    entry_city.delete(0, tk.END)
    entry_state.delete(0, tk.END)
    entry_zip.delete(0, tk.END)
    combo_country.current(0)

# Window Setup
root = tk.Tk()
root.title("Address Entry Form")
root.geometry("400x320")
root.resizable(False, False)

# Form Container
frame = ttk.Frame(root, padding="15")
frame.pack(fill=tk.BOTH, expand=True)

# Form Fields Layout
labels = ["Full Name:", "Street Address:", "City:", "State / Province:", "ZIP / Postal Code:", "Country:"]

for i, text in enumerate(labels):
    ttk.Label(frame, text=text).grid(row=i, column=0, sticky=tk.W, pady=4)

# Inputs
entry_name = ttk.Entry(frame, width=30)
entry_street = ttk.Entry(frame, width=30)
entry_city = ttk.Entry(frame, width=30)
entry_state = ttk.Entry(frame, width=30)
entry_zip = ttk.Entry(frame, width=30)
combo_country = ttk.Combobox(frame, values=["United States", "Canada", "United Kingdom", "India", "Australia", "Other"], width=28, state="readonly")
combo_country.current(0)

# Place Inputs in Grid
entry_name.grid(row=0, column=1, pady=4)
entry_street.grid(row=1, column=1, pady=4)
entry_city.grid(row=2, column=1, pady=4)
entry_state.grid(row=3, column=1, pady=4)
entry_zip.grid(row=4, column=1, pady=4)
combo_country.grid(row=5, column=1, pady=4)

# Button Panel
btn_frame = ttk.Frame(frame)
btn_frame.grid(row=6, column=0, columnspan=2, pady=15)

btn_submit = ttk.Button(btn_frame, text="Submit", command=submit_form)
btn_submit.pack(side=tk.LEFT, padx=5)

btn_clear = ttk.Button(btn_frame, text="Clear", command=clear_fields)
btn_clear.pack(side=tk.LEFT, padx=5)

root.mainloop()
