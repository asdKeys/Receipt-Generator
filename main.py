import tkinter as tk
import random
from datetime import datetime

items = [
    ("Milk", 3.48),
    ("Eggs", 2.97),
    ("Bananas", 1.24),
    ("Bread", 1.98),
    ("Coke(2liters)", 7.48),
    ("American Cheese(plastic)", 2.78),
    ("Cheddar Cheese", 4.58),
    ("Chicken", 8.96),
    ("Beef", 6.97),
    ("Rice", 4.38),
    ("Chips", 3.28),
    ("Apple Juice", 3.48),
    ("Cereal", 3.76),
    ("Pizza", 5.97),
    ("Ice Cream", 4.98),
    ("Cookies", 2.48),
    ("Orange Juice", 4.28),
    ("Tomatoes", 2.96),
    ("Potatoes", 3.47),
    ("Onions", 8.94),
    ("Fried Chicken", 9.97)
]

TAX_RATE = 0.0825

def generate_receipt():
    receipt_text.config(state="normal")
    receipt_text.delete("1.0", tk.END)

    store = random.randint(100, 999)
    transaction = random.randint(100000, 999999)
    card_last4 = random.randint(1000, 9999)

    selected_items = random.sample(items, random.randint(5, 8))

    subtotal = 0

    receipt_text.insert(tk.END, "================================\n")
    receipt_text.insert(tk.END, "            WALMART\n")
    receipt_text.insert(tk.END, "      YOUR FAVORITE STORE\n")
    receipt_text.insert(tk.END, "================================\n")
    receipt_text.insert(tk.END, f"Store #: {store}\n")
    receipt_text.insert(tk.END, datetime.now().strftime("%m/%d/%Y  %I:%M %p") + "\n")
    receipt_text.insert(tk.END, f"Transaction #: {transaction}\n")
    receipt_text.insert(tk.END, "--------------------------------\n")

    for name, price in selected_items:
        quantity = random.randint(1, 3)
        item_total = price * quantity
        subtotal += item_total

        receipt_text.insert(
            tk.END,
            f"{name[:24]:24} x{quantity} ${item_total:>6.2f}\n"
        )

    tax = subtotal * TAX_RATE
    total = subtotal + tax

    receipt_text.insert(tk.END, "--------------------------------\n")
    receipt_text.insert(tk.END, f"{'Subtotal':24} ${subtotal:>7.2f}\n")
    receipt_text.insert(tk.END, f"{'Tax (8.25%)':24} ${tax:>7.2f}\n")
    receipt_text.insert(tk.END, "--------------------------------\n")
    receipt_text.insert(tk.END, f"{'TOTAL':24} ${total:>7.2f}\n")
    receipt_text.insert(tk.END, "--------------------------------\n")
    receipt_text.insert(tk.END, "Payment: CREDIT CARD\n")
    receipt_text.insert(tk.END, f"Card: **** **** **** {card_last4}\n")
    receipt_text.insert(tk.END, "\n")
    receipt_text.insert(tk.END, "     Thank you for shopping!\n")
    receipt_text.insert(tk.END, "        Please come again!\n")
    receipt_text.insert(tk.END, "\n")
    receipt_text.insert(tk.END, "     *** SIMULATED RECEIPT ***\n")
    receipt_text.insert(tk.END, "================================\n")

    receipt_text.config(state="disabled")

window = tk.Tk()
window.title("Receipt Generator")
window.geometry("850x650")
window.configure(bg="#eeeeee")

title = tk.Label(
    window,
    text="Receipt Generator",
    font=("Arial", 24, "bold"),
    bg="#eeeeee"
)
title.pack(pady=15)

main_frame = tk.Frame(window, bg="#eeeeee")
main_frame.pack(fill="both", expand=True)

receipt_frame = tk.Frame(main_frame, bg="#eeeeee")
receipt_frame.pack(side="left", anchor="n", padx=(50, 0), pady=10)

receipt_text = tk.Text(
    receipt_frame,
    width=42,
    height=30,
    font=("Courier New", 10),
    bg="white",
    fg="black",
    relief="solid",
    borderwidth=1
)
receipt_text.pack()

button_frame = tk.Frame(
    main_frame,
    bg="#eeeeee"
)
button_frame.pack(
    side="right",
    fill="both",
    expand=True,
    padx=(80, 50)
)

button_title = tk.Label(
    button_frame,
    text="Receipt Controls",
    font=("Arial", 20, "bold"),
    bg="#eeeeee"
)
button_title.pack(pady=(180, 25))

refresh_button = tk.Button(
    button_frame,
    text="REFRESH RECEIPT",
    font=("Arial", 16, "bold"),
    bg="#0071ce",
    fg="white",
    activebackground="#005fa3",
    activeforeground="white",
    padx=30,
    pady=15,
    command=generate_receipt
)
refresh_button.pack()

generate_receipt()

window.mainloop()

