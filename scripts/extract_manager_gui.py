import tkinter as tk
from tkinter import ttk
from datetime import datetime
import json
import os
#note: File to persist batch data
DATA_FILE = "batches.json"

#note: Try to load existing data
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        batches = json.load(f)
else:
    batches = {}

#note: Create the main app window
root = tk.Tk()
root.title("🍄 Mycoceuticals Extract Manager")
root.geometry("700x500")
root.resizable(False, False)

#note: Dictionary to hold all batches
batches = {}

#note: Function to calculate dried weight
def calculate_dried_weight(fresh_weight):
    try:
        return round(float(fresh_weight) * 0.10, 2)
    except ValueError:
        return "Invalid"

#note: Save all batches to file
def save_to_file():
    with open(DATA_FILE, "w") as f:
        json.dump(batches, f, indent=4)

#note: Add or update batch
def save_batch():
    code = entry_code.get()
    strain = entry_strain.get()
    method = method_var.get()
    ratio = entry_ratio.get()
    volume = entry_volume.get()
    weight = entry_weight.get()
    date = datetime.now().strftime("%Y-%m-%d")

    if code == "" or strain == "":
        return

    dried_weight = calculate_dried_weight(weight)

    batches[code] = {
        "strain": strain,
        "method": method,
        "ratio": ratio,
        "volume": volume,
        "fresh_weight": weight,
        "dried_weight": dried_weight,
        "added_on": date
    }

    save_to_file()
    refresh_tree()
    clear_fields()

#note: Clear the input fields after adding
def clear_fields():
    entry_code.delete(0, tk.END)
    entry_strain.delete(0, tk.END)
    method_var.set(method_options[0])
    entry_ratio.delete(0, tk.END)
    entry_volume.delete(0, tk.END)
    entry_weight.delete(0, tk.END)

def refresh_tree():
    for row in tree.get_children():
        tree.delete(row)
    for code, details in batches.items():
        tree.insert("", "end", values=(code, details["strain"], details["method"], details["volume"], details["dried_weight"]))

#note: Labels and Entry Fields
tk.Label(root, text="Batch Code").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_code = tk.Entry(root, width=20)
entry_code.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Strain").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_strain = tk.Entry(root, width=20)
entry_strain.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Extraction Method").grid(row=2, column=0, padx=10, pady=5, sticky="w")
method_options = ["Dual (Water + ACV)", "Water Only", "ACV Only"]
method_var = tk.StringVar(value=method_options[0])
dropdown_method = tk.OptionMenu(root, method_var, *method_options)
dropdown_method.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Ratio").grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_ratio = tk.Entry(root, width=20)
entry_ratio.grid(row=3, column=1, padx=5, pady=5)

tk.Label(root, text="Volume").grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry_volume = tk.Entry(root, width=20)
entry_volume.grid(row=4, column=1, padx=5, pady=5)

tk.Label(root, text="Fresh Weight (g)").grid(row=5, column=0, padx=10, pady=5, sticky="w")
entry_weight = tk.Entry(root, width=20)
entry_weight.grid(row=5, column=1, padx=5, pady=5)

#note: Add Button
btn_add = tk.Button(root, text="Save / Update Batch", command=save_batch, bg="#4CAF50", fg="white", width=20)
btn_add.grid(row=6, column=1, pady=10)

#note: Treeview Table for Displaying Batches
columns = ("code", "strain", "method", "volume", "dried_weight")
tree = ttk.Treeview(root, columns=columns, show="headings", height=10)
tree.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

for col in columns:
    tree.heading(col, text=col.replace("_", " ").capitalize())
    tree.column(col, width=130)

#note: Start the GUI
root.mainloop()