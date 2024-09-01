import tkinter as tk
from tkinter import messagebox

menu = {
    "ESPRESSO": 150,
    "LONG BLACK": 250,
    "CORTADO": 350,
    "CAPPUCCINO": 200,
    "TRUE CHOCOLATE": 250,
    "OREO WAFFLE": 100,
    "TRIPLE CHOCOLATE WAFFLE": 120,
    "BLUEBERRY CHEESECAKE WAFFLE": 150,
    "BLACK CURRANT WAFFLE": 170,
    "MAPLE BUTTER WAFFLE ": 180
}

items_purchased = []

def calculate_total():
    try:
        quantity = int(quantity_entry.get())
        selected_item = menu_var.get()

        if selected_item not in menu:
            messagebox.showerror("Error", "Invalid menu item.")
            return

        price = menu[selected_item]

        tax_rate = 0.09 
        subtotal = quantity * price
        tax = subtotal * tax_rate
        total = subtotal + tax

        selected_item_label.config(text="Selected Item: %s (₹%.2f)" % (selected_item, price))

        items_purchased.append((selected_item, price, quantity, total))

        user_choice = messagebox.askyesno("Confirmation", "Do you want to add more items?")

        if user_choice:
            receipt_textbox.delete("1.0", tk.END)
            receipt_textbox.insert(tk.END, "Please add more items.")

        else:
            grand_total = sum(item[3] for item in items_purchased)  

            receipt_text = "Receipt:\n\n"
            for item in items_purchased:
                item_name, item_price, item_quantity, item_total = item
                receipt_text += f"Item: {item_name}\nPrice: ₹{item_price:.2f}\nQuantity: {item_quantity}\nTotal: ₹{item_total:.2f}\n\n"

            receipt_text += f"Grand Total: ₹{grand_total:.2f}"

            receipt_textbox.delete("1.0", tk.END)
            receipt_textbox.insert(tk.END, receipt_text)

            items_purchased.clear() 

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

def exit_app():
    window.destroy()

window = tk.Tk()
window.title("Cafe Bill Calculator")
can = tk.Canvas(window, height=500, width=470, bg="lavender")
can.create_line(0, 50, 470, 50)
can.pack()

window.geometry("470x470")
window.resizable(False, False)

cafename = tk.Label(window, text="UKUSA CAFE", font=("times", 17), bg="lavender")
cafename.place(x=145, y=10)

menu_label = tk.Label(window, text="Menu:", bg="lavender")
menu_label.place(x=150, y=65)

menu_var = tk.StringVar(window)
menu_var.set("ESPRESSO")  

menu_options = list(menu.keys())
menu_dropdown = tk.OptionMenu(window, menu_var, *menu_options)
menu_dropdown.place(x=200, y=60)

selected_item_label = tk.Label(window, text="Selected Item: %s (₹%.2f)" % (menu_var.get(), menu[menu_var.get()]), bg="lavender")
selected_item_label.place(x=150, y=100)

quantity_label = tk.Label(window, text="Quantity:", bg="lavender")
quantity_label.place(x=150, y=130)
quantity_entry = tk.Entry(window)
quantity_entry.place(x=210, y=130)

calculate_button = tk.Button(window, text="Calculate", command=calculate_total, width=15, activebackground="grey", activeforeground="blue")
calculate_button.place(x=190, y=170)

receipt_label = tk.Label(window, text="Receipt:", bg="lavender")
receipt_label.place(x=150, y=205)

receipt_textbox = tk.Text(window, height=10, width=40)
receipt_textbox.place(x=80, y=230)

scrollbar = tk.Scrollbar(window)
scrollbar.place(x=390, y=230, height=165)

receipt_textbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=receipt_textbox.yview)

exit_button = tk.Button(window, text="Exit", command=exit_app, width=15, activebackground="grey", activeforeground="blue")
exit_button.place(x=185, y=420)

receipt_textbox.bind("<Key>", lambda e: "break")
receipt_textbox.bind("<Button-1>", lambda e: "break")

window.mainloop()