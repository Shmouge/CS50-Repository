import tkinter as tk
from tkinter import messagebox

def add():
    calculate(lambda x, y: x + y)

def subtract():
    calculate(lambda x, y: x - y)

def multiply():
    calculate(lambda x, y: x * y)

def divide():
    try:
        calculate(lambda x, y: x / y)
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")

def calculate(operation):
    try:
        x = float(entry1.get())
        y = float(entry2.get())
        result = operation(x, y)
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# GUI setup
root = tk.Tk()
root.title("Simple Calculator")

tk.Label(root, text="First Number:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Second Number:").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Button(root, text="Add", command=add).grid(row=2, column=0)
tk.Button(root, text="Subtract", command=subtract).grid(row=2, column=1)
tk.Button(root, text="Multiply", command=multiply).grid(row=3, column=0)
tk.Button(root, text="Divide", command=divide).grid(row=3, column=1)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()