import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class RestaurantOrderManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("South Indian Breakfast Management App")

        self.menu_items = {
            "IDLI (2 PCS)": 40,
            "MEDU VADA (2 PCS)": 50,
            "MASALA DOSA": 80,
            "UPMA": 45,
            "PONGAL": 60,
            "FILTER COFFEE": 25
        }

        self.exchange_rate = 0.012

        self.setup_background(root)

        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        ttk.Label(
            frame,
            text="South Indian Breakfast Management",
            font=("Arial", 20, "bold")
        ).grid(row=0, columnspan=3, padx=10, pady=10)

        self.menu_labels = {}
        self.menu_quantities = {}

        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(
                frame,
                text=f"{item} (₹{price}):",
                font=("Arial", 12)
            )
            label.grid(row=i, column=0, padx=10, pady=5)
            self.menu_labels[item] = label

            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = quantity_entry

        self.currency_var = tk.StringVar()
        ttk.Label(
            frame,
            text="Currency:",
            font=("Arial", 12)
        ).grid(
            row=len(self.menu_items) + 1,
            column=0,
            padx=10,
            pady=5
        )

        currency_dropdown = ttk.Combobox(
            frame,
            textvariable=self.currency_var,
            state="readonly",
            width=18,
            values=("INR", "USD")
        )
        currency_dropdown.grid(
            row=len(self.menu_items) + 1,
            column=1,
            padx=10,
            pady=5
        )
        currency_dropdown.current(0)
        self.currency_var.trace("w", self.update_menu_prices)

        order_button = ttk.Button(
            frame,
            text="Place Order",
            command=self.place_order
        )
        order_button.grid(
            row=len(self.menu_items) + 2,
            columnspan=3,
            padx=10,
            pady=10
        )

    def setup_background(self, root):
        bg_width, bg_height = 800, 600
        canvas = tk.Canvas(root, width=bg_width, height=bg_height)
        canvas.pack()

        
        opened_image = Image.open("South Indian Res BG.jpg")
        resized_image = opened_image.resize((bg_width, bg_height), Image.Resampling.LANCZOS)
        
        background_image = ImageTk.PhotoImage(resized_image)

        canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
        canvas.image = background_image # Keep a reference so garbage collection doesn't delete it

    def update_menu_prices(self, *args):
        currency = self.currency_var.get()
        symbol = "$" if currency == "USD" else "₹"
        rate = self.exchange_rate if currency == "USD" else 1

        for item, label in self.menu_labels.items():
            price = round(self.menu_items[item] * rate, 2)
            label.config(text=f"{item} ({symbol}{price}):")

    def place_order(self):
        total_cost = 0
        order_summary = "Order Summary:\n"
        currency = self.currency_var.get()
        symbol = "$" if currency == "USD" else "₹"
        rate = self.exchange_rate if currency == "USD" else 1

        for item, entry in self.menu_quantities.items():
            quantity = entry.get()
            if quantity.isdigit():
                quantity = int(quantity)
                price = round(self.menu_items[item] * rate, 2)
                cost = round(quantity * price, 2)
                total_cost += cost

                if quantity > 0:
                    order_summary += (
                        f"{item}: {quantity} x {symbol}{price} = {symbol}{cost}\n"
                    )

        if total_cost > 0:
            order_summary += f"\nTotal Cost: {symbol}{round(total_cost, 2)}"
            messagebox.showinfo("Order Placed", order_summary)
        else:
            messagebox.showerror("Error", "Please order at least one item.")

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantOrderManagement(root)
    root.geometry("800x600")
    root.mainloop()