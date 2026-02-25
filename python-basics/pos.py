import tkinter as tk
from tkinter import messagebox

# ------------------ DATA ------------------
inventory = {
    "Milk": 120,
    "Bread": 50,
    "Eggs": 10,
    "Sugar": 100,
    "Butter": 200
}

cart = {}
total_amount = 0

# ------------------ FUNCTIONS ------------------

def add_to_cart():
    global total_amount   # must be at the top
    item = item_entry.get()
    qty = qty_entry.get()

    if item not in inventory:
        messagebox.showerror("Error", f"{item} not in inventory")
        return

    try:
        qty = int(qty)
        if qty <= 0:
            raise ValueError
    except:
        messagebox.showerror("Error", "Quantity must be a positive integer")
        return

    # Add item to cart
    if item in cart:
        cart[item] += qty
    else:
        cart[item] = qty

    total_amount += inventory[item] * qty
    update_cart_display()


def update_cart_display():
    cart_list.delete(0, tk.END)
    for item, qty in cart.items():
        price = inventory[item] * qty
        cart_list.insert(tk.END, f"{item} x{qty} - KES {price}")
    total_label.config(text=f"Total: KES {total_amount}")


def checkout():
    global total_amount   # must be at the top

    if not cart:
        messagebox.showerror("Error", "Cart is empty")
        return

    method = payment_var.get()
    if method == "":
        messagebox.showerror("Error", "Select a payment method")
        return

    messagebox.showinfo("Payment Successful", f"Paid KES {total_amount} via {method}")
    cart.clear()
    total_amount = 0
    update_cart_display()
    payment_var.set("")


# ------------------ GUI ------------------

root = tk.Tk()
root.title("Supermarket POS")
root.geometry("500x600")

# --- Item Input ---
tk.Label(root, text="Item Name").pack(pady=5)
item_entry = tk.Entry(root)
item_entry.pack()

tk.Label(root, text="Quantity").pack(pady=5)
qty_entry = tk.Entry(root)
qty_entry.pack()

tk.Button(root, text="Add to Cart", command=add_to_cart, bg="blue", fg="white").pack(pady=10)

# --- Cart Display ---
tk.Label(root, text="Cart", font=("Arial", 14)).pack(pady=10)
cart_list = tk.Listbox(root, width=50)
cart_list.pack()

# --- Total Display ---
total_label = tk.Label(root, text="Total: KES 0", font=("Arial", 14))
total_label.pack(pady=10)

# --- Payment Methods ---
tk.Label(root, text="Payment Method").pack(pady=5)
payment_var = tk.StringVar()
tk.Radiobutton(root, text="Cash", variable=payment_var, value="Cash").pack()
tk.Radiobutton(root, text="Card", variable=payment_var, value="Card").pack()

tk.Button(root, text="Checkout", command=checkout, bg="green", fg="white").pack(pady=20)

root.mainloop()