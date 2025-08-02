
import tkinter as tk
from tkinter import messagebox

# Create main window
win = tk.Tk()
win.title("Smart Calculator")
win.geometry("300x400")
win.configure(bg="black")

# Entry field for input/output
expression = ""
entry = tk.Entry(win, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify='right', bg="gray20", fg="white")
entry.pack(fill="both", ipadx=8, ipady=15, pady=10, padx=10)

# Function to handle button clicks
def click(btn):
    global expression
    expression += str(btn)
    entry.delete(0, tk.END)
    entry.insert(tk.END, expression)

# Evaluate the expression
def calculate():
    global expression
    try:
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        expression = result
    except:
        messagebox.showerror("Error", "Invalid Input")
        expression = ""

# Clear the entry
def clear():
    global expression
    expression = ""
    entry.delete(0, tk.END)

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+'),
]

# Create buttons dynamically
for row in buttons:
    frame = tk.Frame(win, bg="black")
    frame.pack(expand=True, fill="both")
    for btn in row:
        if btn == '=':
            b = tk.Button(frame, text=btn, font=("Arial", 18), bg="darkgreen", fg="white",
                          command=calculate)
        else:
            b = tk.Button(frame, text=btn, font=("Arial", 18), bg="gray30", fg="white",
                          command=lambda b=btn: click(b))
        b.pack(side="left", expand=True, fill="both", padx=1, pady=1)

# Add clear button
clear_btn = tk.Button(win, text="Clear", font=("Arial", 18), bg="darkred", fg="white", command=clear)
clear_btn.pack(expand=True, fill="both", padx=10, pady=10)

# Start the GUI loop
win.mainloop()
