import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# ------------------------
# PRODUCT DATABASE (KES)
# ------------------------

products = {
    "Coca Cola 500ml": {"price": 80, "stock": 50},
    "Milk 1L": {"price": 65, "stock": 40},
    "Bread": {"price": 60, "stock": 35},
    "Sugar 1kg": {"price": 180, "stock": 25},
    "Eggs Tray": {"price": 420, "stock": 15},
    "Rice 2kg": {"price": 300, "stock": 20},
    "Cooking Oil 1L": {"price": 240, "stock": 30},
    "Juice 1L": {"price": 120, "stock": 45},
}

cart = {}

VAT_RATE = 0.16  # Kenya VAT 16%

# ------------------------
# FUNCTIONS
# ------------------------

def add_to_cart(product):
    if products[product]["stock"] <= 0:
        messagebox.showwarning("Out of Stock", f"{product} is out of stock!")
        return

    cart[product] = cart.get(product, 0) + 1
    products[product]["stock"] -= 1
    update_cart()
    refresh_products()


def increase_qty(product):
    add_to_cart(product)


def decrease_qty(product):
    if product in cart:
        cart[product] -= 1
        products[product]["stock"] += 1
        if cart[product] <= 0:
            del cart[product]
    update_cart()
    refresh_products()


def update_cart():
    for widget in cart_frame.winfo_children():
        widget.destroy()

    subtotal = 0

    for product, qty in cart.items():
        price = products[product]["price"]
        total_price = price * qty
        subtotal += total_price

        row = tk.Frame(cart_frame, bg="white")
        row.pack(fill="x", pady=2)

        tk.Label(row, text=product, bg="white").pack(side="left")

        tk.Button(row, text="-", command=lambda p=product: decrease_qty(p)).pack(side="right")
        tk.Label(row, text=f"{qty}", width=3, bg="white").pack(side="right")
        tk.Button(row, text="+", command=lambda p=product: increase_qty(p)).pack(side="right")

    vat = subtotal * VAT_RATE
    total = subtotal + vat

    subtotal_label.config(text=f"Subtotal: KES {subtotal:.2f}")
    vat_label.config(text=f"VAT (16%): KES {vat:.2f}")
    total_label.config(text=f"TOTAL: KES {total:.2f}")


def process_payment():
    if not cart:
        messagebox.showwarning("Empty Cart", "No items in cart!")
        return

    payment_method = payment_var.get()
    receipt = "====== QUICKMART RECEIPT ======\n\n"

    subtotal = 0
    for product, qty in cart.items():
        price = products[product]["price"]
        total_price = price * qty
        subtotal += total_price
        receipt += f"{product} x{qty} - KES {total_price}\n"

    vat = subtotal * VAT_RATE
    total = subtotal + vat

    receipt += "\n----------------------------\n"
    receipt += f"Subtotal: KES {subtotal:.2f}\n"
    receipt += f"VAT (16%): KES {vat:.2f}\n"
    receipt += f"TOTAL: KES {total:.2f}\n"
    receipt += f"Payment: {payment_method}\n"
    receipt += "\nThank you for shopping!\n"

    messagebox.showinfo("Receipt", receipt)

    cart.clear()
    update_cart()


def refresh_products():
    for widget in product_frame.winfo_children():
        widget.destroy()

    search_text = search_var.get().lower()

    for product, data in products.items():
        if search_text in product.lower():
            frame = tk.Frame(product_frame, bg="white", bd=2, relief="ridge")
            frame.pack(padx=5, pady=5, fill="x")

            tk.Label(frame, text=product, font=("Arial", 10, "bold"), bg="white").pack()
            tk.Label(frame, text=f"KES {data['price']}", fg="blue", bg="white").pack()
            tk.Label(frame, text=f"Stock: {data['stock']}", fg="green", bg="white").pack()

            tk.Button(frame, text="Add to Cart",
                      command=lambda p=product: add_to_cart(p),
                      bg="#2d89ef", fg="white").pack(pady=3)


# ------------------------
# GUI SETUP
# ------------------------

root = tk.Tk()
root.title("QuickMart Supermarket POS - Kenya")
root.geometry("1100x600")
root.configure(bg="#f4f6f9")

# LEFT SIDE (PRODUCTS)

left_frame = tk.Frame(root, bg="#f4f6f9")
left_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

tk.Label(left_frame, text="Products",
         font=("Arial", 18, "bold"), bg="#f4f6f9").pack()

search_var = tk.StringVar()
search_bar = tk.Entry(left_frame, textvariable=search_var)
search_bar.pack(fill="x", pady=5)
search_bar.bind("<KeyRelease>", lambda e: refresh_products())

product_frame = tk.Frame(left_frame, bg="#f4f6f9")
product_frame.pack(fill="both", expand=True)

# RIGHT SIDE (CART)

right_frame = tk.Frame(root, bg="white", width=350)
right_frame.pack(side="right", fill="y")

tk.Label(right_frame, text="Current Order",
         font=("Arial", 16, "bold"), bg="white").pack(pady=10)

cart_frame = tk.Frame(right_frame, bg="white")
cart_frame.pack(fill="both", expand=True)

subtotal_label = tk.Label(right_frame, text="Subtotal: KES 0.00", bg="white")
subtotal_label.pack()

vat_label = tk.Label(right_frame, text="VAT (16%): KES 0.00", bg="white")
vat_label.pack()

total_label = tk.Label(right_frame, text="TOTAL: KES 0.00",
                       font=("Arial", 14, "bold"), fg="green", bg="white")
total_label.pack(pady=10)

# Payment Method
payment_var = tk.StringVar(value="Cash")

tk.Label(right_frame, text="Payment Method:", bg="white").pack()

payment_dropdown = ttk.Combobox(
    right_frame,
    textvariable=payment_var,
    values=["Cash", "M-Pesa", "Card"],
    state="readonly"
)
payment_dropdown.pack(pady=5)

tk.Button(right_frame, text="PAY NOW",
          bg="#28a745", fg="white",
          font=("Arial", 12, "bold"),
          command=process_payment).pack(pady=10)

refresh_products()
root.mainloop()