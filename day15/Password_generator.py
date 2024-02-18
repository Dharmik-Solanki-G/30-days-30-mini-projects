import random
import string
import pyperclip
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Please select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_copy_password():
    try:
        length = int(length_entry.get())
        use_uppercase = uppercase_var.get()
        use_lowercase = lowercase_var.get()
        use_digits = digits_var.get()
        use_special = special_var.get()

        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        if password:
            password_entry.delete(0, 'end')
            password_entry.insert(0, password)
            pyperclip.copy(password)
            messagebox.showinfo("Password Generated", "Password copied to clipboard.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

def clear_password_entry():
    password_entry.delete(0, 'end')

root = tk.Tk()
root.title("Password Generator")

# Configure style for ttk widgets
style = ttk.Style()
style.theme_use("clam")  # Change the theme to any theme you like

# Change default settings for all widgets
style.configure('.', background='#121212', foreground='#eeeeee', font=('Arial', 12))

# Specific adjustments for certain widgets
style.configure('TLabel', background='#121212', foreground='#eeeeee')
style.configure('TCheckbutton', background='#121212', foreground='#eeeeee')
style.configure('TButton', background='#37474f', foreground='#eeeeee', padding=10)

# Override text color for TEntry widget
style.configure('TEntry', foreground='black')

main_frame = ttk.Frame(root, padding="20")
main_frame.grid(row=0, column=0)

length_label = ttk.Label(main_frame, text="Password Length:")
length_label.grid(row=0, column=0, sticky="w")
length_entry = ttk.Entry(main_frame, width=5)
length_entry.grid(row=0, column=1)
length_entry.insert(0, "12")

options_label = ttk.Label(main_frame, text="Character Types:")
options_label.grid(row=1, column=0, sticky="w")

uppercase_var = tk.BooleanVar()
uppercase_check = ttk.Checkbutton(main_frame, text="Uppercase", variable=uppercase_var)
uppercase_check.grid(row=1, column=1, sticky="w")
uppercase_var.set(True)

lowercase_var = tk.BooleanVar()
lowercase_check = ttk.Checkbutton(main_frame, text="Lowercase", variable=lowercase_var)
lowercase_check.grid(row=2, column=1, sticky="w")
lowercase_var.set(True)

digits_var = tk.BooleanVar()
digits_check = ttk.Checkbutton(main_frame, text="Digits", variable=digits_var)
digits_check.grid(row=3, column=1, sticky="w")
digits_var.set(True)

special_var = tk.BooleanVar()
special_check = ttk.Checkbutton(main_frame, text="Special Characters", variable=special_var)
special_check.grid(row=4, column=1, sticky="w")
special_var.set(True)

generate_button = ttk.Button(main_frame, text="Generate Password", command=generate_and_copy_password)
generate_button.grid(row=5, column=0, columnspan=2, pady=10)

password_label = ttk.Label(main_frame, text="Generated Password:")
password_label.grid(row=6, column=0, sticky="w")
password_entry = ttk.Entry(main_frame, width=30)
password_entry.grid(row=6, column=1, sticky="w")

clear_button = ttk.Button(main_frame, text="Clear Password", command=clear_password_entry)
clear_button.grid(row=7, column=0, columnspan=2, pady=10)

root.mainloop()