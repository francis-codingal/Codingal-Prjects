from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

workspace = Tk()
workspace.title("Custom Text Workspace")
workspace.geometry("700(600")
workspace.rowconfigure(0, minsize=800, weight=1)
workspace.columnconfigure(1, minsize=800, weight=1)

def load_file():
    target_path = askopenfilename(
        filetypes=[("Text Documents", "*.txt"), ("All Formats", "*.*")]
    )
    if not target_path:
        return
    editor_space.delete(1.0, END)
    with open(target_path, "r") as file_stream:
        content = file_stream.read()
        editor_space.insert(END, content)
    workspace.title(f"Custom Text Workspace - {target_path}")

def export_file():
    target_path = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Documents", "*.txt"), ("All Formats", "*.*")],
    )
    if not target_path:
        return
    with open(target_path, "w") as file_stream:
        updated_text = editor_space.get(1.0, END)
        file_stream.write(updated_text)
    workspace.title(f"Custom Text Workspace - {target_path}")

editor_space = Text(workspace)
control_panel = Frame(workspace, relief=GROOVE, bd=3)
action_open = Button(control_panel, text="Load File", command=load_file)
action_save = Button(control_panel, text="Save Copy", command=export_file)

action_open.grid(row=0, column=0, sticky="ew", padx=8, pady=8)
action_save.grid(row=1, column=0, sticky="ew", padx=8)

control_panel.grid(row=0, column=0, sticky="ns")
editor_space.grid(row=0, column=1, sticky="nsew")

workspace.mainloop()