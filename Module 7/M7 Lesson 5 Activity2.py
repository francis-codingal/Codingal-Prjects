from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

main_window = Tk()
main_window.title("Cash breakdown tool")
main_window.configure(bg="#E0F7FA")
main_window.geometry("650x420")

asset_load = Image.open("Cash Register.png")
asset_load = asset_load.resize((300, 300))
display_image = ImageTk.PhotoImage(asset_load)

graphic_holder = Label(main_window, image=display_image, bg="#E0F7FA")
graphic_holder.place(x=180, y=20)

greeting_lbl = Label(
    main_window,
    text="Welcome! Use this tool to split totals into standard notes.",
    bg="#E0F7FA",
    font=("Arial", 11)
)
greeting_lbl.place(relx=0.5, y=340, anchor=CENTER)

def prompt_user():
    user_choice = messagebox.askquestion(
        "Confirmation",
        "Proceed to the breakdown calculation panel?"
    )
    if user_choice == "yes":
        open_breakdown_panel()

start_action = Button(
    main_window,
    text="Launch System",
    command=prompt_user,
    bg="#2E7D32",
    fg="white",
    font=("Arial", 10, "bold")
)
start_action.place(x=260, y=370)

def open_breakdown_panel():
    sub_window = Toplevel()
    sub_window.title("Breakdown Panel")
    sub_window.configure(bg="#ECEFF1")
    sub_window.geometry("600x350+80+80")

    input_lbl = Label(sub_window, text="Target Sum:", bg="#ECEFF1", font=("Arial", 10, "bold"))
    sum_field = Entry(sub_window, justify="center")

    instruction_lbl = Label(
        sub_window,
        text="Distribution of available notes:",
        bg="#ECEFF1",
        font=("Arial", 10, "italic")
    )

    tier_one_lbl = Label(sub_window, text="2000 Note count:", bg="#ECEFF1")
    tier_two_lbl = Label(sub_window, text="500 Note count:", bg="#ECEFF1")
    tier_three_lbl = Label(sub_window, text="100 Note count:", bg="#ECEFF1")

    tier_one_out = Entry(sub_window, justify="center")
    tier_two_out = Entry(sub_window, justify="center")
    tier_three_out = Entry(sub_window, justify="center")

    def run_distribution():
        try:
            remaining_balance = int(sum_field.get())

            count_2000 = remaining_balance // 2000
            remaining_balance %= 2000

            count_500 = remaining_balance // 500
            remaining_balance %= 500

            count_100 = remaining_balance // 100

            tier_one_out.delete(0, END)
            tier_two_out.delete(0, END)
            tier_three_out.delete(0, END)

            tier_one_out.insert(END, str(count_2000))
            tier_two_out.insert(END, str(count_500))
            tier_three_out.insert(END, str(count_100))

        except ValueError:
            messagebox.showerror("Invalid Input", "Provide a whole numeric value.")

    process_action = Button(
        sub_window,
        text="Compute Split",
        command=run_distribution,
        bg="#37474F",
        fg="white"
    )

    input_lbl.place(x=200, y=50)
    sum_field.place(x=300, y=50)
    process_action.place(x=250, y=100)

    instruction_lbl.place(x=150, y=160)

    tier_one_lbl.place(x=130, y=200)
    tier_two_lbl.place(x=130, y=230)
    tier_three_lbl.place(x=130, y=260)

    tier_one_out.place(x=280, y=200)
    tier_two_out.place(x=280, y=230)
    tier_three_out.place(x=280, y=260)

    sub_window.mainloop()

main_window.mainloop()