
            
import tkinter as tk
from tkinter import ttk

# Exchange rates dictionary
exchange_rates = {
    'USD': 1.0,
    'INR': 83.2,
    'EUR': 0.92,
    'GBP': 0.78,
    'JPY': 157.8,
    'CAD': 1.36,
    'BGN': 1.96
}

# Currency conversion logic
def convert():
    try:
        amount = float(from_amount_entry.get())
        from_curr = from_currency.get()
        to_curr = to_currency.get()

        if from_curr not in exchange_rates or to_curr not in exchange_rates:
            result_label.config(text="Unsupported currency.")
            return

        usd_amount = amount / exchange_rates[from_curr]
        converted = usd_amount * exchange_rates[to_curr]

        to_amount_entry.delete(0, tk.END)
        to_amount_entry.insert(0, f"{round(converted, 2)}")

        rate = round(exchange_rates[to_curr] / exchange_rates[from_curr], 4)
        rate_label.config(text=f"1 {from_curr} = {rate} {to_curr}", fg="green")

    except ValueError:
        result_label.config(text="Please enter a valid amount.", fg="red")


# Main window setup
root = tk.Tk()
root.title("Currency Converter")
root.configure(bg="white")
root.geometry("360x400")  # Set a mobile-friendly window size

# Title
title_label = tk.Label(root, text="Currency Converter", font=("Arial", 16, "bold"), bg="white")
title_label.pack(pady=20)

# Frame to center all widgets
main_frame = tk.Frame(root, bg="white")
main_frame.pack(expand=True)

# FROM section
from_label = tk.Label(main_frame, text="From", font=("Arial", 12), bg="white")
from_label.grid(row=0, column=0, padx=10, pady=5)

to_label = tk.Label(main_frame, text="To", font=("Arial", 12), bg="white")
to_label.grid(row=0, column=1, padx=10, pady=5)

from_amount_entry = tk.Entry(main_frame, font=("Arial", 12), width=15, justify='center')
from_amount_entry.grid(row=1, column=0, padx=10, pady=5)

to_amount_entry = tk.Entry(main_frame, font=("Arial", 12), width=15, justify='center')
to_amount_entry.grid(row=1, column=1, padx=10, pady=5)

from_currency = ttk.Combobox(main_frame, values=list(exchange_rates.keys()), font=("Arial", 11), width=12, justify='center')
from_currency.grid(row=2, column=0, padx=10, pady=5)
from_currency.set("EUR")

to_currency = ttk.Combobox(main_frame, values=list(exchange_rates.keys()), font=("Arial", 11), width=12, justify='center')
to_currency.grid(row=2, column=1, padx=10, pady=5)
to_currency.set("BGN")

# Convert button
convert_btn = tk.Button(root, text="Convert", font=("Arial", 13), bg="#4CAF50", fg="white", width=20, command=convert)
convert_btn.pack(pady=20)

# Result display
rate_label = tk.Label(root, text="", font=("Arial", 11), bg="white")
rate_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 10), bg="white")
result_label.pack()

# Run app
root.mainloop()

