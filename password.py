import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    username = username_entry.get()
    password_length = int(length_entry.get())
    
    if password_length < 8:
        messagebox.showwarning("Invalid Length", "Password length should be at least 8 characters.")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choice(characters) for _ in range(password_length))
    
    result_label.config(text=f"Generated Password for {username}: {generated_password}")


root = tk.Tk()
root.title("Password Generator")


username_label = tk.Label(root, text="Enter Username:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()


root.mainloop()
