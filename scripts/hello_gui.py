import tkinter as tk

#note: Create the main application window
root = tk.Tk()
root.title("My First Tkinter App")
root.geometry("300x150")  # Width x Height

#note: Create a label
label = tk.Label(root, text="Welcome to Mycoceuticals GUI!")
label.pack(pady=20)

#note: Run the app
root.mainloop()